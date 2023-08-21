import time
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Response, status, HTTPException
from .db import engine, get_db
from . import models, response, schemas




app=FastAPI()

models.Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)
    
while True:
    try:
        # Connect to an existing database
        conn = psycopg2.connect(
            host='localhost', dbname='diadem', user='postgres', password='d3spicabl3')
        cur = conn.cursor()
        print("database connection successful")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error :", error)
        time.sleep(2)




@app.get("/", response_model=List[response.Items])
async def home (db: Session = Depends(get_db)):
    home_products = db.query(models.Product).all()
    return home_products

@app.get("/products", response_model=List[response.Items])
async def get_all_products(db: Session = Depends(get_db)):
    products_query = db.query(models.Product).all()
    return products_query

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=response.Items)
async def create_prod(product: schemas.ItemBase, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@app.get("/products/categories/{category}", response_model=List[response.Items])
async def get_products_by_category(category: str, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.strCategory == category).all()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No products found in this category')

    return products

@app.get("/products/categories")
async def get_product_categories(db:Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories


@app.get("/products/categories/{category}", response_model=response.Items)
async def get_all_product_by_category(category:str, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(models.Product.strCategory == category).all()

    if not product_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Page Not Found')
    
    return product_query

# @app.post("/products/categories")
# async def add_product_category(db: Session = Depends(get_db)):


@app.get("/products/searchid/{product_id}", response_model=response.Items)
async def get_product_by_name(product_id:int, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Page Not Found')
    
    return product_query
    