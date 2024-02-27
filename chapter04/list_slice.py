squares=[value**2 for value in range(1,11)] #list comprehension
print(squares)
print(squares[0:3])
print(squares[:4])
print(squares[2:])
print(squares[-3:])
print(squares[2:9:2])

print(squares[::-2])

a=[1,2]
b=[3,4]
c=a+b
print(c)

c1=[x for x in a if x not in b]
print(c1)
c2=list(set(a)-set(b))
print(c2)