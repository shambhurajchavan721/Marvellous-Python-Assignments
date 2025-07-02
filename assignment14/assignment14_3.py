class Book:
    def _init_(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price

def main():
    b = Book(500)
    print("Price:", b.get_price())
    b.set_price(700)
    print("Updated Price:", b.get_price())

if __name__ == "__main__":
    main()