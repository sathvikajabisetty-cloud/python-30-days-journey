
# Day 13: File Handling in Python

# Program 1: Write data into a file
with open("student.txt", "w") as file:
    file.write("Name: Sathvika\n")
    file.write("Course: CSE-DS\n")
    file.write("Subject: Python\n")


# Program 2: Read data from a file
with open("student.txt", "r") as file:
    content = file.read()
    print("Student Details:")
    print(content)


# Program 3: Append data to a file
with open("student.txt", "a") as file:
    file.write("Subject: SQL\n")

with open("student.txt", "r") as file:
    print("Updated Details:")
    print(file.read())


# Program 4: Handle a missing file
try:
    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found!")


# Program 5: Calculate average marks from a file
with open("marks.txt", "w") as file:
    file.write("85\n")
    file.write("90\n")
    file.write("75\n")

with open("marks.txt", "r") as file:
    marks = []

    for line in file:
        marks.append(int(line.strip()))

    total = sum(marks)
    average = total / len(marks)

    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
