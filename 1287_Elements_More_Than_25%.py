'''
Q. Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
'''
# Ans :

def findSpeialInteger(arr):
    n = len(arr)
    limit = ((n * 25) // 100)
    freq_map = {}

    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
        if freq_map[num] > limit:
            return num

    return -1

# print(findSpeialInteger([1,2,2,6,6,6,6,7,10]))
# print(findSpeialInteger([1,1]))
    

def findSpecialInteger2(arr):
    n = len(arr)
    k = n // 4

    for i in range(n-k):
        if arr[i] == arr[i+k]:
            return arr[i]

print(findSpecialInteger2([1,2,2,6,6,6,6,7,10]))
print(findSpecialInteger2([1,1]))
