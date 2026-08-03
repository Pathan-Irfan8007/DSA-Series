'''
Q. Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
'''
# Ans :

def isPowerOfThree(n):
    num = n
    while num > 3:
        num = num / 3
    if(num == 3 or num == 1):
        return True
    else:
        return False

def isPowerOfThree2(n):
    num = n
    while num > 1:
        if(num % 3 == 0):
            num //= 3
        else:
            return False
    return num == 1 

print(isPowerOfThree2(27))
print(isPowerOfThree2(0))
print(isPowerOfThree2(-1))

# print(isPowerOfThree())
        