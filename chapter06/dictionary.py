a={#딕셔너리->키&밸류값으로 구성됨->검색에 유용
    'a':1,
    'b':2,
    'c':3,}
b=[1,2,3,4]
print(type(a),type(b)) #<class 'dict'> <class 'list'>
print(a['b'])
a['d']=4 #라이브러리는 쉽게 값을 추가할 수 있다. 리스트는 append나 insert로 추가할 수 있다.
print(a)
a['b']=3
print(a)

c={#딕셔너리 안에 딕셔너리를 넣을 수 있다.
    9:{'정원':'A+'},
    7:{'윤정':'A+'},
    3:{'세영':'A+'}
    }
print(c)
#print(c[1]['정원'])#딕셔너리 안의 딕셔너리를 검색하는 방법
d=c.get(3)
print(d)
print("리스트의 길이:",b[-1])#리스트의 길이
print(c.get(4,0))#딕셔너리의 길이를 알때 4를 검색하면 에러를 뜨지 않게 하기위한 방어코드

for row in c:#인덱스가 출력
    print(row)
for row in c.items():#내용전체 출력
    print(row)
for k,v in c.items():#튜플출력
    print(k,v, type(row))

e=[3,2,1]
print(sorted(e),e) #e.sort()보다 sorted(e)를 더 많이 쓴다.(앞에건 e를 바꾸는것 이기 때문에)

print(sorted(c))
print(sorted(c.items()))

f={
    9:'C',
    7:'B',
    3:'A'
}
#성적순(밸류값)으로 솔팅하기 위한 방법
first= lambda x:x[0]
second= lambda x:x[1]
for row in f.items():
    print(first(row), second(row))
g=sorted(f.items(), key=second)
print(g)

for x in range(5):
    for y in range(10):
        print(x,y)
if x<5:
    print('low')
else:
    print('high')