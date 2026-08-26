'''
Q. Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
'''
# Ans :

def titleToNumber(columnTitle):
    result = 0

    for ch in columnTitle:
        current = ord(ch) - 64
        result = result * 26 + current
        
    return result

print(titleToNumber("A"))
print(titleToNumber("AB"))
print(titleToNumber("ZY"))