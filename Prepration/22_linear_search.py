def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    else:
        return -1

print(linearSearch([0,1,2,3,4,5,6,7,8,9], 5))