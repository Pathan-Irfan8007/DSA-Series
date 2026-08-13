'''
Q. Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
# Ans :

def isSubsequence(s, t):
    i = 0

    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1

    return i == len(s)

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("aaaaaa", "bbaaaa"))
print(isSubsequence("aza", "abzba"))
