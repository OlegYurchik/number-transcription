from number_transcription.enums import GenderEnum, ScaleTypeEnum
from .enums import RussianUnit
from .storage import (
    DOZENS,
    HUNDREDS,
    LONG_THOUSAND_POWERS,
    ONE_DOZEN,
    SHORT_THOUSAND_POWERS,
    UNITS,
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
    thousand_power = -1
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
        thousand_power += 1
        if thousand_power < len(thousand_powers):
            current_unit = thousand_powers[thousand_power]
        else:
            current_unit = None
        number //= 1000
        
        if number == 0:
            break

    return " ".join(result)
