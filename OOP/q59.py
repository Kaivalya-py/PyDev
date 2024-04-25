# Design a class hierarchy for a vehicle management system where `Vehicle` is the base class with common attributes like `make`, `model`, and `year`. Derive two subclasses from it: `Car` and `Motorcycle`, each having specific attributes like `car_type` (SUV, Sedan, etc.) for `Car` and `has_sidecar` (True/False) for `Motorcycle`. Implement an initialization method for each class that appropriately uses `super()` to leverage the base class `__init__`. Include a method `display_vehicle_info()` in each class to print the vehicle's details.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_vehicle_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print()

class Car(Vehicle):
    def __init__(self, make, model, year, car_type):
        super().__init__(make, model, year)
        self.car_type = car_type

    def display_vehicle_info(self):
        super().display_vehicle_info()
        print(f"Car Type: {self.car_type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def display_vehicle_info(self):
        super().display_vehicle_info()
        print(f"Has Sidecar: {self.has_sidecar}")

c = Car("Toyota", "Camry", 2019, "Sedan")
c.display_vehicle_info()
