class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

# Creating a rectangle
rectangle = Rectangle(5, 10)
rectangle.display()

# Creating a parallelepiped
parallelepiped = Parallelepipede(5, 10, 3)
parallelepiped.display()
print("Volume:", parallelepiped.volume())

Length: 5
Width: 10
Perimeter: 30
Area: 50

Length: 5
Width: 10
Perimeter: 30
Area: 50
Volume: 150
