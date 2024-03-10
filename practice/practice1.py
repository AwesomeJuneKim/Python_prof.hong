# def gugudan():
#     for i in range(2,10):
#         # print("=={}단".format(i))
#         for j in range(1,10):
#             print("{}x{}={}".format(i,j,i*j))
            
# if __name__=="__main__":
#     gugudan()

#백준예제 윤달
# year= int(input())
# if year<=4000 and year>=1:
#     if year%4==0 and (year%100!=0 or year%400==0):
#         print("1")
#     else:
#         print("0")
        

#백준예제-미완10950-완료
# T=int(input())
# for i in range(T):
#     a,b=map(int, input().split())
#     print(a+b)

#백준예제 1000미완
# A=input()
# B=input()
# print(int(A)+int(B))

#백준예제 14681
# x=int(input())
# y=int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)

# 백준예제 25314
# 입력값을 4로 나눈 몫의 갯수만큼 long을 적어준다
# N=int(input())
# string=""
# if(4<=N<=1000 and N%4==0):
#     for i in range(1,int(N/4)+1):
#         string +="long "
#     string +="int"
#     print(string)

#백준 11021
# T=int(input())
# for i in range(1,T+1):
#     a,b=map(int, input().split())
#     print(f'Case #{i}: {a+b}')

#백준 10951 입력이 끝날때 까지 덧셈을 계속하는 코드
#나는 try except를 사용하지 않아서 에러 났음
# while True:
#     try:
#         a,b=map(int, input().split())
#         print(a+b)
#     except:
#         break

#백준 10807-미완
# N개 만큼의 정수를 입력한다??
# N개의 정수가 생성되고 리스트에 넣는다. 그 리스트 안에 해당정수가 몇개 있는지 확인한다.
# N=int(input())
# NList=map(int, input().split())
# print(NList.count(N))

# data=[]
# for _ in range(10):
#     data.append(int(input()%42))
# print(data)

# print(set([1,1,1]))

# answer=[]
# for d  in answer:
#     if d not in answer:
#         answer.append(d)
# print(len(answer))

#백준 10871
# A=list(int(map(int, input().split())))

#백준 27866
S=input()
i=int(input())
print(S[i-1])

#백준 9086
T=int(input())
for i in range(T):
    a=input()
    print(a[0]+a[-1])

#백준 11654
a=input()
print(ord(a))