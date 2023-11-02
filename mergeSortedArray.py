def mergeSortedArray(arr1,arr2):
    mergedArray = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1   
    while i<len(arr1):
        mergedArray.append(arr1[i])
        i += 1
    while j<len(arr2):
        mergedArray.append(arr2[j])
        j += 1
    return mergedArray

print(mergeSortedArray([-1,2,2,6,8],[-1,3,5,9]))




