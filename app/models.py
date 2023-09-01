from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base
    
class Category(Base):
    __tablename__ = "categories"
    strCategory = Column(String, primary_key=True, index=True)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    strName = Column(String, nullable=False)
    strDescription = Column(String, nullable=False, unique=True)
    strImg = Column(String, nullable=False, unique=True)
    intPrice = Column(Integer, nullable= False)
    intInventory = Column(Integer)
    strCategory = Column(String, nullable=False)
    onSale = Column(Boolean, server_default='False')
    strCategory = Column(String, ForeignKey("categories.strCategory"))

    category = relationship("Category", back_populates="products")
    
