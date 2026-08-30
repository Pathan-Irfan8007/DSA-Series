'''
q. Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
# Ans :

def spiralOrder(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    i, j, k, l = 0, 0, 0, 1

    while True:
        if j < cols:
            result.append(matrix[i][j])
            j += 1
        elif l < rows:
            result.append(matrix[l][j-1])
            l += 1
        else:
            break

    print(result)

# spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

def spiralOrder2(matrix):
    top, left = 0, 0
    bottom, right = len(matrix), len(matrix[0])
    result = []

    while top <= bottom and left <= right:

        # going left to right
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        # going top to bottom
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        # going right to left
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # going bottom to top
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

print(spiralOrder2([[1,2,3],[4,5,6],[7,8,9]]))