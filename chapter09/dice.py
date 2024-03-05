from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1,self.sides)

dice=Die()
print("6면체 주사위: ")
for i in range(10):
    print(dice.roll_die())

dice10=Die(sides=10)
print("10면체 주사위:")
for i in range(10):
    print(dice10.roll_die())