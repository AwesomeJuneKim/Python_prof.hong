class User:
    def __init__(self, first, last):
        self.greet_user="Hello"
        self.first = first.title()
        self.last = last.title()
    def describe_user(self):
        print(f"{self.greet_user}! My name is {self.first} {self.last}.")


# intro=User("john","smith")
# intro.describe_user()

#연습문제 9-7 관리자
class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges=Privileges()

#연습문제 9-8 권한
class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = ['can delete post','can add post','can ban user']
    def show_privileges(self):
        print(f"Administrator {self.privileges[0]}, {self.privileges[1]} and {self.privileges[2]}.")
# new_admin=Privileges()
# new_admin.show_privileges()