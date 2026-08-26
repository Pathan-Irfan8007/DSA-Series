def partition(nums, low, high):
    pivot = nums[low]
    i,j = low,high

    while i < j:
        while nums[i] <= pivot and i <= high-1:
            i += 1
        while nums[j] >= pivot and j >= low+1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j

def quickSort(nums, low, high):
    if low < high:
        index = partition(nums, low, high)
        quickSort(nums, low, index-1)
        quickSort(nums, index+1, high)

    return nums

print(quickSort([4,2,3,1,8,9,7], 0, 6))