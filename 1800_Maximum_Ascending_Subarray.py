'''
Q. Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
'''
# Ans :

def maxAscendingSum(nums):
    maxi = float("-inf")
    total = 0

    for i in range(len(nums)):
        if i > 0 and nums[i] <= nums[i-1]:
            maxi = max(maxi, total)
            total = 0
        total += nums[i]
    maxi = max(maxi, total)

    return maxi

print(maxAscendingSum([10,20,30,5,10,50]))
print(maxAscendingSum([10,20,30,40,50]))
print(maxAscendingSum([12,17,15,13,10,11,12]))
print(maxAscendingSum([3,6,10,1,8,9,9,8,9]))