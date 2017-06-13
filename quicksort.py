def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
        # splitpoint is partitioning index, alist[] is now at right place
       splitpoint = partition(alist,first,last)
       # Separately sort elements before partition and after partition
       quickSortHelper(alist,first,splitpoint-1)           
       quickSortHelper(alist,splitpoint+1,last)

# The main function that implements QuickSort
# alist[] --> list to be sorted, first --> Starting index, last --> Ending index
 
# Function to do Quick sort
def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark
