from webscraper import Webscraper
#from finance_calculations import Basic_Calculations

if __name__ == '__main__':

    # Eventually this code will be moved somewhere else, probably model.py
    webscraper = Webscraper()
    ticker = input("Type the stock ticker: ")
    d = webscraper.get_data_nasdaq_summary(ticker)
