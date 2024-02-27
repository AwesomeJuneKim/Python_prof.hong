def greet_user(username):
    """인사말을 출력합니다."""
    print(f"Hello, {username.title()}!")
    
greet_user('anna')

#아래는 함수 외부에서 변수를 변경했음
username='june'
username=greet_user(username)

# help(greet_user)
# print(greet_user.__doc__)