'''
Q. Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

Example 5:
Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.
'''
# Ans :

def myAtoi(s):
    s = s.lstrip()
    index = 0
    flag = False
    result = 0
    if(s == ""):
        return 0
    elif(s[index] == "-"):
        flag = True
        index += 1
    elif(s[index] == "+"):
        index += 1

    for i in range(index, len(s)):
        if s[i].isdigit():
            current = ord(s[i]) - 48
            result = result * 10 + current
            
        else:
            break
    if flag:
        result = -result
    if result > 2147483647:
        return 2147483647
    elif result < -2147483648:
        return -2147483648
    return result


def myAtoi2(s):
    s = s.lstrip()

    if not s:
        return 0

    index = 0
    sign = 1
    if s[index] == "-":
        sign = -1
        index += 1
    elif s[index] == "+":
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
        digit = ord(s[index]) - ord("0")
        result = result * 10 + digit
        index += 1
        
    result = result * sign

    if result > 2147483647:
        return 2147483647
    elif result < -2147483648:
        return -2147483648
    return result


print(myAtoi2("42"))
print(myAtoi2(" -042"))
print(myAtoi2("1337c0d3"))
print(myAtoi2("0-1"))
print(myAtoi2("words and 987"))