class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
       return f"{self.name}: {self.score}"

students = [Student("Andres", 0.46), Student("Naomi", 0.75), Student("Musk", 0.95)]

score_total = 0
for student in students:
    score_total += student.score

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total , students, 0)

print("score_total ", score_total / len(students))
print("reduce_total ", round(reduce_total / len(students), 4))

#Challenge use reduce to multiply all the numver togerther

numbers = [1,2,3,4,5]
total_average = 0
reduce_mul = reduce(lambda total, number: number * total ,numbers)

print(reduce_mul)

