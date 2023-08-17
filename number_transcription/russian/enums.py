from dataclasses import dataclass

from number_transcription.enums import GenderEnum 


@dataclass()
class RussianUnit:
    one: str
    any: str
    many: str
    gender: GenderEnum
