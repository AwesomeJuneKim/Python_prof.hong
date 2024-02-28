#백준 사칙연산
# a=int(input("a:"))
# b=int(input("b:"))

# total=a+b
# print("c: ",total)

# a,b=input().split()
# a,b=int(a), int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(a+b,a-b,a*b,a//b,a%b, sep="\n")



# b=len(input())
# print(b)


#리스트 출력해보기
# a=[1,2,3,4]
# a.insert(-1,"orange")
# print(a[::-1],a[:2])

# for i in 'asdf':
#     print(i)
    
# for i in "asdf":
#     print(i)
    
# for i in range(1,10):
#     print(i)
    
# for i in (1,2,3,4,5):
#     print(i)
    
# d={1:'a',2:'b',3:'c',4:'d'}
# print(d)
# #keyValue
# for i in d:
#     print(i) #key만 출력된다.


#짝수 홀수 출력
# for i in range(1,6):
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")

#백준 두 수 비교하기
# a,b=input().split()
# a,b=int(a), int(b)
# if a-b<0:
#     print('<')
# elif a-b>0:
#     print('>')
# else:
#     print('==')
    
#백준 시험성적
a=input()
a=int(a)
if a>=90 and a<=100:
    print('A')
elif a>=80 and a<=89:
    print('B')
elif a>=70 and a<=79:
    print('C')
elif a>=60 and a<=69:
    print('D')
else:
    print('F')