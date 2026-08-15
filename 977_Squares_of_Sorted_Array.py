'''
Q. Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
# Ans :

def sortedSquares(nums):
    result = []
    for i in nums:
        result.append(i * i)

    result.sort()
    return result

def sortedSquares2(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    place = len(nums) - 1
    for i in range(len(nums)):
        if abs(nums[left]) > abs(nums[right]):
            result[place] = nums[left] * nums[left]
            place -= 1
            left += 1
        else:
            result[place] = nums[right] * nums[right]
            place -= 1
            right -= 1

    return result


print(sortedSquares2([-4,-1,0,3,10]))
print(sortedSquares2([-7,-3,2,3,11]))