class Shape:
    def __init__(self,base,height):
        self.__base=base
        self.__height=height
    @property #2+ decorator for getter //데코레이터는 getter, setter를 사용하기 위함//
    def base(self):
        return self.__base
    @base.setter
    def base(self,value):
        self.__base = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height=value

#1+ zip을 사용하는 방법
def get_data():
    return 1,2,3

_,a,b=get_data() #첫번째를 무시

a=[1,2,3]
b=[11,22,33]
mylist=[*a,*b] #*는 병합을 의미한다.
print(mylist) #[1, 2, 3, 11, 22, 33]

c=['a','b']
z=zip(a,b)
print(list(z)) #[(1, 11), (2, 22), (3, 33)]
z=zip(a,b,c)
print(list(z))#[(1, 11, 'a'), (2, 22, 'b')]

