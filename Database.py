import sqlite3



def create_connection(db_file):
    #Create a database connection to the SQLite database specified by the file.

    #Argument: db file (stock_info.db)
    #Return: Connection Object or none

    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

    return None


def newSummaryValues(conn, values):
    #Inserts values into summary table

    #Arguments: connection object, values to be inserted
    #Return: generated row id

    query = """INSERT INTO summaryValues(Symbol, Best Bid/Ask,
            1 Year Target, Today's High/Low, Share Volume,
            50 Day Avg. Daily Volume, Previous Close,
            52 Week High/Low, Market Cap, P/E Ratio,
            Forward P/E (1y), Earnings Per Share,
            Annualized Dividend, Ex Dividend Date,
            Dividend Payment Date, Current Yield (%),
            Beta) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

    c = conn.cursor()
    c.execute(query, values)

    return c.lastrowid

def main():
    database = 'stock_info.db'

    #create database connection
    conn = create_connection(database)
    with conn:
        #values to be inserted
        values = ['AAPL', 'NA/NA', '210', '223.49/219.41', '27254804',
                  '24041860', '219.70', '220.54/149.16', '1076976899480',
                  '20.22', '18.81', '11.03', '2.92', '8/10/2018', '8/16/2018',
                  '1.34 %', '1.02']
        summary = newSummaryValues(conn, values)
                      
