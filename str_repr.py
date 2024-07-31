class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"Person {self.name}; {self.age} years old."
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
    


katheryn = Person("Katheryn", 44)
print(katheryn)