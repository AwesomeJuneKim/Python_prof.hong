class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def describe_restaurant(self):
        print(f"This {self.name} restaurant is {self.type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant=Restaurant("Hankook","Korean")
restaurant.describe_restaurant()
restaurant.open_restaurant()