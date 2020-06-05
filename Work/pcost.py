# pcost.py
#
# Exercise 1.27 and Exercise 1.30

import csv
import sys

def portfolio_cost(filename):
    cost = 0

    with open(filename, 'rt') as file:
        lines = csv.reader(file)
        # skip the header
        headers = next(lines)

        # loop through the rest of the lines
        
        for lineno, line in enumerate(lines, start=1):
            record = dict(zip(headers, line))
            try:
                share_cost = int(record['shares']) * float(record['price'])
                cost = cost + share_cost
            except ValueError:
                print(f'Row {lineno}: Bad row: {line}')

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:0.2f}')
