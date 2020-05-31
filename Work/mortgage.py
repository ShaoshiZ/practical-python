# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0
month = 1

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
       
    if principal < payment:
        total_paid = total_paid + principal
        principal = 0
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment

    print(f'Month: {month},\tTotal Paid: ${round(total_paid, 2)},\tPrincipal: ${round(principal, 2)}')
   
    month = month + 1

print(f'Total paid:\t${round(total_paid, 2)}') 
print(f'Months: \t{month - 1}')
