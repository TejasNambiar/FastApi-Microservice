from sqlalchemy.orm import Session
from app.repository.productRepository import get_productById, get_Products, create_Product, delete_productById
from app.schemas.productDto import ProductCreate

def fetch_products(db: Session):
    return get_Products(db)

def fetch_product_by_id(db: Session, product_id: int):
    return get_productById(db, product_id)

def add_product(db: Session, product: ProductCreate):
    return create_Product(db, product)

def remove_product(db: Session, product_id: int):
    return delete_productById(db, product_id)