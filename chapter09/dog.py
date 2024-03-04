class Dog:
    def __init__(self, name, age):#->자바 클래스의 필드로 생각하면 된다.
        self.name = name
        self.age = age
        self.__price=100 #비공개 속성이므로 클래스 외부에서 접근할 수 없다.

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog=Dog('Willie',6)#생성자 호출->인스턴스 생성->__init__()함수가 자동 호출
my_dog.sit()

print(f"My dog's name is {my_dog.name} {my_dog._Dog__price}.")
#my_dog.__price는 비공개 속성->에러->_class명을 비공개속성 앞에 붙이면 클래스 외부에서 사용가능

your_dog=Dog('Lucy', 3)
your_dog.sit()
print(f"your dog's name is {your_dog.name}.")