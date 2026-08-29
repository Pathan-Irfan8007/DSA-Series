'''
Q. You are given an integer array nums.
You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:
All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

Example 1:
Input: nums = [1,2,3,4,5]
Output: 15

Example 2:
Input: nums = [1,1,0,1,1]
Output: 1

Example 3:
Input: nums = [1,2,-1,-2,1,0,-1]
Output: 3
'''
# Ans :

def maxSum(nums):
    nums_set = set(nums)
    positive_max = 0
    negative_max = float("-inf")

    for num in nums_set:
        if num > 0:
            positive_max += num
        else:
            negative_max = max(negative_max, num)

    return positive_max if positive_max else negative_max

print(maxSum([1,2,3,4,5]))
print(maxSum([1,1,0,1,1]))
print(maxSum([1,2,-1,-2,1,0,-1]))