#import html-parser
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.nasdaq.com/symbol/amzn' #AMZN is just an example
response = get(url)

#Create parse tree (BeautifulSoup Object)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all(class_= 'column span-1-of-2')

items = []
itemName = []
itemValue = []

#Extract table rows
for i in range(len(data)):
    items.append(data[i].find_all(class_='table-cell'))

#Seperate name titles from values 
for j in range(len(items)):
    for k in range(len(items[j])):
        lst = items[j]
        itemName.append(lst[k].find_all('b')) 
        if k%2 != 0:
            itemValue.append(lst[k])

print(itemValue)
