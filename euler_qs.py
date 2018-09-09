'''#question (1) sum of squares

k = 0
l = 0
for j in range(1,101):
    k = k+j**2
    l = l+j
print(k)

print(l)
n = l**2
print(n)

print(n-k)
'''

print('-^^^^^^^^^^^^--------')

#question (2)

import numpy

a = numpy.array([[7,53,183,439,863],
        [497,383,563,79,973],
        [287,63,343,169,583],
        [327,343,773,959,943],
        [767,473,103,699,303]])
print(a)
b = a[4][3]
print(b)
c = numpy.sort(a)
print(c)
d = numpy.max(a[0]),max(a[1]),max(a[2]),min(a[3])
print(d)
e = numpy.max(a[0])+max(a[1])+max(a[2])+max(a[3])
print(e)

print('=================')

x = range(25)
x = numpy.reshape(x,(5,5))
print(x)

print('|||||||||||||||||||||||')


#question (3) 10,001 prime number

import sympy
k = sympy.prime(10001)
print(k)
print(sympy.isprime(5))
print(sympy.prime(50))
#I cheated lol.... imported a library in the end coz i got confused

