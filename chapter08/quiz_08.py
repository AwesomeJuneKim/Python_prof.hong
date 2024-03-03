#Quiz_1
def make_sandwich(*ingradients):
    print("다음의 재료로 샌드위치를 만들어주세요.")
    for ingredient in ingradients:
        print(f" {ingredient}")
    print("주문하신 샌드위치 나왔습니다.\n")

make_sandwich('chesse', 'lettuce','tomato','onion')
make_sandwich('chicken','pepper','onion','tomato')
make_sandwich('ham','mayo','lettuce','olive')

#Quiz_2
from user_profile import build_profile
my_profile=build_profile("Kim", "ujeong", location='busan', field='computer')
print(my_profile)


#Quiz_3
def car_info(company, model,**car_etc):
    car_etc['company']=company
    car_etc['model']=model
    return car_etc

car_make=car_info('subaru','outback',color='blue', tow_package=True)
print(car_make)