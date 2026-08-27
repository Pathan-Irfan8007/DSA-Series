def rotateArray(nums, count):
    n = len(nums)
    count %= n
    nums[:] = nums[n-count:] + nums[:n-count]
    return nums

print(rotateArray([1,2,3,4,5,6,7,8,9,10],2))


# Without Slicing
def rotateArray2(nums, rotation):
    n = len(nums)
    rotation = rotation % n

    for _ in range(rotation):
        key = nums[n-1]
        for i in range(n-2, -1, -1):
            nums[i+1] = nums[i]

        nums[0] = key

    return nums

print(rotateArray2([1,2,3,4,5,6,7,8,9,10],2))


# Best / Optimal
def rotateArray3(nums, rotation):

    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    n = len(nums)
    rotation %= n
    reverse(nums, n-rotation, n-1)
    reverse(nums,0, n-rotation-1)
    reverse(nums, 0, n-1)

    return nums

print(rotateArray3([1,2,3,4,5,6,7,8,9,10],12))
