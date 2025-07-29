from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI(title="lolmob REST API")

class Item(BaseModel):
    id: str | None = None
    name: str
    description: str | None = None

items: dict[str, Item] = {}

@app.get("/items", response_model=List[Item])
def list_items() -> List[Item]:
    return list(items.values())

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item) -> Item:
    item.id = str(uuid4())
    items[item.id] = item
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
