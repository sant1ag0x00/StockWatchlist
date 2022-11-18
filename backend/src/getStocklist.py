import sqlite3

def getStocklist(symbols: list):
    stocklist = []
    con = sqlite3.connect("../stock.db")
    cur = con.cursor()
    for symbol in symbols:
        cur.execute(f"SELECT * FROM stocks WHERE Symbol = '{symbol}'")
        rows = cur.fetchall()
        stocklist.append(rows[0])
    print(stocklist)
    con.close()
        
getStocklist(['NVDA','AAPL'])
