# To heapify subtree rooted at index i.
# n is size of heap
def heapify(alist, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is greater than root
    if l < n and alist[i] < alist[l]:
        largest = l
 
    # See if right child of root exists and is greater than root
    if r < n and alist[largest] < alist[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        alist[i],alist[largest] = alist[largest],alist[i]  # swap
 
        # Heapify the root.
        heapify(alist, n, largest)
 
# The main function to sort an array of given size
def heapSort(alist):
    n = len(alist)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(alist, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]   # swap
        heapify(alist, i, 0)
