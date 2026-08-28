def findMaxConsecutiveOnes(nums):
    flag = False
    count = 0
    result = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            # if count > result:
            #     result = count
            result = max(result, count)
            count = 0

    # if count > result:
        # result = count
    return max(result, count)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,0,1]))
print(findMaxConsecutiveOnes([1,1,0,1,0,1,1,1,1,0,1,1]))
            