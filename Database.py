import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('stock_info.db')
        self.c = self.conn.cursor()

    #def insertSummaryValues(self):
        #query = 
