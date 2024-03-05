class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer=0
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

# my_car=Car("audi","a7","2024")
# print(my_car.get_descriptive_name())
# my_car.read_odometer()
# my_car.update_odometer(22)
# my_car.read_odometer()
# my_car.update_odometer(20)
# my_car.read_odometer()
# my_car.increment_odometer(100)
# my_car.read_odometer()