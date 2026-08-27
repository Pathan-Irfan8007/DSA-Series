def moveZeros(nums):
    if len(nums) == 0:
        return nums

    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1

    j = i+1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    return nums
          
print(moveZeros([1,2,3,0,0,1,2,0,4,5,6]))


def moveZeros2(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums

print(moveZeros2([1,2,3,0,0,1,2,0,4,5,6]))
