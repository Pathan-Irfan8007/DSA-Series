def reverseArray(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    print(nums)
# reverseArray([0,1,2,3,4,5,6])


def reverseArray2(nums, left, right):
    if left >= right:
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    return reverseArray2(nums, left+1, right-1)

print(reverseArray2([0,1,2,3,4,5,6], 0, 6))
