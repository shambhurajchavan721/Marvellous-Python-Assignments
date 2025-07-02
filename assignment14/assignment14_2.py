class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def main():
    r = Rectangle(10, 5)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())

if __name__ == "__main__":
    main()