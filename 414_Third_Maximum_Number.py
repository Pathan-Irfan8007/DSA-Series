'''
Q. Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''
# Ans :

def thirdMax(nums):
    nums.sort()
    result = nums[::-1]
    result = list(dict.fromkeys(result))
    
    return result[0] if len(result) < 3 else result[2]


def thirdMax2(nums):
    first_max = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')

    for num in nums:
        if num == third_max or num == second_max or num == first_max:
            continue

        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num

        elif num > second_max:
            third_max = second_max
            second_max = num

        elif num > third_max:
            third_max = num
 
    return first_max if third_max == float('-inf') else third_max

print(thirdMax2([3,2,1]))
print(thirdMax2([1,2]))
print(thirdMax2([2,2,3,1]))
print(thirdMax2([2,2,3,1,4,5,6,4,5,6]))