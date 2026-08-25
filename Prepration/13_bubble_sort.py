def bubbleSort(nums):
    n = len(nums)

    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if not is_swap:
            # print("Break")
            break

    return nums

print(bubbleSort([2,1,5,7,9,1,3,4,8]))
            