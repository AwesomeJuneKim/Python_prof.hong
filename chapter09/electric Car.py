class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """전기차에만 해당하는 특징을 정의합니다."""
    
    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다."""
        super().__init__(make, model, year)
        self.battery_size=40
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    #Car클래스에 fill_gas_tank()메서드가 있다고 치고
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank.")

my_leaf=ElectricCar("Ford", "Mustang", "2019")
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
print(f"이차의 배터리는 {my_leaf.battery_size}-kWh 입니다.")
my_leaf.fill_gas_tank()