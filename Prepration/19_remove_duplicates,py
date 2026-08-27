     # In place replacement
def removeDuplicates2(nums):
    i = 0
    j = i + 1 

    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            j  += 1
        else:
            j += 1
    return nums[:i+1], i+1

print(removeDuplicates2([1,1,1,2,2,3,4,5,5,6,6]))
print(removeDuplicates2([1]))


