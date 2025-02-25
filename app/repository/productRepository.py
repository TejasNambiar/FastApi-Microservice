from sqlalchemy.orm import Session
from app.entity.Product import Product
from app.schemas.productDto import ProductCreate

def get_Products(db: Session):
    return db.query(Product).all();

def get_productById(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first() 

def create_Product(db:Session, product: ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_productById(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product