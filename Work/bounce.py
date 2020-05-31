# bounce.py
#
# Exercise 1.5

initial_height = 100

i = 0
while i < 10:
    i = i+1
    height = round(initial_height * 3/5, 4)
    initial_height = height
    print(height)
