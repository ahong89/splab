from typing import Union

from fastapi import FastAPI, status

from . import data
from . import models

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tabs/create", status_code=status.HTTP_201_CREATED)
def create_tab(total: models.Total):
    db = data.SplabDB()
    tab_id = db.create_tab(total.total)
    return {"tab_id": tab_id}

@app.get("/tabs/paid/{tab_id}", status_code=status.HTTP_200_OK)
def get_tab_paid(tab_id: int):
    db = data.SplabDB()
    tab_total, tab_paid = db.get_tab_paid(tab_id)
    return {"tab_total": tab_total, "tab_paid": tab_paid}

@app.post("/users/create", status_code=status.HTTP_201_CREATED)
def create_user():
    db = data.SplabDB()
    user_id = db.create_user()
    return {"user_id": user_id}

@app.post("/items/create", status_code=status.HTTP_201_CREATED)
def create_item_add_to_tab(request: models.CreateItemRequest):
    db = data.SplabDB()
    item_id = db.create_item_add_to_tab(request.tab_id, request.item_total)
    return {"item_id": item_id}

@app.post("/items/add_user", status_code=status.HTTP_201_CREATED)
def add_user_to_item(user_to_item: models.UserToItem):
    db = data.SplabDB()
    user_item_id = db.add_user_to_item(
        user_to_item.item_id,
        user_to_item.user_id,
        user_to_item.portion)

@app.post("/users/pay", status_code=status.HTTP_200_OK)
def user_pay(request: models.UserPayRequest):
    db = data.SplabDB()
    db.user_pay(request.user_id)
