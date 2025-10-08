import hazm
from collections import Counter
import re


homophones = [
    ["خار", "خوار"],
    ["سد", "صد"],
    ["خیش", "خویش"],
    ["خاست", "خواست"],
    ["ثواب", "صواب"],
    ["قاضی", "غازی"],
    ["علم", "الم"],
    ["غریب", "قریب"],
    ["غالب", "قالب"],
    ["پرتغال", "پرتقال"],
    ["غدیر", "قدیر"],
    ["حول", "هول"],
    ["اساس", "اثاث"],
    ["اسم", "اثم"],
    ["عمل", "امل"],
    ["امارت", "عمارت"],
    ["حیات", "حیاط"],
    ["سیف", "صیف"],
    ["خان", "خوان"],
    ["سفر", "صفر"],
    ["عرض", "ارز"],
    ["ارض", "ارز"],
    ["ارض", "عرض"],
    ["راضی", "رازی"],
    ["آقا", "آغا"],
    ["غذا", "قضا"],
    ["خرد", "خورد"],
    ["هضم", "حزم"],
    ["تهدید", "تحدید"],
    ["حوزه", "حوضه"],
    ["قدر", "غدر"],
    ["صر", "سر"],
]


def load_data(file_path):
    return open(file_path).read()


def find_homophone_pair(word):
    """
    Finds the homophone of a given word if it exists in the homophones list.
    :param word: The input word to search for.
    :return: The homophone of the given word if found, otherwise None.
    """
    for pair in homophones:
        if word in pair:
            new_pair = [*pair]
            new_pair.remove(word)
            return new_pair[0]
    return None


def get_homophone_list():
    """
    Generates a flat list of all homophones from the homophones list.
    :return: A list containing all words from homophone pairs.
    """
    return [
        word for pair in homophones for word in pair
    ]  # Flatten the list of homophone pairs


class CleanText:
    def __init__(self) -> None:
        """
        Initializes the clean_text class by defining a normalizer and a tokenizer
        using the Hazm library.
        """
        self.normalizer = hazm.Normalizer()
        self.tokenizer = hazm.WordTokenizer()

    def clean_text(self, text: str, output="word") -> str:
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
        punc_removed = re.sub(r"[^\w\s]", "", normalized_text)
        cleaned_text = self.tokenizer.tokenize(punc_removed)
        if output == "word":
            return cleaned_text
        else:
            return " ".join(cleaned_text)
