import math

class CircleComp:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = None
        self.circumference = None
        self.area = None

    def calculate_properties(self):
        self.diameter = self.radius * 2.0
        self.circumference = 2 * math.pi * self.radius
        self.area = math.pi * self.radius * self.radius

    def print_properties(self):
        print(f"Diameter: {self.diameter:.2f}")
        print(f"Circumference: {self.circumference:.2f}")
        print(f"Area: {self.area:.2f}")

def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = CircleComp(radius)
    circle.calculate_properties()
    circle.print_properties()

if __name__ == "__main__":
    main()
