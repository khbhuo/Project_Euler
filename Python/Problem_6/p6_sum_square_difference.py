#!/usr/bin/python

up_to = 100
sum_of_square = sum([x**2 for x in range(up_to + 1)])
square_of_sum = (sum(range(up_to + 1)))**2

print square_of_sum - sum_of_square
