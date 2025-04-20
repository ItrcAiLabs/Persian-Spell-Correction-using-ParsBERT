# اصلاح‌گر املای فارسی

این پروژه ابزاری برای اصلاح املای جملات فارسی است که با استفاده از ترکیبی از تکنیک‌ها از جمله بررسی املایی سفارشی، مدل زبانی ماسک‌شده بر پایه BERT برای پیش‌بینی زمینه‌ای و تشخیص هم‌صداها می‌تواند خطاهای املایی را شناسایی و اصلاح کند.

## ویژگی‌ها

- **اصلاح املا**: با استفاده از یک بررسی‌گر املایی الهام‌گرفته از Norvig مبتنی بر فراوانی کلمات، خطاهای املایی در متن فارسی را شناسایی و اصلاح می‌کند.  
- **پیش‌بینی جمله ماسک‌شده**: از مدل BERT (`HooshvareLab/bert-fa-base-uncased`) برای پیش‌بینی کلمات ماسک‌شده در جمله استفاده می‌کند و بر اساس زمینه، اشتباهات املایی را اصلاح می‌نماید.  
- **تشخیص هم‌صدا**: هم‌صداها (کلماتی که مشابه تلفظ می‌شوند ولی معانی یا نگارش متفاوت دارند) را شناسایی کرده و با توجه به زمینه، تلاش می‌کند آن‌ها را با کلمهٔ صحیح جایگزین کند.  

## نصب

1. **کلون کردن مخزن**:

   ```bash
   git clone https://github.com/telegram-nlp-farsi/Persian-Spell-Correction-using-ParsBERT
   cd Persian-Spell-Correction-using-ParsBERT
   ```

2. **نصب وابستگی‌ها**:

   مطمئن شوید Python نسخهٔ 3.6 یا بالاتر و pip نصب شده است. همچنین باید بسته‌های پایتون مورد نیاز را نصب کنید.

   ```bash
   pip install -r requirements.txt
   ```

   وابستگی‌های مورد نیاز:
   - `torch`: برای PyTorch و مدل BERT  
   - `transformers`: برای بارگذاری و استفاده از مدل از پیش آموزش‌دیده BERT  
   - `hazm`: کتابخانهٔ NLP فارسی برای توکن‌سازی و نرمال‌سازی  
   - `re`: عبارات منظم برای تمیزسازی متن  

3. **دانلود مدل BERT**:

   این پروژه از مدل فارسی BERT از پیش آموزش‌دیده (`HooshvareLab/bert-fa-base-uncased`) استفاده می‌کند. مدل به‌صورت خودکار توسط کتابخانهٔ `transformers` هنگام اجرای اسکریپت دانلود خواهد شد.

## نحوه استفاده

### استفادهٔ پایه

برای استفاده از قابلیت اصلاح املا، کافی است کلاس `correct_spelling` را نمونه‌سازی کرده و متد `get_correct_text()` را با جملهٔ ورودی فراخوانی کنید:

```python
from Spell_correction import correct_spelling

model = correct_spelling()
corrected_sentence = model.get_correct_text("من صفر کردم")
print(corrected_sentence)
```

### توضیحات

- **کلاس `correct_spelling`**: این کلاس اصلی برای اصلاح املای جمله است و از اجزای زیر استفاده می‌کند:  
  - کلاس `CleanText` برای پیش‌پردازش و تمیزسازی جملهٔ ورودی.  
  - `NorvigSpellChecker` برای شناسایی کلمات اشتباه و پیشنهاد اصلاح بر اساس رویکرد فراوانی.  
  - `MaskedSentencePredictor` برای استفاده از مدل BERT جهت پیش‌بینی صحیح کلمات ماسک‌شده بر مبنای زمینه.  
  - تشخیص هم‌صداها برای شناسایی و جایگزینی کلمات غلط هم‌صدا با شکل درست.  



## ساختار فایل ها

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

## لایسنس

این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر، فایل [LICENSE](LICENSE) را ببینید.