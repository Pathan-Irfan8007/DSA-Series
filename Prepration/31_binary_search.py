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
    x, y = -1, -1
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            x, y = mid, mid
            while x > left and nums[x] == nums[x-1]:      # Lower Bound 
                x -= 1
            while y < right and nums[y] == nums[y+1]:      # Upper Bound
                y += 1
            break
            
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [x, y]

print(lowUpBound([0,0,1,1,1,1,2,3,4], 4))