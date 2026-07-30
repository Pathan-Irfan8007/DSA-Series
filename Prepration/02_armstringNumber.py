def armstrongNumber(n):
    num = n
    result = 0
    l = len(str(n))
    while(num > 0):
        x = (num % 10)
        num = num // 10
        result += (x**l)
    return result == n

print(armstrongNumber(153))
print(armstrongNumber(1634))