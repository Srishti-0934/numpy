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


# Overall Topper

topper_index = np.argmax(percentages)

print("\nOVERALL TOPPER")
print(f"Student ID : {student_ids[topper_index]}")
print(f"Percentage : {percentages[topper_index]:.2f}%")

# Lowest Scorer

lowest_index = np.argmin(percentages)

print("\nLOWEST SCORER")
print(f"Student ID : {student_ids[lowest_index]}")
print(f"Percentage : {percentages[lowest_index]:.2f}%")

# Subject Toppers

print("\nSUBJECT TOPPERS")

for i, subject in enumerate(subjects):
    topper = np.argmax(marks[:, i])

    print(
        f"{subject}: "
        f"Student {student_ids[topper]} "
        f"({marks[topper, i]:.0f})"
    )

   
# Student Rankings

ranking = np.argsort(percentages)[::-1]

print("\nSTUDENT RANKINGS")

for rank, index in enumerate(ranking, start=1):
    print(
        f"Rank {rank}: "
        f"Student {student_ids[index]} "
        f"({percentages[index]:.2f}%)"
    )

# Grade Generator

grades = np.full(len(percentages), "F", dtype="<U2")

grades[percentages >= 90] = "A+"
grades[(percentages >= 80) & (percentages < 90)] = "A"
grades[(percentages >= 70) & (percentages < 80)] = "B"
grades[(percentages >= 60) & (percentages < 70)] = "C"
grades[(percentages >= 50) & (percentages < 60)] = "D"

print("\nSTUDENT GRADES")

for sid, grade in zip(student_ids, grades):
    print(f"Student {sid}: {grade}")

# Pass / Fail Analysis

passed = np.all(marks >= 40, axis=1)

print("\nPASS / FAIL STATUS")

for sid, status in zip(student_ids, passed):
    result = "PASS" if status else "FAIL"
    print(f"Student {sid}: {result}")
    print("\nSUBJECT PASS PERCENTAGE")

for i, subject in enumerate(subjects):
    passed = np.sum(marks[:, i] >= 40)
    percentage = (passed / len(marks)) * 100

    print(f"{subject}: {percentage:.2f}%")

class_average = np.mean(percentages)

print("\nCLASS AVERAGE")
print(f"{class_average:.2f}%")

class_average = np.mean(percentages)

print("\nCLASS AVERAGE")
print(f"{class_average:.2f}%")

print("\nABOVE CLASS AVERAGE")

above = percentages > class_average

for sid, per in zip(student_ids[above], percentages[above]):
    print(f"Student {sid}: {per:.2f}%")


print("\nDISTINCTION HOLDERS")

distinction = percentages >= 75

for sid in student_ids[distinction]:
    print(f"Student {sid}")


failed_subjects = np.sum(marks < 40, axis=1)

print("\nFAILED SUBJECT COUNT")

for sid, count in zip(student_ids, failed_subjects):
    print(f"Student {sid}: {count}")

print("\nHIGHEST MARKS")

for i, subject in enumerate(subjects):
    print(f"{subject}: {np.max(marks[:, i])}")

print("\nHIGHEST MARKS")

for i, subject in enumerate(subjects):
    print(f"{subject}: {np.max(marks[:, i])}")

print("\nMARKS RANGE")

for i, subject in enumerate(subjects):
    rng = np.ptp(marks[:, i])

    print(f"{subject}: {rng}")

means = np.mean(marks, axis=0)

hardest = np.argmin(means)
easiest = np.argmax(means)

print("\nSUBJECT ANALYSIS")

print("Hardest Subject:", subjects[hardest])
print("Easiest Subject:", subjects[easiest])

print("\nOVERALL CLASS STATISTICS")

print("Highest Percentage:", np.max(percentages))

print("Lowest Percentage:", np.min(percentages))

print("Average Percentage:", np.mean(percentages))

print("Median Percentage:", np.median(percentages))

print("Standard Deviation:", np.std(percentages))