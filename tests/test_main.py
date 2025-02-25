from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)  # ✅ TestClient acts like Postman

# Test1 GET | get_all_products
def test_get_all_products():
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.json(),list)  # Response should be a list
    
# Test2 | CRUD API's
def test_product_apis():
    new_product = {"name": "Test Product", "price": 50.0}
    # sub-test 1
    response = create(new_product)
    
    id = response.json()["id"]
    # sub-test 2
    getById(id)
    # sub-test 3
    deleteById(id)
    
# t2.POST | create_new_product
def create(new_product):
    response = client.post("/products/", json=new_product)
    assertCommonGet(response)
    
    return response

# t2.GET | get_single_product
def getById(id):
    response = client.get(f"/products/{id}")
    assertCommonGet(response)
    assert response.json()["id"] == id

def assertCommonGet(response):
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
    assert response.json()["price"] == 50.0
    
# t2.DELETE | delete_product
def deleteById(id):
    response = client.delete(f"/products/{id}")
    assert response.status_code == 200
    