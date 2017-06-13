def mergeSort(alist):
    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
     # create temp arrays
        mergeSort(lefthalf)
        mergeSort(righthalf)
      # Merge the temp arrays back
        i=0     # Initial index of first subarray
        j=0     # Initial index of second subarray
        k=0     # Initial index of merge subarray
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            # Copy the remaining elements of L[], if there are any
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            # Copy the remaining elements of R[], if there are any
            j=j+1
            k=k+1
