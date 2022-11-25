from updateStock import updateStock
from getSymbols import getSymbols
from getStocklist import getStocklist
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Schluessel": "Wert"}

@app.get("/stocklist/{name}")
def getStocks(name: str):
    sym = getSymbols(name)
    updateStock(sym)
    stocklist = getStocklist(sym)
    content = {'data': stock for stock in stocklist}
    print(content)
    return content

#getStocks("Robert")
uvicorn.run(app,host="0.0.0.0",port="8080")
