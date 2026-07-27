'''
Q. Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
# Ans :


def sumClosest(nums, target):
    n = len(nums)
    nums.sort()

    closest_sum = nums[0] + nums[1] + nums[2]
    for i in range(n-2):
        left = i+1
        right = n-1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if(abs(current_sum - target) < abs(closest_sum - target)):
                closest_sum = current_sum

            if(current_sum == target):
                return current_sum
            elif(current_sum > target):
                right -= 1
            else:
                left += 1
    return closest_sum

print(sumClosest([-1,2,1,-4], 1))
print(sumClosest([0,0,0], 1))