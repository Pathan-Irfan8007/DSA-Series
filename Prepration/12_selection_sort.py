def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if nums[min_index] > nums[j]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

print(selectionSort([9,5,4,1,2,6,7,4,1,5,0]))
