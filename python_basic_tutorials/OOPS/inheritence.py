class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")



e1 = Employee("Ibrahim", 456332)
e1.showDetails()
e2 = Programmer("Harry", 169040)
e2.showDetails()
e2.showLanguage()
