from spell_correction.utils import *
from spell_correction.MaskedSentencePredictor import MaskedSentencePredictor
from spell_correction.NorvigSpellChecker import NorvigSpellChecker
from spell_correction.data_wiki import parser


class correct_spelling:
    def __init__(self):
        self.clean_text_model = CleanText()
        wikipedia = load_data(parser.get_path())
        wikipedia_words = self.clean_text_model.clean_text(wikipedia)

        self.spl = NorvigSpellChecker(wikipedia_words)
        self.bert_predictor = MaskedSentencePredictor()


    def get_correct_text(self, sentence):
        """
        Corrects the spelling of a given sentence.

        Args:
            sentence (str): A string representing the input sentence to correct.

        Returns:
            A string representing the corrected sentence.
        """
        
        # Split the sentence into words and clean it
        words = self.clean_text_model.clean_text(sentence)

        # Check each word for spelling errors
        for i, word in enumerate(words):
            # If the word is spelled correctly, keep it
            if word == self.spl.candidates(word):
                continue
            # Otherwise, replace it with a mask and predict the correct spelling
            else:
                words[i] = "[MASK]"
                masked_sentence = ' '.join(words)
                preds = self.bert_predictor.predict_masked_sent(masked_sentence, top_words=500)
                norvig_cands = self.spl.candidates(word)
                first_match = next((element for element in preds if element in norvig_cands), None)

                # If a correct spelling is found, replace the mask with the correct spelling
                if first_match:
                    words[i] = first_match
                else:
                    words[i] = self.spl.correction(word)

        # Check if the sentence contains homophones
        homophones_set = set(get_homophone_list())
        sentence_set = set(words)
        has_homophone = list(sentence_set.intersection(homophones_set))

        # If the sentence contains homophones, replace one with a mask and predict the correct spelling
        if has_homophone:
            homophone_index = words.index(has_homophone[0])
            words[homophone_index] = "[MASK]"
            masked_sentence = ' '.join(words)
            preds = self.bert_predictor.predict_masked_sent(masked_sentence, top_words=500)

            homophone_pair = find_homophone_pair(has_homophone[0])

            # If a correct spelling is found, replace the mask with the correct spelling
            if homophone_pair in preds:
                pred_index = preds.index(homophone_pair)
                words[homophone_index] = preds[pred_index]
            else:
                words[homophone_index] = has_homophone[0]

        # Join the corrected words back into a sentence
        corrected_sentence = ' '.join(words)
        
        return corrected_sentence
    


#Example Usage
model = correct_spelling()
print(model.get_correct_text("من صفر کردم"))