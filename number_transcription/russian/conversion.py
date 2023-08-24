import re

from number_transcription.enums import GenderEnum, ScaleTypeEnum
from .enums import RussianUnit
from .storage import (
    DOZENS,
    DOZENS_REVERSE,
    HUNDREDS,
    HUNDREDS_REVERSE,
    LONG_THOUSAND_POWERS,
    LONG_THOUSAND_POWERS_REVERSE,
    ONE_DOZEN,
    ONE_DOZEN_REVERSE,
    SHORT_THOUSAND_POWERS,
    SHORT_THOUSAND_POWERS_REVERSE,
    UNITS,
    UNITS_REVERSE,
)


def _choose_unit(number: int, unit: RussianUnit) -> str:
    tail = number % 100
    if 10 <= tail < 20:
        return unit.many
    elif tail % 10 == 1:
        return unit.one
    elif 2 <= tail % 10 < 5:
        return unit.any
    else:
        return unit.many


def number_to_words(number: int, unit: RussianUnit | None = None,
                    scale_type: ScaleTypeEnum = ScaleTypeEnum.SHORT) -> str:
    power = 0
    result = []
    if scale_type is ScaleTypeEnum.SHORT:
        thousand_powers = SHORT_THOUSAND_POWERS
    else:
        thousand_powers = LONG_THOUSAND_POWERS
    current_unit = unit

    while True:
        current_result = []

        # Add hundreds
        tail = number % 1000
        if (hundreds := tail // 100) > 0:
            current_result.append(HUNDREDS[hundreds])

        # Add dozens
        tail %= 100
        if 10 <= tail < 20:
            current_result.append(ONE_DOZEN[tail])
        elif (dozens := tail // 10) > 0:
            current_result.append(DOZENS[dozens])
        
        # Add units
        gender = GenderEnum.MALE if current_unit is None else current_unit.gender
        if tail % 10 > 0 and (tail < 10 or tail >= 20): 
            current_result.append(UNITS[tail % 10](gender))
        elif not result and not current_result and number == 0:
            current_result.append(UNITS[0](gender))

        # Add current unit
        if current_unit and (current_result or current_unit is unit):
            current_result.append(_choose_unit(tail, current_unit))            

        result = current_result + result

        # Increment iteration
        power += 3
        current_unit = thousand_powers.get(power)
        number //= 1000
        
        if number == 0:
            break

    return " ".join(result)


SEPARATOR_REGEXP = re.compile(r"[\W\d_]+")


def words_to_number(text: str, scale_type: ScaleTypeEnum = ScaleTypeEnum.SHORT) -> int:
    words = SEPARATOR_REGEXP.split(text)
    words = map(str.strip, words)
    words = filter(lambda element: bool(element), words)
    words = tuple(map(str.lower, words))
    number = 0

    if scale_type is ScaleTypeEnum.SHORT:
        thousand_powers_reverse = SHORT_THOUSAND_POWERS_REVERSE
    else:
        thousand_powers_reverse = LONG_THOUSAND_POWERS_REVERSE

    for word in words:
        if (thousand_power := thousand_powers_reverse.get(word)):
            number *= 10 ** thousand_power
        elif (hundreds := HUNDREDS_REVERSE.get(word)):
            number += hundreds * 100
        elif (dozens := DOZENS_REVERSE.get(word)):
            number += dozens * 10
        elif (one_dozen := ONE_DOZEN_REVERSE.get(word)):
            number += one_dozen
        elif (unit := UNITS_REVERSE.get(word)):
            number += unit

    return number
