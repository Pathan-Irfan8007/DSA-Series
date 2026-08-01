'''
Q. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
# Ans :

def intersection2(nums1, nums2):
    result = []
    if(len(nums1) < len(nums2)):
        min_list = nums1
        max_list = nums2
    else:
        min_list = nums2
        max_list = nums1

    for i in min_list:
        if(i in max_list):
            result.append(i)
            max_list.remove(i)

    return result

def intersection2_2(nums1, nums2):
    freq = {}
    for i in nums1:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    result = []
    for i in nums2:
        if i in freq:
            if freq[i] > 0:
                freq[i] -= 1
                result.append(i)

    return result
            

print(intersection2_2([1,2,2,1], [2,2]))
print(intersection2_2([4,9,5], [9,4,9,8,4]))
print(intersection2_2([3,1,2], [1,1]))
print(intersection2_2([1,2], [1,1]))