people ={}

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def addyears(self, x):
        self.age += x
        return self.age
    def __str__(self):
        return f"Name: {self.name}\nAge {self.age}\nGender: {self.gender}\n"
    
def addperson(self):
    print("Enter Name")
    name = str(input())
    print("Enter Age")
    age = int(input())
    print("Enter Gender")
    gender = str(input())
    people[name] = Person(name, age, gender)
    print("Person Added")