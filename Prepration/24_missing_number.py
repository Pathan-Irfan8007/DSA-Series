def missingNumber(nums):
    result = 0

    for i in nums:
        result ^= i

    for i in range(len(nums)+1):
        result ^= i

    return result

print(missingNumber([0,1,3]))
print(missingNumber([0,1,2,4,5,6,7,8,3]))