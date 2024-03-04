def ten_times(func):
    for i in range(5):
        func()
        
def print_hello():
    print("hello")
    
ten_times(print_hello)

def print_work():
    print('coding')
    
ten_times(print_work)

#1+ 함수 자체를 인수로 전달하는 방법
def add(x,y):
    return x+y
def minus(x,y):
    return x-y

def apply_operation(operation,x,y):
    return operation(x,y)

result = apply_operation(add,3,4)
print(result)
result2= apply_operation(minus,4,3)
print(result2)

#2+ 위의 apply_operation을 이용하지 않고 함수전달하는 방법
##map(), filter() 함수사용
# def power(item):
#     return item**2

# def under_three(item):
#     return item < 3

#3+더 쉬운 방법은 람다식을 이용하는 방법이다.
power=lambda x:x*x
under_three=lambda x:x<3

#2+ map()을 사용해서 함수를 적용시킨다.(람다식에도 동일하게 적용 됨)
lst=[1,2,3,4,5]
map_list=map(power, lst)
print(f"map()함수 적용결과: {list(map_list)}")

map_list=map(under_three, lst)
print(f"두번째 적용결과: {list(map_list)}")
