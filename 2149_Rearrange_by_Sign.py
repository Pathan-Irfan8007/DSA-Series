'''
Q. You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
'''
# Ans :

def rearrangeArray(nums):
    result = [0] * len(nums)
    positive = 0
    negative = 1

    index = 0

    while index < len(nums):
        if nums[index] > 0:
            result[positive] = nums[index]
            positive += 2
        else:
            result[negative] = nums[index]
            negative += 2
        index += 1

    return result

print(rearrangeArray([3,1,-2,-5,2,-4]))
print(rearrangeArray([-1,1]))

            
        