def get_formatted_name(first_name, last_name):
    """실제이름 형식"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your full name")
    print("Enter 'q'at anytime to quit")
    
    f_name=input("first name: ")
    if f_name=='q':
        break
    l_name=input("last name: ")
    if l_name=='q':
        break
    
    formatted_name=get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}!")

musician = get_formatted_name('jimi', 'hexdrix')
print(musician)


#미들네임이 존재하는 경우
def get_formatted_name(first_name, last_name, middle_name=''):
    """실제이름 형식"""
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hexdrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
#파이썬은 비어있지 않은 문자열을 true로 간주한다
#middle_name=''은 옵션이 된다.
