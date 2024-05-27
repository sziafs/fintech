from pydantic import BaseModel

class Product(BaseModel):
    '''
    id, name, description, price, category
    '''
    id: int
    name: str
    description: str
    price: float
    category: str

