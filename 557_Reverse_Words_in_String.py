'''
Q. Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
'''
# Ans :

def reverseWords(s):
    word_list = s.split(" ")
    print(word_list)
    result1 = []
    result2 = ""
    count = 0
    for word in word_list:
        result1.append(word[::-1])
        count += 1

        i = len(word) - 1
        while(i >= 0):
            result2 += word[i]
            i -= 1
        result2 += " "

    print(" ".join(result1))
    print(result2[:-1])


reverseWords("Let's take LeetCode contest")