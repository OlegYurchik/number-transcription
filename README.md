# Number Transcription

Multilanguage library for conversion numbers to words description

## Installation

**pip**
```shell
pip install number-transcription
```

**poetry**
```shell
poetry add number-transcription
```

**from source**
```shell
git clone https://github.com/OlegYurchik/number-transcription
pip install ./number_transcription
```

## Quick Start

```python
import number_transcription as nt


text = nt.russian.number_to_words(100_011)
print(text)  # сто тысяч одинадцать

text = nt.russian.number_to_words(
    1_015_000,
    unit=nt.russian.RussianUnitForm(one="ложка", any="ложки", many="ложек",
                                    gender=nt.enums.GenderEnum.FEMALE),
)
print(text)  # один миллион пятнадцать тысяч ложек
```
