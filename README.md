# Persian Spelling Corrector

This project provides a Persian spelling correction tool that can detect and correct spelling errors in Persian sentences using a combination of techniques including a custom spell checker, BERT-based masked language model for context prediction, and homophone detection.

## Features

- **Spelling Correction**: Detects and corrects spelling mistakes in Persian text using a Norvig-inspired spell checker based on word frequency.
- **Masked Sentence Prediction**: Utilizes a BERT model (`HooshvareLab/bert-fa-base-uncased`) to predict masked words in a sentence and correct spelling mistakes based on context.
- **Homophone Detection**: Identifies homophones in a sentence and attempts to replace them with the correct word based on context.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/parvvaresh/Persian-Spell-Correction-using-ParsBERT
   cd Persian-Spell-Correction-using-ParsBERT
   ```

2. **Install dependencies**:

   Make sure you have Python 3.6+ and pip installed. You will also need to install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```

   Required dependencies:

   - `torch`: For PyTorch and BERT model
   - `transformers`: For loading and using the pre-trained BERT model
   - `hazm`: Persian NLP library for tokenization and normalization
   - `re`: Regular expressions for text cleaning

3. **Download BERT model**:

   The project uses the pre-trained Persian BERT model (`HooshvareLab/bert-fa-base-uncased`). The model will be automatically downloaded by the `transformers` library when running the script.

## Usage

### Basic Usage

To use the spelling correction feature, simply instantiate the `correct_spelling` class and call the `get_correct_text()` method with the input sentence.

```python
from Spell_correction import correct_spelling

model = correct_spelling()
corrected_sentence = model.get_correct_text("من صفر کردم")
print(corrected_sentence)
```

### Explanation

- **`correct_spelling` Class**: This is the main class used to correct the spelling in a sentence. It uses:
  - `CleanText` class to preprocess and clean the input sentence.
  - `NorvigSpellChecker` to identify misspelled words and suggest corrections based on a frequency-based approach.
  - `MaskedSentencePredictor` to use a BERT model to predict the correct spelling of masked words based on the context.
  - Homophone detection to identify and replace homophones (words that sound the same but have different meanings or spellings).

### Example

```python
model = correct_spelling()
input_sentence = "من صفر کردم"
corrected_sentence = model.get_correct_text(input_sentence)
print(corrected_sentence)
```

The output will show the corrected version of the input sentence.

## File Structure

```
├── __pycache__                        # Compiled Python files
│   └── Spell_correction.cpython-312.pyc
├── spell_correction
│   ├── data_wiki
│   │   ├── parser.py                  # Data parsing utilities
│   │   ├── Persian-WikiText.txt       # Wikipedia corpus for spell-checker training
│   │   └── __pycache__                # Compiled files for the data_wiki module
│   ├── MaskedSentencePredictor.py     # BERT model for masked sentence prediction
│   ├── NorvigSpellChecker.py          # Norvig-inspired spell checker
│   ├── __pycache__                    # Compiled files for the spell_correction module
│   └── utils.py                       # Utility functions
└── Spell_correction.py                # Main script to run the spelling correction
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
