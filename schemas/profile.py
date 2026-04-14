from pydantic import BaseModel
from datetime import datetime
from models.enum import ContractType,Sex


class ProfileCreate(BaseModel):
    name: str
    date_birthday: datetime
    sex: Sex
    experience: str
    diploma: str
    formation: str
    permis: bool
    contract_type: ContractType
    localisation: str
    disponibility: datetime
