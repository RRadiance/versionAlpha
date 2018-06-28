#This is a comment.
#This code is going to take some predetermined 'variables' and calculate missing values on the income statement
#This is practice or a template for once we figure out how to webscrape

import time
import decimal
import locale
locale.setlocale(locale.LC_ALL, '')

print("Hello")
print("Below are the financials for AAPL (in thousands)")
print("-----------------------------------")

#These are the Variables that we would otherwise need to webscrape
#I used the variables from the screenshot on the Inherant Workings document
#From the Summary Quote Page
currentshareprice = 184.62
idmovement = 2.45
idmovementdirection = 1
todayhigh = 185.03
todaylow = 182.54
sharevolume = 7046821
ftweekhigh = 194.20
ftweeklow = 142.28
marketcap = 907432777560
eps = 10.36
industry = str("Technology")
#From the Income Statement Page
totalrevenue = 229234000
costofrevenue = 141048000
randdexp = 11581000
sgaexp = 15261000
otherincome = 2745000
interestexp = 0
incometax = 15738000

#The remaining lines from the Income Statement filled in and Calculated
grossprofit = int(int(totalrevenue)-int(costofrevenue))
operatingincome = int(int(grossprofit) - (int(randdexp) + int(sgaexp)))
ebit = int(int(operatingincome) + int(otherincome))
ebt = int(int(ebit) - int(interestexp))
netincome = int(int(ebt) - int(incometax))
operatingexp = randdexp + sgaexp

#Relative Share Price Indicator Formulas
ftweekhighspread = (1 - (currentshareprice / ftweekhigh)) * 100
ftweeklowspread = ((currentshareprice / ftweeklow) -1) * 100

odayhighspread = (1 - (currentshareprice / todayhigh)) * 100
odaylowspread = ((currentshareprice / todaylow) -1) * 100

#Other calculations and formulas
outstandingshares = marketcap / currentshareprice
peratio = currentshareprice / eps

#Revenue And Expenses Calculations
grossprofitmargin = ((totalrevenue - costofrevenue) / totalrevenue) * 100
netprofitmargin = ((grossprofit - operatingexp) / totalrevenue) * 100

#Rounding variables that need rounding
ftweekhighspreadround = round(ftweekhighspread,2)
ftweeklowspreadround = round(ftweeklowspread,2)
odayhighspreadround = round(odayhighspread,2)
odaylowspreadround = round(odaylowspread,2)
peratioround = round(peratio,2)
grossprofitmarginround = round(grossprofitmargin,2)
netprofitmarginround = round(netprofitmargin,2)

#Printing Calculated Variables
print("Gross Profit: $" + str(grossprofit))
print("Operating Income: $" + str(operatingincome))
print("Earnings Before Interest and Tax: $" + str(ebit))
print("Earnings Before Tax: $" + str(ebt))
print("Net Income: $" + str(netincome))

print("---------------------")
print("The stock is trading " + str(ftweekhighspreadround) + "% below its 52-Week high")
print("The stock is trading " + str(ftweeklowspreadround) + "% above its 52-Week low")

print("The stock is trading " + str(odayhighspreadround) + "% below its intraday high")
print("The stock is trading " + str(odaylowspreadround) + "% above its intraday low")
print("---------------------")

print("AAPL has " + str(outstandingshares) + " outstanding shares")
print("P/E Ratio: " + str(peratioround))

print("Gross Profit Margin (%): " + str(grossprofitmarginround))
print("Net Profit Margin (%): " + str(netprofitmarginround))

#Attempt at creating a scoring system for Gross Profit Margins
if grossprofitmargin < 100 and grossprofitmargin > 90:
    grossprofitmarginscore = 5
if grossprofitmargin < 90 and grossprofitmargin > 80:
    grossprofitmarginscore = 5
if grossprofitmargin < 80 and grossprofitmargin > 70:
    grossprofitmarginscore = 5
if grossprofitmargin < 70 and grossprofitmargin > 60:
    grossprofitmarginscore = 4
if grossprofitmargin < 60 and grossprofitmargin > 50:
    grossprofitmarginscore = 4
if grossprofitmargin < 50 and grossprofitmargin > 40:
    grossprofitmarginscore = 3
if grossprofitmargin < 40 and grossprofitmargin > 30:
    grossprofitmarginscore = 3
if grossprofitmargin < 30 and grossprofitmargin > 20:
    grossprofitmarginscore = 2
if grossprofitmargin < 20 and grossprofitmargin > 10:
    grossprofitmarginscore = 1
if grossprofitmargin < 10 and grossprofitmargin > 00:
    grossprofitmarginscore = 1
else:
    print(" ")

print("The Gross Profit Margin was rated " + str(grossprofitmarginscore) + "/5.")





