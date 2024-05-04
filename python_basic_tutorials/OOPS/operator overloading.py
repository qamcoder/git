class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    #         object_1
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)





v1 = Vector(3, 8, 7)
print(v1)

v2 = Vector(5, 1, 2)
print(v2)

v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)