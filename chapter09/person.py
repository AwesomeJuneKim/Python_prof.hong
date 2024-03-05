class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.weight=50
        self.__vision=1.0
    def __str__(self):#스트링을 만들어주는 함수(객체를 출력하려면 스트링으로 만들어야 함)
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    def show_person_vision(self):
        print(f"This person's vision is {self.__vision}")

new_person=Person("Kim","20","Kim's house")
print("This person's name is",new_person.name, "and he is ",new_person.age, " years old.")
print(f"This person weighs {new_person.weight} kg")

new_person.show_person_vision()

print(str(new_person))
print(new_person.__str__())
#-> 두 코드의 차이점은 없다. 방식만 다름
print(new_person)
#->__str__은 자동호출 되기 때문에 메서드를 호출할 필요가 없어서 코드가 간단해 진다.

my_list=[1,2,3,4]
print(my_list)