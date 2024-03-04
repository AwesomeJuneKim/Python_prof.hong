class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer=23
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")
    def update_odometer(self,mileage):
        #self.odometer=mileage
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print("You can't roll back an odometer.")
    def increment_odometer(self, miles):
        self.odometer+=miles

my_car=Car("audi","a7","2024")
print(my_car.get_descriptive_name())
my_car.update_odometer(22)
my_car.read_odometer()
my_car.update_odometer(20)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()