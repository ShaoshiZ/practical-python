# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    'Initialize an empty list'
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = dict(zip(headers, row))
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
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

def make_report(portfolio, prices):
    report = []

    'Print a header'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-'*10 + ' ') * len(headers)) 
   
    for s in portfolio:
        change = prices[s['name']] - s['price']
        report.append((s['name'], s['shares'], prices[s['name']], change))

    for name, shares, price, change in report:
        price = '$' + str(round(price, 2))
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


    return report
