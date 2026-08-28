
# Merge 2 Sorted Arrays - no duplicates 
def mergeWithoutDuplicates(arr1, arr2):
    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    k = 0
    result = []

    while i<m and j<n:
        if arr1[i] <= arr2[j]:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1


    while i<m:
        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j<n:
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result

print(mergeWithoutDuplicates([1,2,3,4,5,7,9], [2,4,6,7,8]))