'''
Q. A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false
'''
# Ans :

def checkPerfectNumber(num):
    fact = []

    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            fact.append(i)
            if num // i not in fact:
                fact.append(num // i)

    result = sum(fact) - num
    return result == num


def checkPerfectNumber2(num):
    if num <= 1:
        return False
    
    total = 1

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i

    return num == total


print(checkPerfectNumber2(28))
print(checkPerfectNumber2(7))
# print(checkPerfectNumber(8128))
# print(checkPerfectNumber(496))
# print(checkPerfectNumber(33550336))