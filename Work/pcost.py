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
        next(lines)

        # loop through the rest of the lines
        
        for line in lines:
            try:
                share_cost = int(line[1]) * float(line[2])
                cost = cost + share_cost
            except ValueError:
                print('[Warninig] Missing Value!')

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:0.2f}')
