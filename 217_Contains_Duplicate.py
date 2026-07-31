'''
Q. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
# Ans :

def containsDuplicate(nums):
    freq_dict = {}
    for i in nums:
        if i in freq_dict:
            return True
        else:
            freq_dict[i] = 1
    return False

def containsDuplicate2(nums):
    unique = set()
    print(set(nums))
    for i in nums:
        if i in unique:
            return True
        unique.add(i)
    return False

print(containsDuplicate2([1,2,3,1]))
print(containsDuplicate2([1,2,3,4]))
print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))