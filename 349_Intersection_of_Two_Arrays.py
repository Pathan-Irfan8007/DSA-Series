'''
Q. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
# Ans :

def intersection(nums1, nums2):
    result = []
    if(len(nums1) < len(nums2)):
        min_list = set(nums1)
        max_list = set(nums2)
    else:
        min_list = set(nums2)
        max_list = set(nums1)

    for i in min_list:
        if i in max_list:
            result.append(i)

    return result

print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))