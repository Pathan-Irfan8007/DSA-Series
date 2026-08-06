'''
Q. Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
'''
# Ans :

def findDisappearedNumbers(nums):
    n = len(nums)
    hash_map = [0] * (n+1)

    for i in nums:
        hash_map[i] += 1

    result = []
    for i in range(1, n+1):
        if hash_map[i] == 0:
            result.append(i)

    return result

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))
