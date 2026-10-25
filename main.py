import argparse,sqlite3
from pathlib import Path

def connect(db_path):
    conn=sqlite3.connect(db_path); conn.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, day TEXT NOT NULL, amount REAL NOT NULL CHECK(amount > 0), currency TEXT NOT NULL, category TEXT NOT NULL, note TEXT NOT NULL DEFAULT '')"); return conn

def add_expense(db_path,day,amount,currency,category,note=""):
    if amount<=0: raise ValueError("Amount must be positive")
    currency=currency.upper().strip()
    if len(currency)!=3 or not currency.isalpha(): raise ValueError("Currency must be a 3-letter code")
    conn=connect(db_path)
    try:
        with conn: conn.execute("INSERT INTO expenses(day,amount,currency,category,note) VALUES(?,?,?,?,?)",(day,amount,currency,category,note))
    finally: conn.close()

def totals(db_path):
    conn=connect(db_path)
    try:
        with conn: rows=conn.execute("SELECT currency, ROUND(SUM(amount),2) FROM expenses GROUP BY currency ORDER BY currency").fetchall()
        return dict(rows)
    finally: conn.close()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--db",default="expenses.db"); sub=ap.add_subparsers(dest="cmd",required=True)
    add=sub.add_parser("add"); add.add_argument("--day",required=True); add.add_argument("--amount",type=float,required=True); add.add_argument("--currency",default="USD"); add.add_argument("--category",required=True); add.add_argument("--note",default="")
    sub.add_parser("total"); a=ap.parse_args()
    if a.cmd=="add": add_expense(a.db,a.day,a.amount,a.currency,a.category,a.note); print("Expense saved locally")
    else: print(totals(a.db))
if __name__=="__main__": main()
