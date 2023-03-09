class Person:
    def __init__(self, name):
        self.name = name
        
    def printname(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, stage):
        super().__init__(name)
        self.stage = stage


s = Student('ivan', 3)
