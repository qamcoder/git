class Student:
    def __init__(self, name, age, grade, marks=None):
        self.name = name
        self.age = int(age)
        self.grade = int(grade)
        self.marks = marks if marks is not None else {}
        self.info = {'Name': self.name, "Age": self.age, "Grade": self.grade, 'Marks': self.marks}
        # self.info.update(self.marks)

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        self.info['Marks'] = self.marks

    def show_info(self):
        print(f"{self.name} reads in {self.grade} grade and is {self.age} years old and his marks: ", end='')
        print(self.marks)

    def average_marks(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    @classmethod
    def from_dict(cls, dict_):
        name = dict_['Name']
        age = dict_['Age']
        grade = dict_['Grade']
        marks = dict_["Marks"]
        return cls(name, age, grade, marks)


class Students_database:
    def __init__(self):
        self.students = []
        self.students_info = []

    def add_student(self, student):
        self.students.append(student)
        self.students_info.append(student.info)

    def show_info_of_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                student.show_info()
                break
        else:
            print(f"Student '{student_name}' not found in the database.")

    def add_marks_to_student(self, student_name, subject, marks):
        for student in self.students:
            if student.name == student_name:
                student.add_marks(subject, marks)
                break
        else:
            print(f"Student '{student_name}' not found in the database.")

    def show_database(self):
        for student in self.students:
            student.show_info()


info_dict = {'Name': 'Ibrahim', 'Age': 15, 'Grade': 10,
             'Marks': {'Maths': 85, 'Science': 90, 'English': 88, 'History': 77}}
ibrahim = Student.from_dict(info_dict)
ibrahim.add_marks("History", 77)

bilal = Student("Bilal", 18, 11, {"Math": 85, "Science": 90, "English": 88})
bilal.add_marks("History", 71)

ali = Student('Ali', 19, 11, {"Maths": 77})

# ibrahim.show_info()

school = Students_database()
school.add_student(ibrahim)
school.add_student(bilal)
school.add_student(ali)

school.add_marks_to_student('Ibrahim','physics', 91)

school.show_info_of_student('Ali')
school.show_database()
