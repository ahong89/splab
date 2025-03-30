from pydantic import BaseModel

class Total(BaseModel):
    total: float

class TabId(BaseModel):
    id: int

class CreateItemRequest(BaseModel):
    tab_id: int
    item_total: float

class UserToItem(BaseModel):
    item_id: int
    user_id: int
    portion: float

class UserPayRequest(BaseModel):
    user_id: int

