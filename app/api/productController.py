from fastapi import APIRouter, HTTPException, Request
from sqlalchemy.orm import Session
from app.service.productService import *  # Import product-related service functions
from app.schemas.productDto import ProductCreate, ProductResponse  # Import data transfer objects (DTOs)

# Create a FastAPI router for handling product-related endpoints
router = APIRouter()

# ✅ GET: Fetch all products
@router.get('/', response_model=list[ProductResponse])
def get_all_products(request: Request):
    """
    Retrieve all products from the database.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        List[ProductResponse]: A list of products in JSON format.
    """
    db: Session = request.state.db  # Retrieve the database session from request
    return fetch_products(db)  # Call service function to fetch all products

# ✅ GET: Fetch a single product by ID
@router.get("/{product_id}", response_model=ProductResponse)
def get_single_product(product_id: int, request: Request):
    """
    Retrieve a single product by its ID.

    Args:
        product_id (int): The unique ID of the product.
        request (Request): The incoming HTTP request object.

    Returns:
        ProductResponse: The product details if found.

    Raises:
        HTTPException: 404 error if the product is not found.
    """
    db: Session = request.state.db  # Retrieve the database session from request
    product = fetch_product_by_id(db, product_id)  # Fetch product from database
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")  # Handle product not found
    return product

# ✅ POST: Create a new product
@router.post("/", response_model=ProductResponse)
def create_new_product(product: ProductCreate, request: Request):
    """
    Create a new product in the database.

    Args:
        product (ProductCreate): The product details received from the request body.
        request (Request): The incoming HTTP request object.

    Returns:
        ProductResponse: The created product with its generated ID.
    """
    db: Session = request.state.db  # Retrieve the database session from request
    return add_product(db, product)  # Call service function to add the product

# ✅ DELETE: Remove a product by ID
@router.delete("/{product_id}")
def delete_product(product_id: int, request: Request):
    """
    Delete a product by its ID.

    Args:
        product_id (int): The unique ID of the product to delete.
        request (Request): The incoming HTTP request object.

    Returns:
        dict: A success message if the product was deleted.

    Raises:
        HTTPException: 404 error if the product is not found.
    """
    db: Session = request.state.db  # Retrieve the database session from request
    deleted_product = remove_product(db, product_id)  # Call service function to delete the product
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")  # Handle product not found
    return {"message": "Product deleted"}  # Return success message
