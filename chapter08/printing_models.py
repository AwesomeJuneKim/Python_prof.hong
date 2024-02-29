
#+2
def print_models(unprinted_designs, completed_models):
    
#남은게 없을 때까지 디자인을 출력한다.
#출력한 디자인을 Completed_models에 저장한다.
    while unprinted_designs:
        current_design=unprinted_designs.pop()#한개씩 삭제됨
        print(f"printing model:{current_design}")
        completed_models.append(current_design)
        print("\nmodels printed")
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
        
#2+위치 변경(맨 위에서 맨 아래로)
#출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def modify_string(s):
    s=s+"world"
    print(s)
    
st="hello"
modify_string(st)
print(st)
