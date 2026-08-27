# First Largest In Array
def largestInArray(nums):
    largest = float("-inf")

    for num in nums:
        if num > largest:
            largest = num

    return largest

# print(largestInArray([55,32,99,-97,45,32,88,21]))

def secondLargest(nums):
    first_max = float("-inf")
    second_max = float("-inf")

    for num in nums:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num

    return second_max

print(secondLargest([55,32,99,-97,45,32,88,21]))