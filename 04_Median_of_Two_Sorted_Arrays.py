'''
Q. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
# Ans :

def findMedianSortedArrays(nums1, nums2):
    result = []
    i,j = 0, 0
    m,n = len(nums1), len(nums2)

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    while i < m:
        result.append(nums1[i])
        i += 1

    while j < n:
        result.append(nums2[j])
        j += 1

    # return result
    n = len(result) // 2

    if len(result) % 2 != 0:
        # print(result[n])
        return result[n]
    else:
        # print(result[n-1], result[n])
        return (result[n-1] + result[n]) / 2

print(findMedianSortedArrays([1,3,5,7,9], [2,4,6,8]))
print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
