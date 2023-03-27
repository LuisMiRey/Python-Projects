class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
       return f"{self.name}: {self.score}"

students = [Student("Andres", 0.46), Student("Naomi", 0.75), Student("Musk", 0.95)]

failing_students = []

for student in students:
    if student.score < 0.7:
        failing_students.append(student)

filter_list = list(filter(lambda student: student.score < 0.7 , students))

print(filter_list)

#Challenge use filter to list all even numbers

numbers = [1,2,3,4,5]

filter_even = list(filter(lambda number: number % 2 == 0 , numbers))

print(filter_even)

