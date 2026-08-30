'''
Q. Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''
# Ans :

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols)]

    r, c = cols, rows
    for i in range(r):
        for j in range(c):
            result[i][j] = matrix[j][i]

    return result

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1,2,3],[4,5,6]]))