def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("Student:", name)
    print(f"(Roll:{roll})")
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    print("Subjects scored below 40:")
    found = False
    for i in range(len(marks)):
        if marks[i] < 40:
            print(f"Subject {i + 1}: {marks[i]}")
            found = True

    if not found:
        print("None")

name = "Niranjanaa"
roll = 101
marks = [95.0, 82.5, 76.0, 38.0, 91.0]

analyze_result(name, roll, marks)