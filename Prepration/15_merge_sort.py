# merge 2 sorted arrays
def mergeSortedArray(arr1, arr2):
    result = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)

    while i<n and j<m :
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    if i<n :
        while i<n:
            result.append(arr1[i])
            i += 1
    else:
        while j<m:
            result.append(arr2[j])
            j += 1

    return result

print(mergeSortedArray([1,3,5,7], [2,4,6,8,10,12]))