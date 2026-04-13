
import enum

class ContractType(enum.Enum):
    alternance = "alternance"
    stage = "stage"
    cdi = "cdi"
    cdd = "cdd"
    poeic = "poeic"
    poec = "poec"
    freelance = "freelance"

class Sex(enum.Enum):
    male= "male"
    female = "female"


class Level(enum.Enum):
    debutant="debutant"
    intermediaire="intermediaire"
    avancé="avancé"