class MyClass:
    def __init__(self, value):
        self._value = value


    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value


    @ten_value.setter
    def ten_value_set(self, new_value):
        self._value = new_value/10

obj = MyClass(10)
obj.show()
print(obj.ten_value)
obj.ten_value_set = 67
print(obj.ten_value)
obj.show()

