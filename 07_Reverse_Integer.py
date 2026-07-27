'''
Q. Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''
# Ans :

def reverseInt(x):
    flag = False
    if(x < 0):
        char = "-"
        flag = True

    number = str(x)
    if(flag):
        number = number[1:]

    number = number[::-1]

    
    if(flag):
        result = int(char + number)
    else:
        result = int(number)

    if((result < -(2**31)) or (result > (2**31)-1)):
        return 0
    else:
        return result

print(reverseInt(123))
print(reverseInt(-123))
print(reverseInt(120))
