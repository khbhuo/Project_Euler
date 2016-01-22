#!/usr/bin/python

def primes(up_to, factorslist):
	while i <= 10001:
		factorslist = filter(lambda x: x == i or x % i, factorslist)
		yield factorslist
