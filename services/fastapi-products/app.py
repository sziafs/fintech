from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get("/")
def read_root():
    '''
    Root endpoint
    Returns a simple hello world message
    '''
    return {"Hello": "World"}

@app.get("/{name}")
def read_name(name: str):
    return {"hello": name}

data = [Product(id=1, name="Product 1", description="Description 1", price=100.0, category="Category 1"),
        Product(id=2, name="Product 2", description="Description 2", price=200.0, category="Category 2"),
        Product(id=3, name="Product 3", description="Description 3", price=300.0, category="Category 3")]

@app.get("/api/products")
def read_products():
    return data

@app.get("/api/products/{product_id}")
def read_product(product_id: int):
    if product_id < 1 or product_id > len(data):
        return {"error": "Product not found"}
    return data[product_id-1]