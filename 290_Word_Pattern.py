'''
Q. Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''
# Ans :

def wordPattern(pattern, s):
    hash_map = {}
    reverse_map = {}
    s_list = s.split(" ")

    if len(pattern) != len(s_list):
        return False
    
    for i in range(len(pattern)):
        ch = pattern[i]
        word = s_list[i]

        if ch in hash_map and hash_map[ch] != word:
            return False

        if word in reverse_map and reverse_map[word] != ch:
            return False
        
        hash_map[ch] = word
        reverse_map[word] = ch

    return True 


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))