calc=0.3+0.4
print(calc)

universe_age=14_000_000_000
print(universe_age)

bicycles=['trek','canondale','specialized']
print(bicycles)
print(bicycles[-1])
bicycles.append('bianche')#꼬리에 추가
print(bicycles)
bicycles.insert(0,'samcheonri')#0번째 배열에 추가
del bicycles[-2]#뒤에서 두번째 삭제
print(bicycles)
bicycles.pop()
print(bicycles)

meaasge=f"bicycle was a {bicycles[0].title()}.!!!"
print(meaasge)