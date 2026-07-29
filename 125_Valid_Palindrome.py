'''
Q. A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
# Ans :

def validPalindrome(s):
    # if(len(s) <= 1):
    #     return True

    # alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    # result = ""
    # for char in s:
    #     if char.lower() in alpha:
    #         result = result + char.lower()
    result = "".join(filter(str.isalnum, s)).lower()

    return (result[:] == result[::-1])


print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))
print(validPalindrome(" "))
print(validPalindrome("0p"))