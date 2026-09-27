students = {
    "Shenaya": 100,
    "Michael": 92,
    "Kylian": 78,
    "Sakina": 95,
    "Mia": 88
}
total = 0

for score in students.values():
    total += score

average = total / len(students)

top_score = max(students.values())
bottom_score = min(students.values())

top_student = max(students, key=students.get)
bottom_student = min(students, key=students.get)

print("Class average: ", average)
print("Top scorer:", top_student, "-", top_score)
print("Bottom scorer:", bottom_student, "-", bottom_score)

name = input("Enter a student's name: ")

grade = students.get(name)

if grade is not None:
    print(name, "has a score of", grade)
else:
    print("Student not found.")