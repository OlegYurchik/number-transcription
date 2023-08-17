from enum import Enum


class GenderEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"


class ScaleTypeEnum(str, Enum):
    SHORT = "short"
    LONG = "long"
