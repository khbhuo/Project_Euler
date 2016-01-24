#!/usr/bin/python

def pyTriplet(m, n, sum):
    a = (n*n) - (m*m)
    b = 2*n*m
    c = (n*n) + (m*m)
    
    if sum:
        return a + b + c
    else:
        return a*b*c
        
n = 2
cont = True

while cont:
    for m in range(1, n):
        if pyTriplet(m, n, True) == 1000:
            print 'm value: ', m, '\nn value: ', n
            print pyTriplet(m, n, False)
            cont = False
            break
    n += 1
 
#answer: 31875000