from collections import Counter
import hazm  # Ensure you have the hazm library installed for Persian NLP processing


class NorvigSpellChecker:
    def __init__(self, words):
        """
        Initializes the spell checker with a dictionary of words and their frequencies.
        :param words: A list of words to build the frequency dictionary.
        """
        self.WORDS = Counter(
            words
        )  # Create a frequency dictionary from the input word list
        self.N = sum(self.WORDS.values())  # Total count of words
        self.letters = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"  # Persian alphabet

    def P(self, word):
        """
        Computes the probability of a word occurring in the corpus.
        :param word: The word whose probability is calculated.
        :return: Probability of the word.
        """
        return self.WORDS[word] / self.N

    def correction(self, word):
        """
        Returns the most probable spelling correction for the given word.
        :param word: The misspelled word.
        :return: The best correction based on probability.
        """
        return max(
            self.word_pool(word), key=self.P
        )  # Select the word with the highest probability

    def word_pool(self, word):
        """
        Generates a pool of possible correct words for the given input word.
        :param word: The word to find corrections for.
        :return: A set of possible corrections.
        """
        return (
            self.known([word])
            or self.known(self.edits1(word))
            or self.known(self.edits2(word))
            or [word]
        )  # Return the best available correction or the word itself if no corrections exist

    def candidates(self, word):
        """
        Generates a list of possible spelling corrections for the given word.
        :param word: The word to correct.
        :return: A sorted list of candidate words based on probability.
        """
        if self.WORDS[word] < 30 or (
            len(word) == 1 and word not in hazm.stopwords_list()
        ):
            candidates_list = list(
                self.known(self.edits1(word))
            )  # Get known one-edit words
            candidates_list.sort(
                key=self.P, reverse=True
            )  # Sort by probability in descending order
            return candidates_list
        else:
            return word  # If word is common enough, return it as is

    def known(self, words):
        """
        Filters the given list of words to only those present in the known dictionary.
        :param words: List of words to check.
        :return: A set of words that exist in the corpus.
        """
        return set(w for w in words if w in self.WORDS)

    def edits1(self, word):
        """
        Generates all possible words that are one edit away from the given word.
        Edits include deletions, transpositions, replacements, and insertions.
        :param word: The input word.
        :return: A set of possible one-edit words.
        """
        splits = [
            (word[:i], word[i:]) for i in range(len(word) + 1)
        ]  # All possible split points
        deletes = [L + R[1:] for L, R in splits if R]  # Deleting one character
        transposes = [
            L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1
        ]  # Swapping adjacent letters
        replaces = [
            L + c + R[1:] for L, R in splits if R for c in self.letters
        ]  # Replacing a character
        inserts = [
            L + c + R for L, R in splits for c in self.letters
        ]  # Inserting a new character
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        """
        Generates all possible words that are two edits away from the given word.
        :param word: The input word.
        :return: A generator of words with two edits.
        """
        return (
            e2 for e1 in self.edits1(word) for e2 in self.edits1(e1)
        )  # Apply edits1 twice
