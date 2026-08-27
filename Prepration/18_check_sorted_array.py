def checkSortedArray(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    else:
        return True

print(checkSortedArray([1,2,3,4,5,6,7,8,9]))
print(checkSortedArray([1,2,3,10,5,6,7,8,9]))