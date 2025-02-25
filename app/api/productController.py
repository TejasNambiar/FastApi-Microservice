from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.service.productService import *;
from app.schemas.productDto import ProductCreate, ProductResponse
from app.db.session import get_db

router = APIRouter()

@router.get('/', response_model=list[ProductResponse])
def get_all_products(request: Request):
    db: Session = request.state.db
    return fetch_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_single_product(product_id: int, request: Request):
    db: Session = request.state.db
    product = fetch_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=ProductResponse)
def create_new_product(product: ProductCreate, request: Request):
    db: Session = request.state.db
    return add_product(db, product)

@router.delete("/{product_id}")
def delete_product(product_id: int, request: Request):
    db: Session = request.state.db
    deleted_product = remove_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}