
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
        
s1 = Student("Rahul", 20)
s1.display()
print(s1.name)

s2 = Student("RakibHasan", 23)
s2.display()
print(s2.name)