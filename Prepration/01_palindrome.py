def isPalindrome(num):
    temp = num
    x = 0
    result = 0
    while(num > 0):
        x = (num % 10)
        num = num // 10
        result = result*10 + x
    print(temp == result)

isPalindrome(12321)