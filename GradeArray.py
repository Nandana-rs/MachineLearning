import numpy as np
grades = np.array([85,90,78,92,88,76,95,89,84,91])

# average (mean) grade in the class
mean_result = np.mean(grades)
print("The mean value is:",mean_result)
average = np.average(mean_result)
print("The average of the mean is:",average)

# students scored above 90
score = grades[grades>90]
print("The above 90 scores are:",score)
s = score.size
print("The no of students who scored above 90 are :",s)

#  standard deviation of the grades
dev = np.std(grades)
print("The standard deviation of the grades are:",dev)