# pcost.py
#
# Exercise 1.27

total_cost = 0

with open('Data/portfolio.csv', 'rt') as file:
    # skip the header
    next(file)

    # loop through the rest of the lines
    for line in file:
        row = line.split(',')
        cost = int(row[1]) * float(row[2])
        total_cost = total_cost + cost

print(f'Total cost {total_cost:0.2f}')
