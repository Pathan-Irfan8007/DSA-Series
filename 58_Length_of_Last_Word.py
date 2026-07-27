'''
Q. Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''
# Ans :

def lengthOfLastWord(s):
    length = 0
    i = len(s) - 1
    while(i >= 0):
        if(s[i] == " "):
            i -= 1
            continue
        else:
            length += 1
            if(s[i-1] == " "):
                break
        i -= 1

    print(length)
        


lengthOfLastWord("Hello World")
lengthOfLastWord("   fly me   to   the moon  ")
lengthOfLastWord("luffy is still joyboy")