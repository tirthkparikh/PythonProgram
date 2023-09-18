class Student: 
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hi {self.name}"
    def display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")


s1 = Student("Anirudh", 55)
print(s1)
s1.display()