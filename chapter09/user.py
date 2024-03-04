class User:
    def __init__(self, first, last):
        self.greet_user="Hello"
        self.first = first
        self.last = last
    def describe_user(self):
        print(f"{self.greet_user} My name is {self.first} {self.last}.")


intro=User("John","Smith")
intro.greet_user()