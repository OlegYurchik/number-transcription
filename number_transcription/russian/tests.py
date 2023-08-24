import pytest

from number_transcription.enums import GenderEnum, ScaleTypeEnum
from .conversion import number_to_words, words_to_number
from .enums import RussianUnit


@pytest.mark.parametrize(("number", "unit", "scale_type", "expected"), (
    (
        0,
        RussianUnit(one="сантиметр", any="сантиметра", many="сантиметров", gender=GenderEnum.MALE),
        None,
        "ноль сантиметров",
    ),
    (
        0,
        None,
        None,
        "ноль",
    ),
    (
        3000,
        RussianUnit(one="палец", any="пальца", many="пальцев", gender=GenderEnum.MALE),
        None,
        "три тысячи пальцев",
    ),
    (
        1,
        RussianUnit(one="кружка", any="кружки", many="кружек", gender=GenderEnum.FEMALE),
        None,
        "одна кружка",
    ),
    (
        141,
        RussianUnit(one="стакан", any="стакана", many="стаканов", gender=GenderEnum.MALE),
        None,
        "сто сорок один стакан",
    ),
    (
        3242,
        RussianUnit(one="ложка", any="ложки", many="ложек", gender=GenderEnum.FEMALE),
        ScaleTypeEnum.SHORT,
        "три тысячи двести сорок две ложки",
    ),
    (
        98765432,
        RussianUnit(one="нож", any="ножа", many="ножей", gender=GenderEnum.MALE),
        ScaleTypeEnum.LONG,
        "девяносто восемь миллионов семьсот шестьдесят пять тысяч четыреста тридцать два ножа",
    ),
    (
        100_200_300_400_500_612_713,
        None,
        ScaleTypeEnum.SHORT,
        (
            "сто квинтиллионов двести квадриллионов триста триллионов четыреста миллиардов пятьсот "
            "миллионов шестьсот двенадцать тысяч семьсот тринадцать"
        ),
    ),
    (
        10_911_812_713_614_515_416_317_218_119_020_000,
        RussianUnit(one="сковородка", any="сковородки", many="сковородок",
                    gender=GenderEnum.FEMALE),
        ScaleTypeEnum.LONG,
        (
            "десять квинтиллиардов девятьсот одиннадцать квинтиллионов восемьсот двенадцать "
            "квадриллиардов семьсот тринадцать квадриллионов шестьсот четырнадцать триллиардов "
            "пятьсот пятнадцать триллионов четыреста шестнадцать биллиардов триста семнадцать "
            "биллионов двести восемнадцать миллиардов сто девятнадцать миллионов двадцать тысяч "
            "сковородок"
        ),
    ),
    (
        1_000_000,
        None,
        ScaleTypeEnum.SHORT,
        "один миллион",
    ),
    # Skip
    # (
    #     10 ** 69,
    #     None,
    #     ScaleTypeEnum.LONG,
    #     "одна тысяча ундециллионов",
    # ),
))
def test_number_to_words(number: int, unit: RussianUnit | None,
                         scale_type: ScaleTypeEnum | None, expected: str):
    parameters = {
        "number": number,
        "unit": unit,
        "scale_type": scale_type,
    }
    parameters = {key: value for key, value in parameters.items() if value is not None}
    
    result = number_to_words(**parameters)

    assert result == expected


@pytest.mark.parametrize(("text", "scale_type", "expected"), (
    (
        "девятнадцать тысяч пятьсот три",
        None,
        19503,
    ),
    (
        "восемьсот пятьдесят две тысячи двадцать одна ложка",
        None,
        852021,
    ),
    (
        "Шестьдесят-Пять тЫсЯча и ТриСта тридцать, четыре",
        None,
        65334,
    ),
    (
        "пятьдесят восемь новемдециллионов четыреста сорок девять",
        None,
        58 * (10 ** 60) + 449,
    ),
    (
        "семьдесят семь новемдециллионов сто тринадцать",
        ScaleTypeEnum.LONG,
        77 * (10 ** 114) + 113,
    ),
))
def test_words_to_number(text: str, scale_type: ScaleTypeEnum | None, expected: str):
    parameters = {
        "text": text,
        "scale_type": scale_type,
    }
    parameters = {key: value for key, value in parameters.items() if value is not None}

    result = words_to_number(**parameters)

    assert result == expected
