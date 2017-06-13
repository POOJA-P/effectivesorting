def bubbleSort(alist):
    n = len(alist)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if alist[j] > alist[j+1] :
                alist[j], alist[j+1] = alist[j+1], alist[j]
