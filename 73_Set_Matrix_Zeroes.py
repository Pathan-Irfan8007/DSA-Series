'''
Q. Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
# Ans :

def setZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zeros = []

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for i, j in zeros:
        for k in range(rows):
            for l in range(cols):
                if i == k or l == j:
                    matrix[k][l] = 0
    print("-" * 15)
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

    return

# setZeros([[1,1,1],[1,0,1],[1,1,1]])
# print("=" * 15)
# setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]])


def setZeros2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_row = [0] * rows
    zero_col = [0] * cols

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_row[i] = 1
                zero_col[j] = 1

    for i in range(rows):
        for j in range(cols):
            if zero_row[i] or zero_col[j]:
                matrix[i][j] = 0

    print("-" * 15)
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()

    return

setZeros2([[1,1,1],[1,0,1],[1,1,1]])
print("=" * 15)
setZeros2([[0,1,2,0],[3,4,5,2],[1,3,1,5]])