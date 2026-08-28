'''
Q. You are given an integer array nums consisting of unique integers.
Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.
The smallest and largest integers of the original range are still present in nums.
Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.

Example 1:
Input: nums = [1,4,2,5]
Output: [3]

Example 2:
Input: nums = [7,8,6,9]
Output: []

Example 3:
Input: nums = [5,1]
Output: [2,3,4]
'''
# Ans :

def findMissingElements(nums):
    result = 0
    smallest = float("inf")
    largest = float("-inf")

    for num in nums:
        result ^= num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    for i in range(smallest, largest+1):
        result ^= i

    return [result] if result else []

# print(findMissingElements([1,4,2,5]))
# print(findMissingElements([7,8,6,9]))
# print(findMissingElements([5,1]))


def findMissingElements2(nums):
    nums_dict = {}
    result = []
    smallest = float("inf")
    largest = float("-inf")

    for num in nums:
        nums_dict[num] = 1
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    for i in range(smallest, largest+1):
        if i not in nums_dict:
            result.append(i)

    return result

# print(findMissingElements2([1,4,2,5]))
# print(findMissingElements2([7,8,6,9]))
# print(findMissingElements2([5,1]))


def findMissingElements3(nums):
    nums_set = set(nums)
    smallest = min(nums)
    largest = max(nums)
    result = []

    for i in range(smallest, largest+1):
        if i not in nums_set:
            result.append(i)

    return result

print(findMissingElements3([1,4,2,5]))
print(findMissingElements3([7,8,6,9]))
print(findMissingElements3([5,1]))