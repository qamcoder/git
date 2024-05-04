class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def sum(a, b):
        return a + b


a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.sum(a.num, 7))

print(Math.sum(7, 2))
