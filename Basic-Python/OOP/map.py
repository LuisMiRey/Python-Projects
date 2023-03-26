#Map,filter and reduce

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = [Student("Andres", 0.46), Student("Naomi", 0.75), Student("Musk", 0.95)]

student_results = []
for student in student:
#    if student.score >= 0.7:
#        student_results.append(f"{student.name} Passed")
#    else:
#        student_results.append(f"{student.name} Failed")
     student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed")

#map(lambda student: student.name, students)

print(student_results)

#Another form

numbers = [1,2,3,4,5]

print(list(map(lambda number: number * 2, numbers)))

