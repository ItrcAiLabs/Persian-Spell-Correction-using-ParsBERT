from collections import Counter
import hazm

class NorvigSpellChecker:
    def __init__(self, words) -> None:
        self.counter_words = Counter(words)
        self.number_words = sum(
            self.counter_words.values()
        )
        self.persian_letters = 'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
    
    def probability(self, word : str) -> float:
        return self.counter_words[word] / self.number_words


    def correction(self, word : str) -> str:
        return max(
            self.word_probability(word) , key=self.probability
        )

    def word_probability(self, word : str):
        pass

    def extraction_words(self, words : list) -> set:
        return set(
            word for word in words if word in self.counter_words
        )
    

    def candidates(self, word : str) -> list:
        if (self.counter_words[word] < 30 
            or
            len(word) == 1
            and 
            word not in hazm.stopwords_list()):


