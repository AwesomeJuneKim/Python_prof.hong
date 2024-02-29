def ten_times(func):
    for i in range(5):
        func()
        
def print_hello():
    print("hello")
    
ten_times(print_hello)

def print_work():
    print('coding')
    
ten_times(print_work)

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