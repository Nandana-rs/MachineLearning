import numpy as np

matrix_A = np.array([[1,2,3],
[4,5,6],
[7,8,9]])

matrix_B = np.array([[9,8,7],
[6,5,4],
[3,2,1]])

matrix_sum = matrix_A + matrix_B
print("The matrix addition is:",matrix_sum)

product = matrix_A * matrix_B
print("the product is:",product)

dots = np.dot(matrix_A,matrix_B)
print("The dot product is:",dots)

matrix_A_transpose = matrix_A.transpose()
print("The transpose of matrix A is:",matrix_A_transpose)
determinant_B = np.linalg.det(matrix_B)
print("The determinant of matrix B is:",(determinant_B))

eigenvalue_A,eigenvector_A = np.linalg.eig(matrix_A)

print("Eigen values of matrix A is:",eigenvalue_A)
print("Eigen vector of matrix A is :",eigenvector_A)