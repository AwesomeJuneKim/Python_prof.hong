from car import ElectricCar
# from 파일이름 import 클래스이름

my_leaf=ElectricCar("Ford", "Mustang", "2019")
print(f"전기차는 {my_leaf.get_descriptive_name()}입니다.")
print("전기차는 {}".format(my_leaf.get_descriptive_name()))
my_leaf.battery_size.describe_battery()