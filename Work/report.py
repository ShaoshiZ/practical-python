# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    'Initialize an empty list'
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)

        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    price = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)        
        
        for row in rows:
            try:
                price[row[0]] = float(row[1])
            except(IndexError):
                pass
    return price

def compute_gain(porfolio, prices):
    'Compute gain, +ve means gain, -ve means loss'
    total_cost = 0.0
    total_value = 0.0

    for s in portfolio:
        total_cost += s['shares'] * s['price']

        total_value += s['shares'] * prices[s['name']]

    gain = total_value - total_cost
    return gain

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
gain = compute_gain(portfolio, prices)

print(f'Gain: {gain:0.2f}')


