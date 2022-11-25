import sqlite3

def getSymbols(name: str):
    con = sqlite3.connect("../stock.db")
    cur = con.cursor()
    cur.execute(f"SELECT s.Symbol FROM User u INNER JOIN user_stock AS us ON u.id = us.user_id INNER JOIN stocks s on us.stock_symbol = s.Symbol WHERE u.name = '{name}'")
    rows = cur.fetchall()
    con.close()
    sym1 = rows
    sym2 = []
    for entry in sym1:
        sym2.append(entry[0])
    return sym2

#print(getSymbols('Robert'))