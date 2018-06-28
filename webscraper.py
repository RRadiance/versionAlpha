#import html-parser
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.nasdaq.com/symbol/amzn' #AMZN is just an example
response = get(url)

# Create parse tree (BeautifulSoup Object)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all(class_= 'column span-1-of-2')

items = []
# itemName = []
# itemValue = []

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
    # items[i] = items[i].encode('ASCII', 'ignore').decode('utf-8')

# Puts data into a dictionary
d = {}
for i in range(0, len(items), 2):
    d[items[i]] = items[i+1].replace(',','')
    


"""
#Seperate name titles from values 
for j in range(len(items)):
    for k in range(len(items[j])):
        lst = items[j]
        itemName.extend(lst[k].find_all('b')) 
        if k%2 != 0:
            itemValue.append(lst[k])

print(itemValue)
"""
