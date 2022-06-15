from typing import Union

from fastapi import FastAPI

app = FastAPI()

cart = {}


@app.get("/")
def Cart_Application():
    return {"Cloud": "CartApp"}


@app.get("/items/")
async def read_items():
    return cart


@app.post("/item")
async def create_item(item: str,quantity: int,price: int):

	cart[item] = [ "quantidade: {}".format(quantity), "Valor: {}".format(price*quantity)]

@app.delete("/item")
async def remove_item(item: str):
	cart.pop(item)

	return cart
