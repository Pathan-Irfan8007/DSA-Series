'''
Q. Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1
'''
# Ans :

def countSegments(s):
    result = s.split()
    return len(result)

def countSegments2(s):
    count = 0
    for i in range(len(s)):
        if(s[i] != " " and (i == 0 or s[i-1] == " ")):
            count += 1
    return count


print(countSegments2("Hello, my name is John"))
print(countSegments2("Hello"))
print(countSegments("                "))
print(countSegments(""))