# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
# #2+배터리 클래스를 하나 더 만들어서 전기차에 연결시킨다.
from car import Car
#3+ class Car을 모두 주석처리함
#3+ 이것만 적어도 자동으로 연결되기 때문에 ElectricCar의 슈퍼클래스가 연결되어 에러가 뜨지 않는다.
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def increment_battery(self, volume):
        self.battery_size += volume

    def get_range(self):
        if self.battery_size<=40:
            range=150
        elif self.battery_size>40 and self.battery_size<=60:
            range=225
        print(f"This car has a range of {range} miles.")
class ElectricCar(Car):
    """전기차에만 해당하는 특징을 정의합니다."""
    
    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다."""
        super().__init__(make, model, year)
        self.battery_size=Battery()#2+위의 배터리 클래스를 연결시켜 줌

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank.")
    

my_leaf=ElectricCar("Ford", "Mustang", "2019")
print(my_leaf.get_descriptive_name())
my_leaf.fill_gas_tank()
my_leaf.battery_size.describe_battery()
my_leaf.battery_size.increment_battery(20)
my_leaf.battery_size.describe_battery()
my_leaf.battery_size.get_range()
