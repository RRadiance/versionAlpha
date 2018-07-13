import sqlite3

class Database:

    def __init__(self):
        conn = sqlite3.connect('stock_info.db')
        c = conn.cursor()
