import numpy as np

marks = np.array([
    [80, 90, 70],
    [50, 60, 70],
    [90, 95, 85]
])

student_averages = np.mean(marks, axis=1)

passed_students = np.where(student_averages > 75)[0]

print("Students with averages greater than 75:", passed_students)
