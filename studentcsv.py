import pandas as pd
df = pd.read_csv('student_data.csv')
print("CSV FILE IS :",df)

print("rows of students who are 20 years old or older. ")
age = df[df['Age'] >= 20]
print(age)

print("Calculate the average GPA of the students in the DataFrame.")
avg = df['GPA'].mean()
print(avg)

print("Sorted DataFrame in descending order of GPA and displaying the top 5 students with the highest GPAs")
DesOrt = df.sort_values(by=['GPA'], ascending=False)
topFive = DesOrt.head(5)
print(topFive)

print("Group the students by their ages and calculate the average GPA for each age group ")
ageGroup = df.groupby('Age')['GPA'].mean().reset_index()
print(ageGroup)