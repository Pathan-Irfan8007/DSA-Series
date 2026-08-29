def matrixPrint(nums):
    rows = len(nums)
    cols = len(nums[0])

    print("Matrix Representation :")
    for i in range(rows):
        for j in range(cols):
            print(nums[i][j], end=" ")
        print()

    return

nums = [[1,2,3], [4,5,6], [7,8,9]]
matrixPrint(nums)
print("-" * 10)

def upperTriangle(nums):
    rows = len(nums)
    cols = len(nums[0])

    print("Upper Triangular :")
    for i in range(rows):
        for j in range(cols):
            if i <= j:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

    return

upperTriangle(nums)
print("-" * 10)

def lowerTriangle(nums):
    rows = len(nums)
    cols = len(nums[0])

    print("Lower Triangular :")
    for i in range(rows):
        for j in range(cols):
            if i >= j:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

    return

lowerTriangle(nums)
print("-" * 10)

def diagonal(nums):
    rows = len(nums)
    cols = len(nums[0])

    print("Diagonal :")
    for i in range(rows):
        for j in range(cols):
            if i == j:
                print(nums[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

    return 

diagonal(nums)
print("-" * 10)

def transpose(nums):
    rows = len(nums)
    cols = len(nums[0])

    result = [([0] * rows) for _ in range(cols)]
    print("Transpose Matrix :")
    for i in range(rows):
        for j in range(cols):
            result[j][i] = nums[i][j]

    # Changing rows & cols for result matrix
    rows, cols = cols, rows 
    for i in range(rows):
        for j in range(cols):
            print(result[i][j], end=" ")
        print()

transpose(nums)