#!/usr/bin/python

#Problem:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

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


pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs)
print largest_prime_factor

