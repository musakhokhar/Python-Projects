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
    name = str(input()).lower()
    print("Enter Age")
    age = abs(int(input()))
    gender = ""
    while gender == "":
        print("Enter Gender")
        choice = str(input()).lower()
        if choice == "male" or choice == "female":
            gender = choice
        else:
            print("Invalid Gender, try again")
    people[name] = Person(name, age, gender)
    print("Person Added")