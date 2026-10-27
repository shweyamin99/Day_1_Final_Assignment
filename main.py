students = [
    {
"Name": "Aung Aung",
"Age": 21,
"Study Hours": 4.5,
"Python score": 85
 },
{
"Name": "Su Su",
"Age": 20,
"Study Hours": 3.0,
"Python score": 65
},
{
"Name": "Mg Mg",
"Age": 19,
"Study Hours": 2.0,
"Python score": 35
},
{
"Name": "Mya Mya",
"Age": 22,
"Study Hours": 5.0,
"Python score": 99
},
{
"Name": "Ko Ko",
"Age": 20,
"Study Hours": 1.5,
"Python score": 22
}
]

grade = ("Excellent", "Good", "Pass", "Fail")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return grade[0]
    elif score >= 60:
        return grade[1]
    elif score >= 40:
        return grade[2]
    else:
        return grade[3]

def count_passed(students):
    passed_count = 0
    for student in students:
        score = student["Python score"]

    if 40 <= score <= 100:
        passed_count += 1

    return passed_count

scores = [student["Python score"] for student in students]

print("\n===== STUDENT PERFORMANCE REPORT =====")

for student in students:
    score = student["Python score"]

    print(f"\nName: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Study Hours: {student['Study Hours']}")
    print(f"Score: {score}")
    print(f"Grade: {classify_grade(score)}")

average = calculate_average(scores)
highest = max(scores)
lowest = min(scores)
passed = count_passed(students)
failed = len(students) - passed

top_student = max(
    students,
    key=lambda student: student["Python score"]
)

print("\n===== SUMMARY =====")

print(f"Total Students: {len(students)}")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Passed Students: {passed}")
print(f"Failed Students: {failed}")
print(
    f"Top Student: {top_student['Name']} "
    f"({top_student['Python score']})"
)