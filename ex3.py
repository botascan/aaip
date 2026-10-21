# module ex3

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getAddress(self):
        return self.address

    def greet(self):
        return f"A good day to {self.getName()}!"

    @classmethod
    def from_string(cls, string):
        name, age, address = str.split(",", 2) # in case address contains commas, split on the first two commas
        return cls(name.strip(),int(age),address.strip())
        

class Student(Person):
    def __init__(self, name, age, address, university):
        super().__init__(name, age, address)
        self.university = university
    
    def greet(self):
        return f"A good day to {self.name} hailing from {self.university}!"