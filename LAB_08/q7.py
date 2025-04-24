import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1.magnitude())
print(v1.rotation())
print(v1.distance(v2))
print(v1.dot_product(v2))
print(v1.cross_product(v2))

v3 = Vector3D(1, 2, 3)
v4 = Vector3D(4, 5, 6)

print(v3.magnitude())
print(v3.distance(v4))
print(v3.dot_product(v4))
cross = v3.cross_product(v4)
print(cross.x, cross.y, cross.z)
