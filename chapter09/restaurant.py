class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def describe_restaurant(self):
        print(f"\nThis {self.name} restaurant is {self.type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.name} is now open!\n")

restaurant=Restaurant("Hankook","Korean")
restaurant2=Restaurant("Burger King","American")
restaurant3=Restaurant("BanJeom","Chinese")
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant.open_restaurant()

