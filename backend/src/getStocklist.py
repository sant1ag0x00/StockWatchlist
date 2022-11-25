import sqlite3

def getStocklist(symbols: list):
    stocklist = []
    testlist = []
    con = sqlite3.connect("../stock.db")
    cur = con.cursor()
    for symbol in symbols:
        cur.execute(f"SELECT * FROM stocks WHERE Symbol = '{symbol}'")
        rows = cur.fetchall()
        stocklist.append(rows[0])
    for stock in stocklist:
        res_dct = {
            'symbol': stock[0],
            'name'  : stock[1],
            'sector': stock[2],
            'price' : stock[3]
            }
        testlist.append(res_dct)
    return testlist
    con.close()
        
getStocklist(['NVDA','AAPL'])
