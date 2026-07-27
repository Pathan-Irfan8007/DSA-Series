'''
Q. Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
# Ans :

# def sumClosest(nums, target):
#     n = len(nums)
#     result = 999
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 print(f"{nums[i]}{nums[j]}{nums[k]}", end=" = ")
#                 sum = nums[i] + nums[j] +nums[k]
#                 print(sum)
#                 diff = max(sum, target) - min(sum, target)
#                 if(diff < result):
#                     result = diff
#                     final_sum = sum
#     print(final_sum)
#     print()


def sumClosest(nums, target):
    n = len(nums)-1
    i = 0
    j = 1
    k = 2
    result = 999999999999999
    
    while True:
        sum = nums[i] + nums[j] +nums[k]
        diff = max(sum, target) - min(sum, target)
        print(f"{nums[i]} {nums[j]} {nums[k]} = {sum}")

        if(diff < result):
            result = diff
            final_sum = sum

        if(i == (n-2)):
            break
        if(k < n):
            k += 1
        elif(k == n and j < (n-1)):
            j += 1
            k = j+1
        elif(k == n and j == (n-1) and i < (n-2)):
            i += 1
            j = i+1
            k = j+1


    print(final_sum , end="\n\n")

sumClosest([0,1,2,3,4], 1)
# sumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
# sumClosest([0,0,0], 1)
