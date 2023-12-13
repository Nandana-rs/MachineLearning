import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

# Add arr1 and arr2 to create a new array called result_add.
result_add = arr1 + arr2
print("The sum of arrays are : ",result_add)

# Multiply arr1 and arr2 to create a new array called result_multiply.
result_multiply = arr1 * arr2
print("The product of 2 arrays are : ",result_multiply)

# Calculate the mean of result_add.
mean=np.mean(result_add)
print("The mean of sum is : ",mean)

# Find the maximum value in result_multiply.
max=np.max(result_multiply)
print("The maximum value is : ",max)