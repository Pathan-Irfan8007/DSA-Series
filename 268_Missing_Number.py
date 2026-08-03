'''
Q. Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''
# Ans :

def missingNumbers(nums):
    n = len(nums)
    temp = list(range(0, n+1))
    for i in temp:
        if i not in nums:
            return i

        
def missingNumbers2(nums):      # Best
    n = len(nums)
    expected_sum = (n * (n+1)) // 2
    actual_sum = 0
    for i in nums:
        actual_sum += i
    return expected_sum - actual_sum


def missingNumbers3(nums):
    result = 0
    for i in range(len(nums)+1):
        result ^= i

    for i in nums:
        result ^= i

    return result



print(missingNumbers3([3,0,1]))
print(missingNumbers3([0,1]))
print(missingNumbers3([9,6,4,2,3,5,7,0,1]))

