#!usr/bin/python

# Problem 10
#The sum of the primes below 10 is 2+3+5+7=17.
#Find the sum of all the primes below two million.

from math import sqrt

def primes(size):
	composites = set()
	for i in range(2, size + 1):
		if i not in composites:
			yield i
			composites.update(range(i*i, size + 1, i))

summation = sum(list(primes(2000000)))
print summation