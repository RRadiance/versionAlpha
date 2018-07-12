from bs4 import BeautifulSoup
from requests import get

class Webscraper:

    # Initialize the class
    def __init__(self):
        pass

    # Retrieves and cleans the data from the NASDAQ Summary Page
    def get_data_nasdaq_summary(self, ticker: str) -> dict:
        url = 'https://www.nasdaq.com/symbol/'+ ticker
        response = get(url)
        # Create parse tree (BeautifulSoup Object)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all(class_= 'column span-1-of-2')
        
        items = []
        # Extract table rows
        for i in range(len(data)):
            items.extend(data[i].find_all(class_='table-cell'))

        # Cleans up data
        for i in range(len(items)):
            # get_text strips the HTML tags
            items[i] = items[i].get_text(strip = True).encode('ASCII', 'ignore').decode('utf-8')
            # Gets rid of the extra ASCII characters, the
            # 'ignore' keyword means any errors in the encoding
            # will leave the character as a ''

        # Puts data into a dictionary
        d = {}
        for i in range(0, len(items), 2):
            d[items[i]] = items[i+1].replace(',','')

        return d

    # Make a lot more get_data functions

    
