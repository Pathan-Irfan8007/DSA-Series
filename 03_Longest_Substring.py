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

# print(longestSubstring("abcabcbb"))
# print(longestSubstring("bbbbb"))
# print(longestSubstring("pwwkew"))
# print(longestSubstring(""))


def longestSubstring2(s):
    seen = set()
    i = 0
    max_len = 0

    for j in range(len(s)):
        while s[j] in seen:
            seen.remove(s[i])
            i += 1

        seen.add(s[j])
        max_len = max(max_len, j - i + 1)

    return max_len


print(longestSubstring2("abcabcbb"))
print(longestSubstring2("bbbbb"))
print(longestSubstring2("pwwkew"))

