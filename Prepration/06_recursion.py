def greet(count):
    if(count > 5):
        return
    print(f"{count}. Hello")
    count += 1
    greet(count)

count = 1
# greet(count)

# --- Recurtion using Parameter ---
def func1(i, n):
    if i > n:
        return
    print(f"{i} : {n}")
    func1(i+1, n)
# func1(1, 5)


def func2(n):
    if n == 0:
        return
    print(n)
    func2(n-1)
# func2(5)

def func3(sum, i, n):
    if i > n:
        print(sum)
        return
    func3(sum+i, i+1, n)
# func3(0,1,10)

# def func4(x, n):
#     sum = 0
#     for i in range(x, n+1):
#         sum += i
#     print(sum)
# func4(1, 10)

# --- Functional Recurtion ---
def func5(n):
    if n == 1:
        return 1
    return n + func5(n-1)
print(func5(10))