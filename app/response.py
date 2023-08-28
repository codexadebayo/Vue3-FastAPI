from pydantic import BaseModel

class Items(BaseModel):
    id:int
    strName: str
    strDescription: str
    strImg: str
    intPrice: int
    intInventory: int
    strCategory: str

    class Config:
        from_attributes = True