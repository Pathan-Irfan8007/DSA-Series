def gcd(m, n):
    while n:
        m,n = n, m%n
    return m

print(gcd(2,5))