from bs4 import BeautifulSoup
from requests import get
import re
import time


class Webscraper:

    # Initialize the class
    def __init__(self):
        self.text = ''
        self.lst = []

    # Retrieves data from the NASDAQ Summary Page
    def get_data_nasdaq_summary(self, ticker: str) -> dict:
        start_time = time.time()
        url = 'https://www.nasdaq.com/symbol/'+ ticker
        response = get(url)
        # Create parse tree (BeautifulSoup Object)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all(class_= 'column span-1-of-2')
        #print(len(data))
        #print(type(data))

        items = []
        # Extract table rows
        for i in range(len(data)):
            items.extend(data[i].find_all(class_='table-cell'))

        # Cleans up data
        for i in range(len(items)):
            # get_text strips the HTML tags
            items[i] = items[i].get_text(strip = True).encode\
                ('ASCII', 'ignore').decode('utf-8')
            # Gets rid of the extra ASCII characters, the
            # 'ignore' keyword means any errors in the encoding
            # will leave the character as a ''

        
        # Puts data into a dictionary
        d = {}
        for i in range(0, len(items), 2):
            d[items[i]] = items[i+1].replace(',','')
        print(d)
        
        '''
        # Puts data into a list
        return_lst = []
        for i in range(0, len(items), 2):
            return_lst.append(items[i+1].replace(',',''))
        '''
        
        print('Elapsed time: ' + str(time.time() - start_time))
        return return_lst

    # Retrieves data from NASDAQ Income Statement Page
    def get_data_nasdaq_income_statement(self, ticker: str) -> tuple:
        start_time = time.time()
        url = 'https://www.nasdaq.com/symbol/'+ ticker + \
            '/financials?query=income-statement'
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all(class_= 'genTable') 
        # data is a list of all tags with the name genTable
        # there is only one item in the data list
        # data[0] is a tag object. These objects have MANY methods
        
        '''
        # Attempted to use tag methods to gather data
        new = []
        for child in data[0].descendants:
            new.append(child)
        a = new[11]
        new_new = []
        for item in new:
            if isinstance(item, type(a)):
                if '$' in item.get_text():
                    new_new.append(item)
        for item in new_new:
            pass
        '''
        # text stores the relevant data in the form of a String
        # strip=True gets rid of the extra escape characters in the string (\n, etc)
        text = data[0].get_text(strip=True)
        # year1 stores the income statement data for the most recent year
        year1 = []
        year2 = []
        year3 = []
        year4 = []
        legend = ['Period Ending', 'Total Revenue', 'Gross Profit',\
                  'Research and Development' , 'Sales, General, and Admin,', \
                  'Non-Recurring Items', 'Other operating items', \
                  'Operating income', 'Addtnl income/expense items', \
                  'Earnings before interest and tax', 'Interest Expense', \
                  'Earnings Before Tax', 'Income Tax', 'Minority Interest', \
                  'Equity Earnings/Loss Unconsolidated Subsidiary', \
                  'Net income-cont. operations', 'Net income', \
                  'Net income appplicable to common shareholders']
        print(len(legend))
        
        # Hardcoding method that uses regex, String methods, and index positions
        text = text.replace(',', '')
        # self.text = text
        pattern = re.compile(r'(\d*\d/\d\d/[2]\d\d\d)')
        # This pattern matches all the 
        matches = pattern.findall(text)
        # print(matches)
        print('There is income statement data for ' + str(len(matches)) + \
              ' years')
        if (len(matches) % 4 != 0) or (len(matches) == 0):
            print('Incomplete income statement info. View webscraper.py (years regex)')    
        else:
            # Adds data to the list
            year1.append(matches[0])
            year2.append(matches[1])
            year2.append(matches[2])
            year3.append(matches[3])
        '''
        split_text = text.split()
        period_ending = split_text[8]
        # Gets the period ending for the income statement
        try:
            year1.append(split_text[8][12:21])
            try:
                year2.append(split_text[8][21:30])
                try:
                    year3.append(split_text[8][30:39])
                    try:
                        year4.append(split_text[8][39:48])
                    except NameError:
                        print('The income statement for fourth most recent year DNE')
                        year4.append(-1) #-1 means it does not exist
                except NameError:
                    print('The income statement for the third most recent year DNE')
                    year3.append(-1)
            except NameError:
                    print('The income statement for the second most recent year DNE')
                    year2.append(-1)
        except NameError:
            print('The income statement for the most recent year does not exist')
            year1.append(-1)
        except Exception:
            print('There has been another type of error; investigate in webscraper.py')
        '''
        # Use Regular Expressions to get all dollar values into a list
        pattern = re.compile(r'\$(\d*)') #Keeps text starting with $, followed by digits
        matches = pattern.findall(text) #matches is now a list
        
        # Adds income statement values into appropiate year lists
        # WARNING: THIS ASSUMES THE COMPANY HAS INCOME STATEMENT INFORMATION FOR ALL 4 YEARS
        if (len(matches) % 4 != 0) or (len(matches) == 0):
            print('Incomplete income statement info. View webscraper.py \
            (values regex)')
        else:
            # Adds data to the lists
            counter = 0
            values = len(matches)
            while counter < values:
                year1.append(matches[counter])
                year2.append(matches[counter+1])
                year3.append(matches[counter+2])
                year4.append(matches[counter+3])
                counter += 4
        print('Successfully stored income statement information')
        print(len(year1))
        
        print('Elapsed time: ' + str(time.time() - start_time))
        return_tuple = (year1, year2, year3, year4)
        return return_tuple
        """
        # Unused code, possible alternative method
        
        # Runs if income statement data exists for the most recent year
        if year1[0] != -1:
            pass
            #year1.append(split_text[9][0:0])
        
        # TODO: Append all the data into the yearX lists, use regex?
        total_revenue = split_text[9]
        cost_of_revenue = split_text[11]
        gross_profit = split_text[12]
        
        r_and_d = split_text[15]
        sales_general_admin = split_text[18]
        
        operating_income = split_text[22]
        additional_income_expense_items = split_text[24]
        earnings_before_interest_and_taxt = split_text[28]
        interest_expense = split_text[29]
        earnings_before_tax = split_text[31]
        income_tax = split_text[32]
        
        net_income = split_text[39]
        
        def extract_dollar_values(s: str) -> tuple:
            for char in s:
                pass
        """ 
    
    
