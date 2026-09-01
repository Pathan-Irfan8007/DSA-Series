def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return [True, mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# print(binarySearch([0,1,2,3,4,5,6], 4))


# ---------- Lower & Upper Bound ----------
def lowUpBound(nums, target):
    lb, ub = -1, -1

    # Lower Bound
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            lb = mid
            right = mid - 1
        else:
            left = mid + 1

    # Upper Bound
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            ub = mid
            left += 1
        else:
            right -= 1

    return [lb, ub]

print(lowUpBound([0,0,1,1,1,1,2,3,4], 1))