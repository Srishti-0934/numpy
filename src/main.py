import numpy as np

data = np.genfromtxt(
    "data/students.csv",
    delimiter=",",
    skip_header=1
)

print("\n STUDENT DATA ")
print(data)


student_ids = data[:, 0].astype(int)
marks = data[:, 1:]

subjects = [
    "Math",
    "Physics",
    "Chemistry"
]

print("\n===== SUBJECT STATISTICS =====")

for i in range(len(subjects)):

    print(f"\n{subjects[i]}")

    print("-"*25)

    print("Mean :", np.mean(marks[:, i]))

    print("Median :", np.median(marks[:, i]))

    print("Minimum :", np.min(marks[:, i]))

    print("Maximum :", np.max(marks[:, i]))

    print("Variance :", np.var(marks[:, i]))

    print("Standard Deviation :", np.std(marks[:, i]))

# Student Percentages

percentages = np.mean(marks, axis=1)

print("\nSTUDENT PERCENTAGES")

for student_id, percentage in zip(student_ids, percentages):
    print(f"Student {student_id}: {percentage:.2f}%")