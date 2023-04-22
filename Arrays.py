import numpy as np
import random

#Empty list so max's can be printed on one line later
max_columns = []

#Initializing array with random values using numpy and random modules with max value 10 and size 5x5 of type integer
array = np.random.randint(10, size=(5,5), dtype=int)

#Printing entire array
print('Printing Array... \n\n',array)

#Printing contents of 2nd row, 3rd column of array
print('\nContents of 2nd row, 3rd column: ',array[1][2])

#Printing sum of entire array
print('\nSum of entire array: ',sum(sum(array)))

#Printing Mean of each row
print('\nMean of each row: ',np.mean(array, axis=1))

#Calculating and storing max value of each column of array in max_columns list
for x in range(5):
    max_columns.append(((max(array[:,x]))))
    
#Printing Max value of each column
print('\nMax value of each Column:',max_columns)
