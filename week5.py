class smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
phone1 = smartphone("Apple", "iPhone 14", 999)
phone2 = smartphone("Samsung", "Galaxy S22", 799)
phone3 = smartphone("Google", "Pixel 6", 599)
class smartwatches(smartphone):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
watch1 = smartwatches("Apple", "Apple Watch Series 7", 399)
watch2 = smartwatches("Samsung", "Galaxy Watch 4", 249)

#Question 2
class Animal:
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

for vehicle in [Car(), Plane(), Boat()]:
    print(vehicle.move)
for animal in [Dog(), Bird(), Fish()]:
    print(animal.move)