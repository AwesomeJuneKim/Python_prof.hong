squares=[]
for value in range(1,11):
    #square=value**2
    squares.append(value**2)
print(squares)
# 간단하게 아래처럼 나타낼 수 있다.

squares=[value**2 for value in range(1,11)] #list comprehension
print(squares)
