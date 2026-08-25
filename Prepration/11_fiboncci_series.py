def fibonacciSeries(num):
    a = 0
    b = 1
    for _ in range(num):
        # print(a)
        a,b = b, a+b
    print(a)

fibonacciSeries(9)

def fibonacciSeries2(num):
    if num == 0 or num == 1:
        return num
    return fibonacciSeries2(num-1) + fibonacciSeries2(num-2)

print(fibonacciSeries2(9))