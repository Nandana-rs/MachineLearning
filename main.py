
import numpy as np
arr1=np.array([1,2,3,4,5])

# Append values to the end of an array.
appended_array=np.append(arr1,[6,7,8])

# Insert values into an array at a specified position.
inserted_array=np.insert(arr1,2,0)

# Delete elements from an array.
deleted_array=np.delete(arr1,[1,3])

# Find unique elements in an array.
unique_array=np.unique(arr1)

# Sort an array.
sort_array=np.sort(arr1)

# Save an array to a text file.
np.savetxt('my_array.txt',arr1)

# Load data from a text file into an array.
loaded_array=np.loadtxt('my_array.txt')

print("Original array",arr1)
print("Appended array",appended_array)
print("inserted array",inserted_array)
print("deleted array",deleted_array)
print("unique array",unique_array)
print("Sorted array",sort_array)
print("Loaded array",loaded_array)