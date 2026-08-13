'''
Q. Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
'''
# Ans :

def isPowerOfTwo(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            return False
    return True if (n > 0) else False    # n > 0 also works

print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
print(isPowerOfTwo(0))