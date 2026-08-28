'''
Q. For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:
Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc". 
'''
# Ans :

def maxRepeating(sequence, word):
    count = 0
    n = len(word)

    for i in range(len(sequence)-1):
        if sequence[i : i+n] == word:
            count += 1

    return count

# print(maxRepeating("ababc", "ab"))
# print(maxRepeating("ababc", "ba"))
# print(maxRepeating("a", "a"))
# print(maxRepeating("aaabaaaabaaab", "aab"))


def maxRepeating2(sequence, word):
    count = 0
    key = word
    while True:
        if word in sequence:
            count += 1
            word += key
        else:
            break 

    return count

print(maxRepeating2("ababc", "ab"))
print(maxRepeating2("ababc", "ba"))
print(maxRepeating2("a", "a"))
print(maxRepeating2("aaabaaaabaaab", "aab"))
        