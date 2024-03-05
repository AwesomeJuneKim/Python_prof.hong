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

class IceCreamStand(Restaurant):
    def __init__(self,name,type,flavors):
        super().__init__(name,type)
        self.flavors=flavors
    def describe_iceStand(self):
        print(f"\nThis {self.name} shop sells {self.flavors} ice creams.")
        

my_icecream=IceCreamStand("Iceman",'',"vanilla")
my_icecream.describe_iceStand()

