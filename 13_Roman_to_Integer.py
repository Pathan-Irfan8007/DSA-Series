'''
Q. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
 
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
# Ans :

def romanToInt(s):
    parameters = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

    index = len(s) - 1
    result = 0
    while index >= 0:
        current = parameters[s[index]]

        if index > 0:
            previous = parameters[s[index-1]]
            if previous < current:
                current = current - previous
                index -= 1

        result += current
        index -= 1

    return result


def romanToInt2(s):
    parameters = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0

    for i in range(len(s)):
        if i < len(s)-1 and parameters[s[i]] < parameters[s[i+1]]:
            result -= parameters[s[i]]
        else:
            result += parameters[s[i]]

    return result



print(romanToInt2("III"))
print(romanToInt2("LVIII"))
print(romanToInt2("MCMXCIV"))
print(romanToInt2("MMMCDXC"))
print(romanToInt2("XXX"))

        