
def greet(count):
    if(count > 5):
        return
    print(f"{count}. Hello")
    count += 1
    greet(count)

count = 1
greet(count)