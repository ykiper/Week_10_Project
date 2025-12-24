from data_interactor import create_contact, get_all_contacts, delete_contact
from fastapi import FastAPI
from pydantic import BaseModel
import json

class Item(BaseModel):
    first_name: str
    last_name: str
    phone_number: str



app = FastAPI()

@app.get("/contacts")
def get_contacts():
    return get_all_contacts()


@app.post("/contacts")
def create_contact_API(item: Item):
    return create_contact(item.first_name, item.last_name, item.phone_number)


@app.put("/contacts/{id}")
def update_contact_API(it: int, item: Item)):
    return


@app.delete("/contacts/{id}")
def delete_contact_API(id: int):
    return delete_contact(id)


