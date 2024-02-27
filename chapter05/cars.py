cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort(reverse=True)#알파벳 역순으로 정렬
print(cars)

cars=sorted(cars)
print(cars)

for car in cars:#확장형 for문
    # print(car)
    print(f"my car is a {car}")
