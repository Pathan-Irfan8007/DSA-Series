'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
'''
# Ans :

def detectCapitalUse(word):
    case1 = True 
    case2 = True 
    case3 = True

    # case1 = USA
    for ch in word:
        if ord(ch) >= 97:
            case1 = False
            # print("case1")
            break

    # case2 = leetcode
    for ch in word:
        if ord(ch) < 97:
            case2 = False
            # print("case2")
            break

    # case3 = Google
    if ord(word[0]) >= 97:
        case3 = False
    else:
        for ch in word[1:]:
            if ord(ch) < 97:
                case3 = False
                break
    

    if (case1 or case2 or case3):
        return True
    else:
        return False


def detectCapitalUse2(word):
    if word.islower() or word.isupper() or word.istitle():
        return True
    else:
        return False

    
print(detectCapitalUse("USA"))
print(detectCapitalUse("leetcode"))
print(detectCapitalUse("Google"))
print(detectCapitalUse("FlaG"))
