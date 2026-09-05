'''
Q. Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
'''
# Ans :

def isValid(s):
    pairs = {")" : "(", 
             "]" : "[",
             "}" : "{"}
    stack = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or pairs[ch] != stack[-1]:
            return False
        else:
            stack.pop()
            
    return not stack

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))