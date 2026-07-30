'''
Q. Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.

Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
'''
# Ans :

def commonFactors(a, b):
    count = 0
    fact1 = []
    fact2 = []
    for i in range(1, int(a**0.5)+1):
        if(a % i == 0):
            fact1.append(i)
            if(a//i != i):
                fact1.append(a//i)

    for i in range(1, int(b**0.5)+1):
        if(b % i == 0):
            fact2.append(i)
            if(b//i != i):
                fact2.append(b//i)
    if(len(fact1) > len(fact2)):
        maximum = fact1
        minimum = fact2
    else:
        maximum = fact2
        minimum = fact1

    for i in minimum:
        if i in maximum:
            count += 1
    print(count)


def commonFactors2(a, b):
    while b:
        a,b = b, a % b
    count = 0

    for i in range(1, int(a**0.5)+1):
        if(a % i == 0):
            count += 1
            if(a//i != i):
                count += 1

    print(count)
             

commonFactors2(12, 6)
commonFactors2(25, 30)