#!/usr/bin/python

#Problem:
#A palindromic number reads the same both ways. The largest palindrome 
#made from the product of two 2-digit numbers is 9009 = 91 x 99
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(palin):
    isPalin = list(str(palin))
    if isPalin == isPalin[::-1]:
        return True 
    return False

foundPalin = 0
for x in reversed(range(100,1000)):
    for y in reversed(range(100,1000)):
        if isPalindrome( x * y):
            if (x * y) > foundPalin:
                foundPalin = x * y

print foundPalin
