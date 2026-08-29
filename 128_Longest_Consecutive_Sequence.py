'''
Q. Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
'''
# Ans :

def longestConsecutive(nums):
    nums.sort()
    longest = 0

    length = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i]-1 == nums[i-1]:
            length += 1
        else:
            longest = max(longest, length)
            length = 0
    longest = max(longest, length)
    return longest+1

# print(longestConsecutive([100,4,200,1,3,2]))
# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(longestConsecutive([1,0,1,2]))

# ------ Optimal ------
def longestConsecutive2(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num-1 not in nums_set:
            x = num
            count = 1
            while x+1 in nums_set:
                count += 1
                x += 1
            longest = max(longest, count)

    return longest

print(longestConsecutive2([100,4,200,1,3,2]))
print(longestConsecutive2([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive2([1,0,1,2]))