from number_transcription.enums import GenderEnum
from .enums import RussianUnit


SHORT_THOUSAND_POWERS = {
    3: RussianUnit(one="тысяча", any="тысячи", many="тысяч", gender=GenderEnum.FEMALE),
    6: RussianUnit(one="миллион", any="миллиона", many="миллионов", gender=GenderEnum.MALE),
    9: RussianUnit(one="миллиард", any="миллиарда", many="миллиардов", gender=GenderEnum.MALE),
    12: RussianUnit(one="триллион", any="триллиона", many="триллионов", gender=GenderEnum.MALE),
    15: RussianUnit(one="квадриллион", any="квадриллиона", many="квадриллионов",
                    gender=GenderEnum.MALE),
    18: RussianUnit(one="квинтиллион", any="квинтиллиона", many="квинтиллионов",
                    gender=GenderEnum.MALE),
    21: RussianUnit(one="секстиллион", any="секстиллиона", many="секстиллионов",
                    gender=GenderEnum.MALE),
    24: RussianUnit(one="септиллион", any="септиллиона", many="септиллионов",
                    gender=GenderEnum.MALE),
    27: RussianUnit(one="октиллион", any="октиллиона", many="октиллионов", gender=GenderEnum.MALE),
    30: RussianUnit(one="нониллион", any="нониллиона", many="нониллионов", gender=GenderEnum.MALE),
    33: RussianUnit(one="дециллион", any="дециллиона", many="дециллионов", gender=GenderEnum.MALE),
    36: RussianUnit(one="ундециллион", any="ундециллиона", many="ундециллионов",
                    gender=GenderEnum.MALE),
    39: RussianUnit(one="дуодециллион", any="дуодециллиона", many="дуодециллионов",
                    gender=GenderEnum.MALE),
    42: RussianUnit(one="тредециллион", any="тредециллиона", many="тредециллионов",
                    gender=GenderEnum.MALE),
    45: RussianUnit(one="кваттордециллион", any="кваттордециллиона", many="кваттордециллионов",
                    gender=GenderEnum.MALE),
    48: RussianUnit(one="квиндециллион", any="квиндециллиона", many="квиндециллионов",
                    gender=GenderEnum.MALE),
    51: RussianUnit(one="сексдециллион", any="сексдециллиона", many="сексдециллионов",
                    gender=GenderEnum.MALE),
    54: RussianUnit(one="септендециллион", any="септендециллиона", many="септендециллионов",
                    gender=GenderEnum.MALE),
    57: RussianUnit(one="октодециллион", any="октодециллиона", many="октодециллионов",
                    gender=GenderEnum.MALE),
    60: RussianUnit(one="новемдециллион", any="новемдециллиона", many="новемдециллионов",
                    gender=GenderEnum.MALE),
    63: RussianUnit(one="вигинтиллион", any="вигинтиллиона", many="вигинтиллионов",
                    gender=GenderEnum.MALE),
}
SHORT_THOUSAND_POWERS_REVERSE = {}
for power, unit in SHORT_THOUSAND_POWERS.items():
    SHORT_THOUSAND_POWERS_REVERSE.update({
        unit.one: power,
        unit.any: power,
        unit.many: power,
    })
LONG_THOUSAND_POWERS = {
    3: RussianUnit(one="тысяча", any="тысячи", many="тысяч", gender=GenderEnum.FEMALE),
    6: RussianUnit(one="миллион", any="миллиона", many="миллионов", gender=GenderEnum.MALE),
    9: RussianUnit(one="миллиард", any="миллиарда", many="миллиардов", gender=GenderEnum.MALE),
    12: RussianUnit(one="биллион", any="биллиона", many="биллионов", gender=GenderEnum.MALE),
    15: RussianUnit(one="биллиард", any="биллиарда", many="биллиардов", gender=GenderEnum.MALE),
    18: RussianUnit(one="триллион", any="триллиона", many="триллионов", gender=GenderEnum.MALE),
    21: RussianUnit(one="триллиард", any="триллиарда", many="триллиардов", gender=GenderEnum.MALE),
    24: RussianUnit(one="квадриллион", any="квадриллиона", many="квадриллионов",
                    gender=GenderEnum.MALE),
    27: RussianUnit(one="квадриллиард", any="квадриллиарда", many="квадриллиардов",
                    gender=GenderEnum.MALE),
    30: RussianUnit(one="квинтиллион", any="квинтиллиона", many="квинтиллионов",
                    gender=GenderEnum.MALE),
    33: RussianUnit(one="квинтиллиард", any="квинтиллиарда", many="квинтиллиардов",
                    gender=GenderEnum.MALE),
    36: RussianUnit(one="секстиллион", any="секстиллиона", many="секстиллионов",
                    gender=GenderEnum.MALE),
    39: RussianUnit(one="секстиллиард", any="секстиллиарда", many="секстиллиардов",
                    gender=GenderEnum.MALE),
    42: RussianUnit(one="септиллион", any="септиллиона", many="септиллионов",
                    gender=GenderEnum.MALE),
    45: RussianUnit(one="септиллиард", any="септиллиарда", many="септиллиардов",
                    gender=GenderEnum.MALE),
    48: RussianUnit(one="октиллион", any="октиллиона", many="октиллионов", gender=GenderEnum.MALE),
    51: RussianUnit(one="октиллиард", any="октиллиарда", many="октиллиардов",
                    gender=GenderEnum.MALE),
    54: RussianUnit(one="нониллион", any="нониллиона", many="нониллионов", gender=GenderEnum.MALE),
    57: RussianUnit(one="нониллиард", any="нониллиарда", many="нониллиардов",
                    gender=GenderEnum.MALE),
    60: RussianUnit(one="дециллион", any="дециллиона", many="дециллионов", gender=GenderEnum.MALE),
    63: RussianUnit(one="дециллиард", any="дециллиарда", many="дециллиардов",
                    gender=GenderEnum.MALE),
    66: RussianUnit(one="ундециллион", any="ундециллиона", many="ундециллионов",
                    gender=GenderEnum.MALE),
    72: RussianUnit(one="дуодециллион", any="дуодециллиона", many="дуодециллионов",
                    gender=GenderEnum.MALE),
    78: RussianUnit(one="тредециллион", any="тредециллиона", many="тредециллионов",
                    gender=GenderEnum.MALE),
    84: RussianUnit(one="кваттордециллион", any="кваттордециллиона", many="кваттордециллионов",
                    gender=GenderEnum.MALE),
    90: RussianUnit(one="квиндециллион", any="квиндециллиона", many="квиндециллионов",
                    gender=GenderEnum.MALE),
    96: RussianUnit(one="сексдециллион", any="сексдециллиона", many="сексдециллионов",
                    gender=GenderEnum.MALE),
    102: RussianUnit(one="септендециллион", any="септендециллиона", many="септендециллионов",
                     gender=GenderEnum.MALE),
    108: RussianUnit(one="октодециллион", any="октодециллиона", many="октодециллионов",
                     gender=GenderEnum.MALE),
    114: RussianUnit(one="новемдециллион", any="новемдециллиона", many="новемдециллионов",
                     gender=GenderEnum.MALE),
    120: RussianUnit(one="вигинтиллион", any="вигинтиллиона", many="вигинтиллионов",
                     gender=GenderEnum.MALE),
}
LONG_THOUSAND_POWERS_REVERSE = {}
for power, unit in LONG_THOUSAND_POWERS.items():
    LONG_THOUSAND_POWERS_REVERSE.update({
        unit.one: power,
        unit.any: power,
        unit.many: power,
    })
HUNDREDS = {
    1: "сто",
    2: "двести",
    3: "триста",
    4: "четыреста",
    5: "пятьсот",
    6: "шестьсот",
    7: "семьсот",
    8: "восемьсот",
    9: "девятьсот",
}
HUNDREDS_REVERSE = {
    value: count
    for count, value in HUNDREDS.items()
}
DOZENS = {
    2: "двадцать",
    3: "тридцать",
    4: "сорок",
    5: "пятьдесят",
    6: "шестьдесят",
    7: "семьдесят",
    8: "восемьдесят",
    9: "девяносто",
}
DOZENS_REVERSE = {
    value: count
    for count, value in DOZENS.items()
}
ONE_DOZEN = {
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
}
ONE_DOZEN_REVERSE = {
    value: count
    for count, value in ONE_DOZEN.items()
}
UNITS = {
    0: lambda gender: "ноль",
    1: lambda gender: "один" if gender == GenderEnum.MALE else "одна",
    2: lambda gender: "два" if gender == GenderEnum.MALE else "две",
    3: lambda gender: "три",
    4: lambda gender: "четыре",
    5: lambda gender: "пять",
    6: lambda gender: "шесть",
    7: lambda gender: "семь",
    8: lambda gender: "восемь",
    9: lambda gender: "девять",
}
UNITS_REVERSE = {
    "ноль": 0,
    "один": 1,
    "одна": 1,
    "два": 2,
    "две": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
}
