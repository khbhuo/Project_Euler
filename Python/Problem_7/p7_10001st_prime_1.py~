#!/usr/bin/python

# Problem:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def primes(n):
    composite = set()
    x = 1
    for i in range(2, n+1):
        if i not in composite and x <= 10001:
            yield i
            composite.update(range(i*i, n+1, i))
            x += 1

list1 = list(primes(200000))
print(list1[-1])
