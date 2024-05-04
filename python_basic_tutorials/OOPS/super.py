class ParentClass:
    def parent_method(self):
        print('This is parent class')


class ChildClass(ParentClass):
    def parent_method(self):
        print("this is child class")
    def child_method(self):
        print('This is child class')
        self.parent_method()
        super().parent_method()


o = ChildClass()
o.parent_method()
o.child_method()
