'''
Q. Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''
# Ans :

def multiply(num1, num2):
    n1, n2 = 0, 0
    for i in num1:
        temp = ord(i) - 48
        n1 = n1*10 + temp

    for j in num2:
        temp = ord(j) - 48
        n2 = n2*10 + temp

    result = n1*n2
    result_str = []
    while result:
        temp = result % 10
        result //= 10
        result_str.append(chr(temp + 48))

    return "".join(result_str[::-1])

# print(multiply("2", "3"))
# print(multiply("123", "456"))

def multiply2(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    m,n = len(num1), len(num2)
    result = [0] * (m+n)


    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            digit1 = ord(num1[i]) - 48
            digit2 = ord(num2[j]) - 48

            product = digit1 * digit2

            pos2 = i+j+1
            pos1 = i+j

            total = product + result[pos2]

            result[pos2] = total % 10
            result[pos1] += total // 10

    start = 0
    while start < len(result) and result[start] == 0:
        start += 1

    return "".join(map(str, result[start:]))

print(multiply2("2", "3"))
print(multiply2("0", "0"))


