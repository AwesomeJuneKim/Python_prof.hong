#1차원 리스트에만 적용되는 방법
a=[10,20,30,40,50]
b=a #얕은 복사
b1=a[:]#깊은 복사
print(b)

a[0]=100
print(b)
print(b1)

#2차원 리스트에서는 a[:]가 얕은복사이고 깊은복사는 deepcopy함수를 써야한다.
