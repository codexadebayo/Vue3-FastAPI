import time
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, HTTPException
from .db import engine, get_db
from . import models, response, schemas
from .config import User

setting = User() #login database with user details

app=FastAPI() #create API key

models.Base.metadata.create_all(bind=engine) #access tables in DB


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],

    # allow_origins=["http://localhost:3000"],
)
#CORS to allow access from clients


while True:
    try:
        # Connect to an existing database
        conn = psycopg2.connect(
            host=setting.DATABASE_HOSTNAME, dbname=setting.DATABASE_NAME, user=setting.DATABASE_USERNAME, password=setting.DATABASE_PASSWORD)
        cur = conn.cursor()
        print("database connection successful")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error :", error)
        time.sleep(2)

        #DB handshake 


@app.get("/", response_model=List[response.Items])
async def get_home_rand (db: Session=Depends(get_db)):
    query_home = db.query(models.Product).order_by(func.random())
    random_products = query_home.limit(10).all()
    
    return random_products


@app.get("/products", response_model=List[response.Items])
async def get_all_products(db: Session = Depends(get_db), limit:Optional[int]= None, search:Optional[ str]="None"):#route parameters allows clients search, and limit response data.
    products_query = db.query(models.Product).filter(models.Product.strDescription.contains(search)).limit(limit) 
    return products_query

@app.get("/products/{strName}", response_model=List[response.Items])
async def get_product( strName:str, db: Session = Depends(get_db)):
    products_query = db.query(models.Product).filter(models.Product.strName == strName).first()
    return {products_query}

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=response.Items)
async def create_prod(product: schemas.ItemBase, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@app.get("/products/categories")
async def get_product_categories(db:Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return categories

@app.get("/products/categories/{category}", response_model=List[response.Items])
async def get_products_by_category(category: str, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.strCategory == category).all()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No products found in this category')

    return products


@app.get("/products/searchid/{product_id}", response_model=response.Items)
async def get_product_by_name(product_id:int, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Page Not Found')
    
    return product_query