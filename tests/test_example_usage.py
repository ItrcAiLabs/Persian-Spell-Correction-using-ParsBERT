# tests/test_example_usage.py
import os
import sys

# Ensure repo root is on sys.path (so `Spell_correction.py` is importable)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Prefer the top-level module; fall back to package path if you refactor later
try:
    from Spell_correction import correct_spelling
except ModuleNotFoundError:
    from spell_correction.correct_spelling import correct_spelling  # if moved later


def test_example_usage_exact_output():
    model = correct_spelling()
    assert model.get_correct_text("من صفر کردم") == "من سفر کردم"
