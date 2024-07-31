class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student = Student("Bob", (90, 81, 70, 44, 100))
student2 = Student("Anya", (54, 38, 44, 80, 70))

print(student.average_grade())
print(student2.average_grade())