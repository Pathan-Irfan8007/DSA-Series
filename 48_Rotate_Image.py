'''
Q. You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
# Ans :

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    m, n = 0, 0
    for i in range(cols-1, -1, -1):
        for j in range(rows):
            result[j][i] = matrix[m][n]
            n += 1
        m += 1
        n = 0

    return result

# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))


# ---------- In Place ----------
def rotate2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Matrix Representation
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()
    print("-" * 15)

    for i in range(rows):
        for j in range(i+1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    for i in range(rows):
        for j in range(cols//2):
            matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]

    # Matrix Representation
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()
    
rotate2([[1,2,3],[4,5,6],[7,8,9]])
print("=" * 15)
rotate2([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])