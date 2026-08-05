'''
Q. Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6
'''
# Ans :

def maxProduct(nums):
    nums.sort()

    result = float('-inf')
    prod1 = nums[-1] * nums[-2] * nums[-3]
    prod2 = nums[0] * nums[1] * nums[-1]
    return max(prod1, prod2)

def maxProduct2(nums):
    largest = second_largest = third_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in nums:

        # largest three
        if num > largest:
            third_largest = second_largest
            second_largest = largest
            largest = num

        elif num > second_largest:
            third_largest = second_largest
            second_largest = num

        elif num > third_largest:
            third_largest = num

        # smallest two
        if num < smallest:
            second_smallest = smallest
            smallest = num

        elif num < second_smallest:
            second_smallest = num

    return max(
        largest * second_largest * third_largest,
        largest * smallest * second_smallest
    )

print(maxProduct2([-1,-2,1,2,3]))
print(maxProduct2([1,2,3,4]))
print(maxProduct2([-1,-2,-3]))
print(maxProduct2([-100,-98,-1,2,3,4]))
print(maxProduct2([-1,-2,1,2,3]))
    