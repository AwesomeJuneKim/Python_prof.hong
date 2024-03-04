class User:
    def __init__(self, first, last):
        self.greet_user="Hello"
        self.first = first.title()
        self.last = last.title()
    def describe_user(self):
        print(f"{self.greet_user}! My name is {self.first} {self.last}.")


intro=User("john","smith")
intro.describe_user()