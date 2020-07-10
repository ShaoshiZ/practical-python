#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27 and Exercise 1.30

import stock
import report
import csv
import sys

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfolio_file')
    cost = portfolio_cost(args[1])
    print(f'Total cost: {cost:0.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
