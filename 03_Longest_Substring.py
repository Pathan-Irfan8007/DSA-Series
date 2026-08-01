'''
Q. Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# Ans :

def longestSubstring(s):
    sub_str = []
    temp = []
    i = 0
    j = 0
    while(i < len(s)):
        if((j < len(s)) and (s[j] not in temp)):
            temp.append(s[j])
            j += 1
        else:
            sub_str.append("".join(temp))
            temp = []
            j = i+1
            i += 1

    result = 0
    for word in sub_str:
        if(len(word) > result):
            result = len(word)
            
    return sub_str, result

print(longestSubstring("abcabcbb"))
print(longestSubstring("bbbbb"))
print(longestSubstring("pwwkew"))
print(longestSubstring(""))


def longestSubstring2(s):
    n = len(s)
    i = 0
    j = 0
    sub_str = []
    temp = ""
    while(i < n):
        if(j < n and s[j] in temp):
            result = s[i:j]
            sub_str.append(result)
            i += 1
            j += 1
            temp = result[i:j]
        else:
            temp += s[j]
            j += 1
    return sub_str


print(longestSubstring2("abcabcbb"))


