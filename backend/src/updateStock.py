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
        response = requests.request("POST", url, data=f"symbol={symbol}", headers=headers)
        response_dict = response.json()
        print(response_dict)
        #response_string = json.dumps(response_json)
        curPrice = response_dict['data']['currentPrice']
        query = f"UPDATE stocks SET Price = {curPrice} WHERE Symbol = '{symbol}'"
        #print(query)
        print(con)
        cur.execute(query)
        #print(type(response_string))
    con.close()
updateStock(['NVDA',"AAPL"])