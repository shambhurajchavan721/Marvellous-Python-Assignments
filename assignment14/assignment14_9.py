class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

    def _eq_(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def display(self):
        print(f"Product: {self.name}, Price: {self.price}")


def main():
    p1 = Product("Laptop", 1500)
    p2 = Product("Smartphone", 1500)
    p3 = Product("Tablet", 1200)

    p1.display()
    p2.display()
    p3.display()

    print(f"p1 == p2? {p1 == p2}")
    print(f"p1 == p3? {p1 == p3}")


if __name__ == "__main__":
    main()