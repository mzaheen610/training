def descendingBubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array : ",arr)

array1 = [3,-2,1,4,5,8]
descendingBubblesort(array1)


 