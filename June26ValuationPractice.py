#This is a comment.
#This code is going to take some predetermined 'variables' and calculate missing values on the income statement
#This is practice or a template for once we figure out how to webscrape

import time
import decimal
import locale
locale.setlocale(locale.LC_ALL, '')
class color:
    RED = '\033[91m'

print("Hello")
print("Below are the financials for AAPL (in thousands)")
print("-----------------------------------")

#These are the Variables that we would otherwise need to webscrape
#I used the variables from the screenshot on the Inherant Workings document
#From the Summary Quote Page
current_share_price = 184.62
intraday_movement = 2.45
intraday_movement_direction = 1
today_high = 185.03
today_low = 182.54
share_volume = 7046821
ft_week_high = 194.20
ft_week_low = 142.28
market_cap = 907432777560
eps = 10.36
industry = str("Technology")
#From the Income Statement Page
total_revenue = 229234000
cost_of_revenue = 141048000
r_and_d_expense = 11581000
sga_expense = 15261000
other_income = 2745000
#Interest Expense below is actually '0'
interest_expense = 18000000
income_tax = 15738000

#The remaining lines from the Income Statement filled in and Calculated
gross_profit = int(int(total_revenue)-int(cost_of_revenue))
operating_income = int(int(gross_profit) - (int(r_and_d_expense) + int(sga_expense)))
ebit = int(int(operating_income) + int(other_income))
ebt = int(int(ebit) - int(interest_expense))
net_income = int(int(ebt) - int(income_tax))
operating_expense = r_and_d_expense + sga_expense

#Relative Share Price Indicator Formulas
ft_week_high_spread = (1 - (current_share_price / ft_week_high)) * 100
ft_week_low_spread = ((current_share_price / ft_week_low) -1) * 100

o_day_high_spread = (1 - (current_share_price / today_high)) * 100
o_day_low_spread = ((current_share_price / today_low) -1) * 100

#Other calculations and formulas
outstanding_shares = market_cap / current_share_price
pe_ratio = current_share_price / eps

#Revenue And Expenses Calculations
gross_profit_margin = ((total_revenue - cost_of_revenue) / total_revenue) * 100
net_profit_margin = ((gross_profit - operating_expense) / total_revenue) * 100

#Rounding variables that need rounding
ft_week_high_spread_round = round(ft_week_high_spread,2)
ft_week_low_spread_round = round(ft_week_low_spread,2)
o_day_high_spread_round = round(o_day_high_spread,2)
o_day_low_spread_round = round(o_day_low_spread,2)
pe_ratio_round = round(pe_ratio,2)
gross_profit_margin_round = round(gross_profit_margin,2)
net_profit_margin_round = round(net_profit_margin,2)

#Printing Calculated Variables
print("Gross Profit: $" + str(gross_profit))
print("Operating Income: $" + str(operating_income))
print("Earnings Before Interest and Tax: $" + str(ebit))
print("Earnings Before Tax: $" + str(ebt))
print("Net Income: $" + str(net_income))

print("---------------------")
print("The stock is trading " + str(ft_week_high_spread_round) + "% below its 52-Week high")
print("The stock is trading " + str(ft_week_low_spread_round) + "% above its 52-Week low")

print("The stock is trading " + str(o_day_high_spread_round) + "% below its intraday high")
print("The stock is trading " + str(o_day_low_spread_round) + "% above its intraday low")
print("---------------------")

print("AAPL has " + str(outstanding_shares) + " outstanding shares")
print("P/E Ratio: " + str(pe_ratio_round))

print("---------------------")
print("Margin Information")
print("Gross Profit Margin (%): " + str(gross_profit_margin_round))
print("Net Profit Margin (%): " + str(net_profit_margin_round))

#Sscoring system for Gross Profit Margins
if gross_profit_margin < 100 and gross_profit_margin > 90:
    gross_profit_margin_score = 5
if gross_profit_margin < 90 and gross_profit_margin > 80:
    gross_profit_margin_score = 5
if gross_profit_margin < 80 and gross_profit_margin > 70:
    gross_profit_margin_score = 5
if gross_profit_margin < 70 and gross_profit_margin > 60:
    gross_profit_margin_score = 4
if gross_profit_margin < 60 and gross_profit_margin > 50:
    gross_profit_margin_score = 4
if gross_profit_margin < 50 and gross_profit_margin > 40:
    gross_profit_margin_score = 3
if gross_profit_margin < 40 and gross_profit_margin > 30:
    gross_profit_margin_score = 3
if gross_profit_margin < 30 and gross_profit_margin > 20:
    gross_profit_margin_score = 2
if gross_profit_margin < 20 and gross_profit_margin > 10:
    gross_profit_margin_score = 1
if gross_profit_margin < 10 and gross_profit_margin > 00:
    gross_profit_margin_score = 1
else:
    empty_variable = 1

print("The Gross Profit Margin was rated " + str(gross_profit_margin_score) + "/5.")

#Interest Expense Rating System
#AAPL has 0 Interest Expense, so we can play around with it
#Attempt at comparing it to different companies
interest_expense_as_percentage_of_operating_income = (interest_expense / operating_income) * 100
interest_expense_as_percentage_of_operating_income_round = round(interest_expense_as_percentage_of_operating_income,2)

print(" ")
interest_prompt = str(input("Would you like to see Interest Expense Information on this company?"))
print(" ")

if interest_prompt == 'yes':
    print("Interest Expense Information")
    print("Interest Expense as Percentage of Operating Income: " + str(interest_expense_as_percentage_of_operating_income_round) + "%")

    if interest_expense_as_percentage_of_operating_income < 100 and interest_expense_as_percentage_of_operating_income > 90:
        interest_expense_as_percentage_of_operating_income_score = 0
    if interest_expense_as_percentage_of_operating_income < 90 and interest_expense_as_percentage_of_operating_income > 80:
        interest_expense_as_percentage_of_operating_income_score = 0
    if interest_expense_as_percentage_of_operating_income < 80 and interest_expense_as_percentage_of_operating_income > 70:
        interest_expense_as_percentage_of_operating_income_score = 0
    if interest_expense_as_percentage_of_operating_income < 70 and interest_expense_as_percentage_of_operating_income > 60:
        interest_expense_as_percentage_of_operating_income_score = 1
    if interest_expense_as_percentage_of_operating_income < 60 and interest_expense_as_percentage_of_operating_income > 50:
        interest_expense_as_percentage_of_operating_income_score = 1
    if interest_expense_as_percentage_of_operating_income < 50 and interest_expense_as_percentage_of_operating_income > 40:
        interest_expense_as_percentage_of_operating_income_score = 2
    if interest_expense_as_percentage_of_operating_income < 40 and interest_expense_as_percentage_of_operating_income > 30:
        interest_expense_as_percentage_of_operating_income_score = 3
    if interest_expense_as_percentage_of_operating_income < 30 and interest_expense_as_percentage_of_operating_income > 20:
        interest_expense_as_percentage_of_operating_income_score = 4
    if interest_expense_as_percentage_of_operating_income < 20 and interest_expense_as_percentage_of_operating_income > 10:
        interest_expense_as_percentage_of_operating_income_score = 4
    if interest_expense_as_percentage_of_operating_income < 10 and interest_expense_as_percentage_of_operating_income > 0:
        interest_expense_as_percentage_of_operating_income_score = 5
    if interest_expense_as_percentage_of_operating_income == 0:
        interest_expense_as_percentage_of_operating_income_score = 6
    else:
        empty_variable = 1

    if interest_expense_as_percentage_of_operating_income_score == 7:
        print("This company is paying more in Interest Fees than it makes.")
    if interest_expense_as_percentage_of_operating_income_score == 6:
        print("This company operates with no debt.")
    if interest_expense_as_percentage_of_operating_income_score == 5:
        print("This company operates with almost no debt.")
    if interest_expense_as_percentage_of_operating_income_score == 4:
        print("This company operates with a low amount debt.")
    if interest_expense_as_percentage_of_operating_income_score == 3:
        print("This company operates with an average amount of debt.")
    if interest_expense_as_percentage_of_operating_income_score == 2:
        print("This company operates with quite a bit of debt.")
    if interest_expense_as_percentage_of_operating_income_score == 1:
        print("This company operates with a lot debt.")
    if interest_expense_as_percentage_of_operating_income_score == 0:
        print("This company operates with a dangerous amount debt.")
    else:
        empty_variable = 1

else:
    empty_variable = 1


#Attempt at creating a Z-Score using Standard Deviations and a Scoring System 
#Multiple Variables Listed Below using SGA Expenses as an example
#Values listed in Thousands (000s)

#assigning variables
sga_expense_2017 = 15261000
sga_expense_2016 = 14194000
sga_expense_2015 = 14329000
sga_expense_2014 = 11993000
sga_expense_2013 = 10830000

gross_profit_2017 = 88186000
gross_profit_2016 = 84263000
gross_profit_2015 = 93262000
gross_profit_2014 = 70537000
gross_profit_2013 = 64304000

#calculating percentages of each year
sga_expense_as_percentage_of_gross_profit_2017 = ((sga_expense_2017 / gross_profit_2017) * 100)
sga_expense_as_percentage_of_gross_profit_2016 = ((sga_expense_2016 / gross_profit_2016) * 100)
sga_expense_as_percentage_of_gross_profit_2015 = ((sga_expense_2015 / gross_profit_2015) * 100)
sga_expense_as_percentage_of_gross_profit_2014 = ((sga_expense_2014 / gross_profit_2014) * 100)
sga_expense_as_percentage_of_gross_profit_2013 = ((sga_expense_2013 / gross_profit_2013) * 100)

#finding the average of all of them
sga_expense_values_in_percentages = [sga_expense_as_percentage_of_gross_profit_2017, sga_expense_as_percentage_of_gross_profit_2016, sga_expense_as_percentage_of_gross_profit_2015, sga_expense_as_percentage_of_gross_profit_2014, sga_expense_as_percentage_of_gross_profit_2013]
average_sga_expense_percentage_values = sum(sga_expense_values_in_percentages) / len(sga_expense_values_in_percentages)

#subtracting mean from each result and then squaring it
sga_expense_middle_step_2017 = ((sga_expense_as_percentage_of_gross_profit_2017 - average_sga_expense_percentage_values) ** 2)
sga_expense_middle_step_2016 = ((sga_expense_as_percentage_of_gross_profit_2016 - average_sga_expense_percentage_values) ** 2)
sga_expense_middle_step_2015 = ((sga_expense_as_percentage_of_gross_profit_2015 - average_sga_expense_percentage_values) ** 2)
sga_expense_middle_step_2014 = ((sga_expense_as_percentage_of_gross_profit_2014 - average_sga_expense_percentage_values) ** 2)
sga_expense_middle_step_2013 = ((sga_expense_as_percentage_of_gross_profit_2013 - average_sga_expense_percentage_values) ** 2)

#finding the average of the middle step numbers
sga_expense_middle_step_list = [sga_expense_middle_step_2017, sga_expense_middle_step_2016, sga_expense_middle_step_2015, sga_expense_middle_step_2014, sga_expense_middle_step_2013]
average_sga_expense_middle_step = sum(sga_expense_middle_step_list) / len(sga_expense_middle_step_list)

#square rooting the average to get the standard deviation
sga_expense_standard_deviation = (average_sga_expense_middle_step ** (1/2))

#rounding the (SGA expenses as percentges of gross income)
sga_expense_as_percentage_of_gross_profit_2017_round = round(sga_expense_as_percentage_of_gross_profit_2017,2)
sga_expense_as_percentage_of_gross_profit_2016_round = round(sga_expense_as_percentage_of_gross_profit_2016,2)
sga_expense_as_percentage_of_gross_profit_2015_round = round(sga_expense_as_percentage_of_gross_profit_2015,2)
sga_expense_as_percentage_of_gross_profit_2014_round = round(sga_expense_as_percentage_of_gross_profit_2014,2)
sga_expense_as_percentage_of_gross_profit_2013_round = round(sga_expense_as_percentage_of_gross_profit_2013,2)

#prompting SGA EXPENSE information
print(" ")
sga_prompt = str(input("Would you like SGA Expense Information on this company?"))

if sga_prompt == 'yes':
    #printing the SGA Expenses for each year
    print(" ")
    sga_list_prompt = str(input("Would you like to see the SGA expenses for each year?"))
    print(" ")
    if sga_list_prompt == 'yes':
        print ("Sales, General and Admin. Expense Information")
        print("The SGA Expense as Percentage of Gross Income in 2017 is " + str(sga_expense_as_percentage_of_gross_profit_2017_round) + "%.")
        print("The SGA Expense as Percentage of Gross Income in 2016 is " + str(sga_expense_as_percentage_of_gross_profit_2016_round) + "%.")
        print("The SGA Expense as Percentage of Gross Income in 2015 is " + str(sga_expense_as_percentage_of_gross_profit_2015_round) + "%.")
        print("The SGA Expense as Percentage of Gross Income in 2014 is " + str(sga_expense_as_percentage_of_gross_profit_2014_round) + "%.")
        print("The SGA Expense as Percentage of Gross Income in 2013 is " + str(sga_expense_as_percentage_of_gross_profit_2013_round) + "%.")
    else:
        empty_variable = 1
    print(" ")
    sga_expense_standard_deviation_round = round(sga_expense_standard_deviation,2)
    print("The Standard Deviation is " + str(sga_expense_standard_deviation_round) +".")

    #Z-Score Prompt
    sga_expense_z_score_prompt = int(input("For which year would you like the Z-Score of the SGA Expense?"))

    #Z-Score Calculations
    sga_expense_z_score_2017 = ((sga_expense_as_percentage_of_gross_profit_2017 - average_sga_expense_percentage_values) / sga_expense_standard_deviation)
    sga_expense_z_score_2016 = ((sga_expense_as_percentage_of_gross_profit_2016 - average_sga_expense_percentage_values) / sga_expense_standard_deviation)
    sga_expense_z_score_2015 = ((sga_expense_as_percentage_of_gross_profit_2015 - average_sga_expense_percentage_values) / sga_expense_standard_deviation)
    sga_expense_z_score_2014 = ((sga_expense_as_percentage_of_gross_profit_2014 - average_sga_expense_percentage_values) / sga_expense_standard_deviation)
    sga_expense_z_score_2013 = ((sga_expense_as_percentage_of_gross_profit_2013 - average_sga_expense_percentage_values) / sga_expense_standard_deviation)
    #Z-Score Rounding
    sga_expense_z_score_2017_round = round(sga_expense_z_score_2017,2)
    sga_expense_z_score_2016_round = round(sga_expense_z_score_2016,2)
    sga_expense_z_score_2015_round = round(sga_expense_z_score_2015,2)
    sga_expense_z_score_2014_round = round(sga_expense_z_score_2014,2)
    sga_expense_z_score_2013_round = round(sga_expense_z_score_2013,2)


    if sga_expense_z_score_prompt == 2017:
        print("Z-Score: " + str(sga_expense_z_score_2017_round))
    if sga_expense_z_score_prompt == 2016:
        print("Z-Score: " + str(sga_expense_z_score_2016_round))
    if sga_expense_z_score_prompt == 2015:
        print("Z-Score: " + str(sga_expense_z_score_2015_round))
    if sga_expense_z_score_prompt == 2014:
        print("Z-Score: " + str(sga_expense_z_score_2014_round))
    if sga_expense_z_score_prompt == 2013:
        print("Z-Score: " + str(sga_expense_z_score_2013_round))
    else:
        empty_variable = 1
    
    #Making all Z-Scores Positive to find the average
    sga_expense_z_score_2017_positive = abs(sga_expense_z_score_2017)
    sga_expense_z_score_2016_positive = abs(sga_expense_z_score_2016)
    sga_expense_z_score_2015_positive = abs(sga_expense_z_score_2015)
    sga_expense_z_score_2014_positive = abs(sga_expense_z_score_2014)
    sga_expense_z_score_2013_positive = abs(sga_expense_z_score_2013)
    #Finding Average
    sga_expense_z_score_list = [sga_expense_z_score_2017_positive, sga_expense_z_score_2016_positive, sga_expense_z_score_2015_positive, sga_expense_z_score_2014_positive, sga_expense_z_score_2013_positive]
    sga_expense_z_score_average = sum(sga_expense_z_score_list) / len(sga_expense_z_score_list)
    sga_expense_z_score_average_round = round(sga_expense_z_score_average,2)
    print(sga_expense_z_score_average_round)
    
    #Scoring Scale for Average Z-Scores
    if sga_expense_z_score_average < 1000 and sga_expense_z_score_average > 10:
        sga_expense_z_score_average_score = 0
    if sga_expense_z_score_average < 10 and sga_expense_z_score_average > 5:
        sga_expense_z_score_average_score = 1
    if sga_expense_z_score_average < 5 and sga_expense_z_score_average > 4:
        sga_expense_z_score_average_score = 2
    if sga_expense_z_score_average < 4 and sga_expense_z_score_average > 3:
        sga_expense_z_score_average_score = 3
    if sga_expense_z_score_average < 3 and sga_expense_z_score_average > 2.5:
        sga_expense_z_score_average_score = 4
    if sga_expense_z_score_average < 2.5 and sga_expense_z_score_average > 2:
        sga_expense_z_score_average_score = 5
    if sga_expense_z_score_average < 2 and sga_expense_z_score_average > 1.5:
        sga_expense_z_score_average_score = 6
    if sga_expense_z_score_average < 1.5 and sga_expense_z_score_average > 1:
        sga_expense_z_score_average_score = 7
    if sga_expense_z_score_average < 1 and sga_expense_z_score_average > 0.8:
        sga_expense_z_score_average_score = 8
    if sga_expense_z_score_average < 0.8 and sga_expense_z_score_average > 0.5:
        sga_expense_z_score_average_score = 9
    if sga_expense_z_score_average < 0.5 and sga_expense_z_score_average > 0:
        sga_expense_z_score_average_score = 10
    if sga_expense_z_score_average == 0:
        sga_expense_z_score_average_score = 10
    else:
        empty_variable = 1

    #Printing SGA Z-Score Average Score
    print("The SGA Expense was rated " + str(sga_expense_z_score_average_score) + "/10.")
    
    
else:
    empty_variable = 1

print("E N D     O F     P R O G R A M")



