class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine has started with a roar!")

def main():
    v = Vehicle()
    v.start()

    print()

    c = Car()
    c.start()

if __name__ == "__main__":
    main()