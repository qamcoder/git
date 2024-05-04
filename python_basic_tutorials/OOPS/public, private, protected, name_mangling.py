###########################-------P R I VA T E-------################################
class Person:
    def __init__(self):
        self.__name = 'Bilal'


a = Person()
# print(a.__name) # gives error
print(dir(a))
print(a._Person__name)

###########################-------P R O T E C T E D-------################################


class Student:
    def __init__(self):
        self._age = 17


class Ibrahim(Student):
    name = 'Ibrahim'


b = Student()
# print(b.age)  # gives error
print(b._age)
c = Ibrahim()
print(c.name)
print(c._age)

