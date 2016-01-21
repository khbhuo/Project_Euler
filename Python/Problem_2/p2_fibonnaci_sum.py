#!/usr/bin/python

#Problem:
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Recursive fibonnaci function which returns the value of the fibonnaci sequence at the index of a given number
def fibonnaci(n):
    if n <= 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n -2)

sum = 0
cnt = 0
 
while True:
    fibNum = fibonnaci(cnt)
    
    # Only add to sum if even number and less than 4 million
    if fibNum <= 4000000 and fibNum % 2 == 0:
        sum += fibNum
    elif fibNum > 4000000:
        break
    cnt += 1
 
print sum
