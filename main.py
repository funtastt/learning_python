"""
IO Python - пока ничего сложного
"""

class Student:
    def __init__(self, name, age, faculty, university):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.university = university


class MedicalStudent(Student):
    def __init__(self, name, age, university):
        super(MedicalStudent, self).__init__(name, age, "Medical", university)


class ITStudent(Student):
    def __init__(self, name, age, university):
        super(ITStudent, self).__init__(name, age, "IT", university)


inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

while True:
    line = inputFile.readline()
    if not line:
        break
    data = line.strip().split(": ")
    personal = data[1].split(" ")
    faculty = data[0]
    name = personal[0]
    age = personal[1]
    university = personal[2]

    description = "Name: " + name + "\n"
    description += "Age: " + str(age) + "\n"
    description += "Studying in: " + university + ", faculty - " + faculty + "\n\n"

    outputFile.write(description)

