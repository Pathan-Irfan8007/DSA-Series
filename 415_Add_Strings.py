'''
Q. Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
'''
# Ans :

def addStrings(num1, num2):
    i, j = 0, 0
    for ch in num1:
        i = (i * 10 + (ord(ch) - 48))
    for ch in num2:
        j = (j * 10 + (ord(ch) - 48))

    result = i + j
    result_str = ""
    string_map = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

    while result:
        result_str = string_map[result % 10] + result_str
        result //= 10
    return result_str if result_str else "0"


def addStrings2(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        if i >= 0:
            x = ord(num1[i]) - 48
        else:
            x = 0

        if j >= 0:
            y = ord(num2[j]) - 48
        else:
            y = 0

        total = x + y + carry
        digit = total % 10
        carry = total // 10

        result = chr(digit + 48) + result

        i -= 1
        j -= 1

    if carry:
        result = chr(carry + 48) + result 

    return result      


def addStrings3(num1, num2):
    result = []
    carry = 0
    i, j = len(num1)-1, len(num2)-1

    while i >= 0 or j >= 0 or carry:
        digit1 = ord(num1[i]) - 48 if i >= 0 else 0
        digit2 = ord(num2[j]) - 48 if j >= 0 else 0

        total = digit1 + digit2 + carry
        carry = total // 10

        result.append(chr(total % 10 + 48))

        i -= 1
        j -= 1

    return "".join(result[::-1])

print(addStrings3("11", "123"))
print(addStrings3("456", "77"))
print(addStrings3("0", "0"))