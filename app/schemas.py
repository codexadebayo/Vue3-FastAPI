from pydantic import BaseModel

class ItemBase(BaseModel):
    strName: str
    strDescription: str
    intPrice: int
    strImg: str
    intInventory: int
    strCategory: str

class CategoryBase(BaseModel):
    strCategory: str