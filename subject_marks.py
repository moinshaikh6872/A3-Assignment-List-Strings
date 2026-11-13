subjects = ["Math", "Science", "English", "History"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter your marks for {subject}: "))
    marks.append(mark)

print("\n--- Student Report ---")
total_marks = 0
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]}")
    total_marks += marks[i]

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {total_marks / len(subjects)}")
