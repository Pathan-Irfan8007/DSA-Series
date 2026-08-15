'''
Q. Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
# Ans :

def majorityElement(nums):
    freq_map = {}

    for i in nums:
        freq_map[i] = freq_map.get(i, 0) + 1
        # if i in freq_map:
        #     freq_map[i] += 1
        # else:
        #     freq_map[i] = 1

    for i in freq_map:
        if freq_map[i] > (len(nums) // 2):
            return i

# Boyer–Moore Voting Algorithm
def majorityElement2(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate


print(majorityElement2([3,2,3]))
print(majorityElement2([2,2,1,1,1,2,2]))