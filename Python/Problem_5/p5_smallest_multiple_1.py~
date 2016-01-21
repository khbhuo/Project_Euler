#!/usr/bin/python

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
