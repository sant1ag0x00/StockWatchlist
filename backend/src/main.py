from fastapi import FastAPI
import uvicorn
import sqlite3

con = sqlite3.connect("StockWatchlist.db")
cur = con.cursor()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Schluessel": "Wert"}

@app.get("/test")
def test():
  return {"test": "test"}
  
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

uvicorn.run(app,host="0.0.0.0",port="8080")