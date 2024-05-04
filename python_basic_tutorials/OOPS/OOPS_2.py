class pers:
    def __init__(self):
        print('I get executed as soon as an object is created\n')


e = pers()

class persons():
    def __init__(self, name, occ, age):
        self.name = name
        self.profession = occ
        self.age = age

    def info(self):
        print(f"{self.name} is a {self.age} year old {self.profession}")


ibrahim = persons('Ibrahim Qamar', 'programmer', 16)
bilal = persons('Bilal ateeq', 'sailor', 17)
ali = persons("Ali amaan", 'business man', 19)


ali.info()
ibrahim.info()
bilal.info()