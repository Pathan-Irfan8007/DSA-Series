'''
Q. Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''
# Ans :

# ----- Kadane’s Algorithm -----

def maximumSubarray(nums):
    maxi = float("-inf")
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        maxi = max(maxi, total)

        if total < 0:
            total = 0

    return maxi

print(maximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maximumSubarray([1]))
print(maximumSubarray([5,4,-1,7,8]))