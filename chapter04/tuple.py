def test():
    return(10,20)

a,b=test() #tuple값을 리턴
print(f"a= {a}, b= {b}")

lst=['a','b','c','d']
for i, value in enumerate(lst):
    print(f"i= {i}, value= {value}")