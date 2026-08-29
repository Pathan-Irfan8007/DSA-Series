def twoSum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        else:
            hash_map[nums[i]] = i

# print(twoSum([0,1,2,3,4,5], 7))
# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,2,4], 6))
# print(twoSum([3,3], 6))
