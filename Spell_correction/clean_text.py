import hazm
from collections import Counter
import re


class clean_text:
    def __init__(self) -> None:
        """
        Initializes the clean_text class by defining a normalizer and a tokenizer
        using the Hazm library.
        """
        self.normalizer = hazm.Normalizer()
        self.tokenizer = hazm.WordTokenizer()

    def clean_text(self, text: str, output='word') -> str:
        """
        Cleans and tokenizes the input text using the Hazm library.
        
        Steps performed:
        1. Normalizes the text to standardize characters and format.
        2. Removes punctuation from the text.
        3. Tokenizes the text into words or a single string.

        Args:
            text (str): The input text to be processed.
            output (str): Specifies the format of the output. 
                          'word' (default) returns a list of words. 
                          'sentence' returns the tokenized text as a single string.

        Returns:
            str: A list of tokenized words (if output='word') 
                 or a single tokenized sentence (if output='sentence').
        """
        normalized_text = self.normalizer.normalize(text)
        punc_removed = re.sub(r'[^\w\s]', '', normalized_text)
        cleaned_text = self.tokenizer.tokenize(punc_removed)
        if output == 'word':
            return cleaned_text
        else:
            return ' '.join(cleaned_text)
