
# ----- Kadane’s Algorithm -----

def maximumSubarraySum(nums):
    maxi = float("-inf")
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        maxi = max(maxi, total)

        if total < 0:
            total = 0

    return maxi

print(maximumSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))