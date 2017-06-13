#!/usr/bin/env python3
print( "enter the numbers to be sorted")	#give numbers with tab 
alist=list(map(int,input().split()))
print('\v')
print( "original list:")
print (alist)
print('\v')
height=[]                                           #height of bars


import time
start_time = time.time()
import quicksort
quicksort.quickSort(alist)
print('1 . Sorted numbers by a Quicksort are : ')
print(alist)
r=time.time() - start_time
print("--- %s seconds for Quicksort ---" % (r))               #getting the running time
height.append(r)                                              #to get the height for the graph


print('\v')


import time
start_time = time.time()
import mergesort
mergesort.mergeSort(alist)
print('2 . Sorted numbers by a Mergesort are :  ')
print(alist)
r2=time.time() - start_time
print("--- %s seconds for Mergesort ---" % (r2))           #getting the running time
height.append(r2)                                          #to get the height for the graph


print('\v')


import time
start_time = time.time()
import bubblesort
bubblesort.bubbleSort(alist)
print('3 . Sorted numbers by a Bubblesort are : ')
print(alist)
r3=time.time() - start_time
print("--- %s seconds for Bubblesort ---" % (r3))                       #getting the running time
height.append(r3)                                                       #to get the height for the graph


print('\v')


import time
start_time = time.time()
import insertionsort
insertionsort.insertionSort(alist)
print('4 . Sorted numbers by a Insertionsort are : ')
print(alist)
r4=time.time() - start_time
print("--- %s seconds for Insertionsort ---" % (r4))                 #getting the running time
height.append(r4)                                                    #to get the height for the graph


print('\v')


import time
start_time = time.time()
import heapsort
heapsort.heapSort(alist)
n = len(alist)
print('5 . Sorted numbers by a Heapsort are : ')
print(alist)
r5=time.time() - start_time
print("--- %s seconds for Heapsort ---" % (r5))                            #getting the running time
height.append(r5)                                                          #to get the height for the graph


print('\v')
tick_label=[]


import matplotlib.pyplot as plt
import numpy as np
left = [1, 2, 3, 4, 5]                                                    # x-coordinates of left sides of bars 

tick_label = ['quick', 'merge', 'bubble', 'insertion', 'heap']            # labels for bars
y_pos = np.arange(len(tick_label))
# plotting a bar chart
plt.bar(y_pos, height,align='center',
		width = 0.8, color = ['red', 'blue'])
plt.xticks(y_pos, tick_label)

plt.xlabel('x - axis = sorting')                                         # naming the x-axis
plt.ylabel('y - axis = running time in seconds')                         # naming the y-axis
plt.title('Running time for the sorting functions!')                     # plot title

plt.show()                                                               # function to show the plot
