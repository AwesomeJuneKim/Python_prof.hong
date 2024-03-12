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
# a=input()
# a=int(a)
# if a>=90 and a<=100:
#     print('A')
# elif a>=80 and a<=89:
#     print('B')
# elif a>=70 and a<=79:
#     print('C')
# elif a>=60 and a<=69:
#     print('D')
# else:
#     print('F')
    
#백준 구구단
# a=input()
# a=int(a)
# for j in range(1,10):
#     print(f"{a} * {j} = {a*j}")

#백준 합산하기
# n=input()
# n=int(n)
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)

#교수님 설명
# def input2():
#     return '1 2'
# print(input2)

# s= input()
# a,b= s.split()
# a,b= int(a), int(b)
# #a,b= int('a'), int('b') #value error int안에 문자를 넣을 수 없다
# print(a,b)

#백준 별찍기
# N=input()
# N=int(N)
# for i in range(1,N+1):
#     print('*'*i)
    
#백준 별찍기reverse
# N=input()
# N=int(N)
# for i in range(1,N+1):
#     print(' '*(N-i)+'*'*i)
    
#백준 개수 세기-미완
# N=input().split()
# print(N, len(N))

#최대 최소-미완
# N=int(input())
# lst=list(map(int, input().split()))
# print(lst)
# print(max(lst), min(lst))

#백준 연습
# a=int(input())
# str=""
# if(4<=a<=1000 and a%4==0):
#     for i in range(1,int(a/4)+1):
#         str +="long "
#     str +="int"
#     print(str)

#백준 10818
# N=int(input())
# v=list(map(int, input().split()))
# print(min(v), max(v))

#백준 2562
# nbr=[int(input()) for _ in range(3)]
# print(max(nbr))
# print(nbr.index(max(nbr))+1)

#백준5597-미완
student= [i for i in range(1,31)]
stn=[int(input()) for _ in range(28)]
student.remove(stn)
print(min(student))
print(max(student))