#!/usr/bin/python

#Problem
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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
    
factorslist = []
for x in range(2,21):
	factorslist.append(prime_factors(x))

factorslist.sort()
print factorslist

