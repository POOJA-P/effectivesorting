def insertionSort(alist):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(alist)):
 
        key = alist[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < alist[j] :
                alist[j+1] = alist[j]
                j -= 1
        alist[j+1] = key
