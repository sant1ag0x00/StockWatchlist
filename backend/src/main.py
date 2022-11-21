from updateStock import updateStock
from getSymbols import getSymbols
from getStocklist import getStocklist
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Schluessel": "Wert"}

@app.get("/{name}")
def test(name):
    #Response.headers["Access-Control-Allow-Origin"] = "http://localhost:4000"
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US","Access-Control-Allow-Origin": "http://localhost:4000"}
    return JSONResponse(content=content, headers=headers)

"""
@app.get("/stocklist/{name}")
def getStocks(name: str):
    sym1 = getSymbols(name)
    sym2 = []
    for entry in sym1:
        sym2.append(entry[0])
    updateStock(sym2)
    stocklist = getStocklist(name)
    return {"foo": "bar"}
"""
uvicorn.run(app,host="0.0.0.0",port="8080")
