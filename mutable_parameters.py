from typing import List, Optional

class Ztudent:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Ztudent("Bob")
rolf = Ztudent("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)