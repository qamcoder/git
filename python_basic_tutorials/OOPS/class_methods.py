class Employee:
    company = 'Apple'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'Name of employee of {self.company} is {self.name}')

    # This decorator takes class as the first argument while normally first argument is the instance(object) itself

    @classmethod
    def change_company(cls, new_company_name):
        cls.company = new_company_name


emp1 = Employee('Ibrahim')
emp1.show()
emp1.change_company('Tesla')
emp1.show()

emp2 = Employee('Bilal')
emp2.show()

