'''
Q. Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
'''
# Ans :

def addDigits(num):
    result = num
    while result > 9:
        num = result
        result = 0
        while num:
            current_digit = num % 10
            result += current_digit
            num = num // 10
    return result

def addDigits2(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9

print(addDigits2(123))
print(addDigits2(0))
