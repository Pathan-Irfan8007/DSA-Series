'''
Q. An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 x 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
'''
# Ans :

def isUgly(n):
    fact = []
    temp = [2,3,5]
    for i in range(1, int(n**0.5)+1):
        if(n % i == 0):
            fact.append(i)
            if(n//i not in fact):
                fact.append(n//i)

    fact.sort()
    return fact
                
print(isUgly(6))
print(isUgly(14))