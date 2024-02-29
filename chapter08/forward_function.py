def ten_times(func):
    for i in range(5):
        func()
        
def print_hello():
    print("hello")
    
ten_times(print_hello)

def print_work():
    print('coding')
    
ten_times(print_work)