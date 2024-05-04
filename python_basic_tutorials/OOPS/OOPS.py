class person:
    ful_name = 'Ibrahim Qamar'
    age = '16'
    profession = 'vela'
    def info(self):
        print(f'{self.ful_name} is {self.profession}')


ibrahim = person()
bilal = person()
bilal.ful_name = 'Bilal ateeq'
bilal.profession = 'hr'
print(ibrahim.info())
bilal.info()