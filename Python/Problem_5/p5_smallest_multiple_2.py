#!/usr/bin/python

#Problem
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import operator

def prime_factors(n):
	factors = []
	d = 2
	while n > 1:
        # divides n by d if fully divisible; adds d to the factors list.
		while n % d == 0:
			factors.append(d)
			n /= d
		d += 1
        
		# keep checking while n > 1 and d < sqrt(n)
		if d*d > n and n > 1:
			factors.append(n)
			break
	return factors

def primes(up_to, factorslist):
	for i in range(2, int(math.floor(math.sqrt(up_to)))):
		factorslist = filter(lambda x: x == i or x % i, factorslist)
	return factorslist

# 1-20, but 1 is not prime and 20 is an even number so not prime. So 2 - 19
list1 = primes(20, range(2,20))

for x in range(2, 21):
	if x not in list1:
		temp = prime_factors(x)
		for y in temp:
			while temp.count(y) > list1.count(y):
				list1.append(y)

list1 = reduce(operator.mul, list1, 1)
print list1
