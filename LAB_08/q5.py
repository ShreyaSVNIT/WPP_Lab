import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.length = a
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

sh = input("Enter Shape (Circle/Rectangle): ").strip().capitalize()

if sh == 'Circle':
    rad = float(input("Enter radius: "))
    circle = Circle(rad)
    print(f"Perimeter of circle = {circle.perimeter()}")
    print(f"Area of circle = {circle.area()}")

elif sh == 'Rectangle':
    l = float(input("Enter the length: "))
    b = float(input("Enter the breadth: "))
    rect = Rectangle(l, b)
    print(f"Perimeter of rectangle = {rect.perimeter()}")
    print(f"Area of rectangle = {rect.area()}")

else:
    print("Invalid shape entered.")
