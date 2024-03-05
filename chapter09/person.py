class List:
    def __init__(self,mylist):
        self.mylist=mylist
        
    def __len__(self):
        return len(self.mylist)
my_list= [1,2,3,4]
print(len(my_list))

class Person:
    count=0 #7+ 클래스 변수
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.weight=[65,70,75,80]
        self.__vision=1.0
        self.height=1.7
        Person.count +=1# 7+ 클래스변수를 인스턴스에 사용하기 위해서는 클래스이름을 적어줘야 함
    # @classmethod #decorator역할 자바의 어노테이션
    
    def __str__(self):#스트링을 만들어주는 함수(객체를 출력하려면 스트링으로 만들어야 함)
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    def show_person_vision(self):
        print(f"This person's vision is {self.__vision}")

    def __eq__(self, other): # 4+ 비교 메서드
        return self.age==other.age
    
    # def __call__(self):
    #     return self.weight/(self.height**2)

    def __getitem__(self, index):
        return self.weight[index] #5+ 인덱스로 값 출력하기
    
    # def __del__(self):
    #     print("객체{}이 소멸됨".format(self.name))#6 삭제하는 메서드->쓸일이 없다. 자바의 가비지컬렉터와 같음(자동으로 삭제함)
    
    def printing(cls):
        print("객체의 수는 {}".format(cls.count))

new_person=Person("Kim","20","Kim's house")
print("This person's name is",new_person.name, "and he is ",new_person.age, " years old.")
print(f"This person weighs {new_person.weight} kg")
other_person=Person("Lee","18","Lee's house")# 4+ 다른사람 정보 추가

new_person.show_person_vision()

print(str(new_person))
print(new_person.__str__())
#-> 두 코드의 차이점은 없다. 방식만 다름
print(new_person)
#->__str__은 자동호출 되기 때문에 메서드를 호출할 필요가 없어서 코드가 간단해 진다.

print(new_person==other_person)#4+ 두사람의 나이가 같은지 비교하고 true false로 결과를 출력한다.

# print(new_person.__call__())
# person=Person("John", 30, "123 Main St", weight=70, height=1.8)
# print(person())

print(f"현재 체중은 {new_person[2]} 입니다.")#5

# ps=Person("John", 30, "123 Main St")
# print(ps)
# del ps
#6+ John은 생성 후 del메서드로 직접 삭제한것이고 위에 생성된 Kim와 Lee는 가비지컬렉터가 삭제한다.

print("객체의 타입은 {}".format(isinstance(new_person,Person)))
#????????????????
print(f"person 객체의 나이는**{new_person.age:5}**")
#나이를 5칸안에 출력해라(나이를 출력하고 나머지는 블랭크)
print(f"{Person.count}객체가 생성됨")
print(f"{other_person.count}객체가 생성됨")
#7+ count를 공유함
# Person.printing()
new_person.printing()