#!usr/bin/python

# Problem 10
#The sum of the primes below 10 is 2+3+5+7=17.
#Find the sum of all the primes below two million.

size = 2000000
list1 = [0] * (size + 1)
list1[0] = 1
list1[1] = 1
for i in range(2, size + 1):
	if list1[i] == 0:
		for j in range(i*i, size + 1, i):
			list1[j] = 1

summation = sum([x for x, y in enumerate(list1) if y == 0])
print summation