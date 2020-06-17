#!/usr/bin/env python3
# report.py
#
# Exercise 2.4

import tableformat
import stock
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    with open(filename) as lines:
        portfolio_dict = parse_csv(lines,select=['name','shares','price'], types=[str,int,float])

    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portfolio_dict]
    return portfolio


def read_prices(filename):
    with open(filename) as lines:
        pricelist = parse_csv(lines, types=[str,float], has_headers=False)    
    price = dict(pricelist)
    
    return price

def compute_gain(porfolio, prices):
    'Compute gain, +ve means gain, -ve means loss'
    total_cost = 0.0
    total_value = 0.0

    for s in portfolio:
        total_cost += s.shares * s.price

        total_value += s.shares * prices[s.name]

    gain = total_value - total_cost
    return gain

def make_report(portfolio, prices, formatter):
    report = []

    'Print a header'
    headers = ('Name', 'Shares', 'Price', 'Change')
    formatter.headings(headers)
   
    for s in portfolio:
        change = prices[s.name] - s.price
        report.append((s.name, s.shares, prices[s.name], change))

    for name, shares, price, change in report:
        price = '$' + str(round(price, 2))
        rowdata = [ name, str(shares), price, f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfolio_file, price_file, fmt='txt'):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)

    # initialize a TableFormatter class instance
    formatter = tableformat.create_formatter(fmt)
    report = make_report(portfolio, prices, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfolio_file price_file format')
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
