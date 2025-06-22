
class Person:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self.__age = age          # private attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

person1 = Person("Alice", 30)
person1.display()

# Accessing private attribute directly will fail
# print(person1.__age)  # Uncommenting this line will raise AttributeError

# Using setter to change age
person1.set_age(35)
print("Updated Age:", person1.get_age())