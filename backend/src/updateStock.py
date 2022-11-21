import sqlite3
import requests
import json

url = "https://yahoo-finance97.p.rapidapi.com/stock-info"

payload = "symbol=AAPL"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "4399c659eamsh707231ff75492ebp145200jsncbd340cea994",
	"X-RapidAPI-Host": "yahoo-finance97.p.rapidapi.com"
}

def updateStock(stock_symbols: list):
    con = sqlite3.connect("../stock.db")
    cur = con.cursor()
    for symbol in stock_symbols:
        try:
            response = requests.request("POST", url, data=f"symbol={symbol}", headers=headers)
        except Exception:
            return None
        response_dict = response.json()
        curPrice = response_dict['data']['currentPrice']
        query = f"UPDATE stocks SET Price = {curPrice} WHERE Symbol = '{symbol}'"
        cur.execute(query)
        con.commit()
    con.close()