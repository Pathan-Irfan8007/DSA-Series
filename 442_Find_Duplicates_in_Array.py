'''
Q. Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
'''
# Ans :

def findDuplicates(nums):
    nums_set = set()
    result = []

    for num in nums:
        if num in nums_set: 
            result.append(num)
        else:
            nums_set.add(num)

    return result

# print(findDuplicates([4,3,2,7,8,2,3,1]))
# print(findDuplicates([1,1,2]))
# print(findDuplicates([1]))



def findDuplicates2(nums):
    result = []

    for num in nums:
        n = abs(num)
        if nums[n-1] < 0:
            result.append(abs(num))
        else:
            nums[n-1] *= -1

    return result



print(findDuplicates2([4,3,2,7,8,2,3,1]))
print(findDuplicates2([1,1,2]))
print(findDuplicates2([1]))
