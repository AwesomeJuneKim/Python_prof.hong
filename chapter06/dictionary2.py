h='hello'
# h[0]='H'#리스트가 아니라서 불가능???
print(h)

def add(x,y):
    return x+y
d={
    'a':{'aa':1, 'aaa':2},
    'b':{'bb':3, 'bbb':4},
    'c':{'cc':5, 'ccc':add(2,3)},#딕셔너리에 메서드도 추가할 수 있다.
}
print("딕셔너리에 메서드 추가",d)
db2={}
# db2['a'].append('3')#-> 바로 어펜드 넣을 수 없음(비어있기 때문에)
db2['a']=list()#->리스트를 삽입한 후에 어펜드 가능함
db2['a'].append('3')
print("어펜드:",db2)
