# pcost.py
#
# Exercise 1.27 and Exercise 1.30

import report
import csv
import sys

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    cost = 0
        
    for rowno, row  in enumerate(portfolio, start=1):
        try:
            cost = cost + row['shares'] * row['price']
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

