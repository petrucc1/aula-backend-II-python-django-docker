from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/')
def hello_world():
    """
    Primeiro endpoint que diz Hello World.
    """
    return {"Hello":"World!"}

@app.get('/{nome}')
def ola(nome: str):
    """
    Escreva o nome e receba a mensagem de Olá com o seu nome.
    """
    if not nome:
        pass
    return {"Olá": nome}

data = [
    Product(id=1, name='Tênis Nike Air Branco', description='Calçado muito bom.', price=599.99),
    Product(id=2, name='Tênis Nike Air Preto', description='Calçado muito bom.', price=599.99),
    Product(id=3, name='Tênis Nike Air Cinza', description='Calçado muito bom.', price=599.99),
]

@app.get('/api/products')
def get_products():
    """
    Endpoint que disponibiliza recursos com todos os produtos.
    """
    return data

@app.get('/api/products/{id}')
def get_products_by_id(id: int):
    """
    Listando um único produto por ID.
    """
    for product in data:
        if product.id == id:
            return product
    return {"message": "Nenhum produto encontrado com o id fornecido."}
