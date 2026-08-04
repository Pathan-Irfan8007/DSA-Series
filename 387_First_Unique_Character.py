'''
Q. Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''
# Ans :

def firstUniqChar(s):
    freq_dict = {}

    for ch in s:
        if ch in freq_dict:
            freq_dict[ch] += 1
        else:
            freq_dict[ch] = 1

    result = ""
    for ch in freq_dict:
        if freq_dict[ch] == 1:
            result = ch
            break

    if result:
        return s.index(result)
    else:
        return -1


def firstUniqChar2(s):
    freq_dict = {}

    for ch in s:
        if ch in freq_dict:
            freq_dict[ch] += 1
        else:
            freq_dict[ch] = 1

    for i, ch in enumerate(s):
        if freq_dict[ch] == 1:
            return i
        
    return -1


print(firstUniqChar2("leetcode"))
print(firstUniqChar2("loveleetcode"))
print(firstUniqChar2("aabb"))