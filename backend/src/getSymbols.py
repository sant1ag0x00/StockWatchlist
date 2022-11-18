import sqlite3

def getSymbols(name: str):
    con = sqlite3.connect("../stock.db")
    cur = con.cursor()
    cur.execute(f"SELECT s.Symbol FROM User u INNER JOIN user_stock AS us ON u.id = us.user_id INNER JOIN stocks s on us.stock_symbol = s.Symbol WHERE u.name = '{name}'")
    rows = cur.fetchall()
    con.close()
    return rows

#print(getSymbols('Robert'))