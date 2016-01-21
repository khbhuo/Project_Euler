#!/usr/bin/python

#Problem
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Thought process: Through preliminary google searches, the LCM can be found by the following:
#LCM = (product of values)/GCD(Values)
#GCD (greatest common multiple) is found using a modified version of the original Euclidean Algorithm.

def find_gcd(a,b):
	z = 0
	while a > 0 and b >0:
		if a >= b:
			z = b
			a %= b
		else:
			z = a
			b %= a
	return z

gcd = 2
for x in range(2,20):
	gcd = find_gcd(gcd, x+1)
print gcd

r = 1
for x in range(1,21):
	r *= x

print r/gcd
