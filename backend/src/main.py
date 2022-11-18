from updateStock import updateStock
from getSymbols import getSymbols
#from fastapi import FastAPI
#import uvicorn
import sqlite3

#con = sqlite3.connect("../Stock.db")
#cur = con.cursor()

#app = FastAPI()

#@app.get("/")
def read_root():
    return {"Schluessel": "Wert"}

#@app.get("/stocklist/{name}")
def getStocks(name: str):
    sym1 = getSymbols(name)
    sym2 = []
    for entry in sym1:
        sym2.append(entry[0])
    print(sym2)
    updateStock(sym2)
    return None
getStocks('Robert')
#uvicorn.run(app,host="0.0.0.0",port="8080")
