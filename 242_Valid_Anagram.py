'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
# Ans :

def validAnagram(s, t):
    freq_dict = {}
    if(len(s) != len(t)):
        return False
    for i in s:
        if(i in freq_dict):
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    for i in t:
        if(i not in freq_dict):
            return False
        elif(freq_dict[i] <= 0):
            return False
        else:
            freq_dict[i] -= 1

    return True

print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "car"))
print(validAnagram("rra", "ara"))
