'''
Q. Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
'''
# Ans :

def findMaxConsecutiveOnes(nums):
    flag = False
    count = 0
    result = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            # if count > result:
            #     result = count
            result = max(result, count)
            count = 0

    # if count > result:
        # result = count
    return max(result, count)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,0,1]))
print(findMaxConsecutiveOnes([1,1,0,1,0,1,1,1,1,0,1,1]))
            