class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, _string):
        return cls(_string.split("-")[0], int(_string.split("-")[1]))


e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))


person = Person.from_string("John Doe, 30")
print(person.name, person.age)
