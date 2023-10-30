from typing import List
from pydantic import BaseModel

class OpportunityBase(BaseModel):
    name: str
    
class SubscriptionTypeBase(BaseModel):
    name: str
    price: float
    subscription_type_infos: List[OpportunityBase]

class SubscriptionTypeGet(BaseModel):
    id: int
    name: str
    price: float
    subscription_type_infos: List[OpportunityBase]

class InfoTrainerBase(BaseModel):
    name: str
    

class TrainerBase(BaseModel):
    name: str
    price: float
    img_path: str
    age: int
    trainer_infos: List[InfoTrainerBase]

class TrainerGet(BaseModel):
    id: int
    name: str
    price: float
    img_path: str
    age: int
    trainer_infos: List[InfoTrainerBase]