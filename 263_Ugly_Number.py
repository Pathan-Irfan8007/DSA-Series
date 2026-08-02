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

    num = n
    if(num < 1):
        return False
    while True:
        if(num % 2 == 0):
            num = num // 2    
        elif(num % 3 == 0):
            num = num // 3
        elif(num % 5 == 0):
            num = num // 5
        elif(num == 1):
            return True
        else:
            return False
        
                
# print(isUgly(6))
# print(isUgly(1))
# print(isUgly(14))

print(isUgly(-15))
# print(isUgly(125))
# print(isUgly(75))
# print(isUgly(50))
