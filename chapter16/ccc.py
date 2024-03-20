# from random import random
from random import randint
from matplotlib import pyplot as plt

# x=[1,2,3,4]
# y=[i**2 for i in x] #x대신 range(x)넣어서 에러
# print(y)
# plt.hist(x,y)
# plt.show()

# x=[randint(0,9)for _ in range(1000)]
# plt.hist(x)
# plt.show()

# x1=list(range(1,5))
# y1=[i*i for i in x1]
# x2=list(range(1,5))
# y2=[i**3 for i in x2]

# fig, axs=plt.subplots(1,2) #1행2열로 그래프를 그리고 싶을 때
# axs[0].plot(x1,y1, label="no.1", color="black")
# axs[1].plot(x1,y1, label="no.1", color="red")
# axs[0].plot(x2,y2, label="no.2", color="blue")
# axs[1].plot(x2,y2, label="no.2", color="yellow")
# plt.title("Random")
# plt.xlabel("X")
# plt.ylabel("Y")
# axs[0].legend()
# plt.show()
#----------------------------------------------------------------
import csv
import datetime as dt
from datetime import datetime

reader=csv.reader('./a.csv')
x1=[]#date
x2=[]
y1=[]#tMax
y2=[]#tMin

with open('a.csv', 'r') as file:
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        # print(row, type(row))
    #type함수로 어떤 타입인지 알고 접근한다.
        x1.append(datetime.strptime(row[2],'%Y-%m-%d'))
        #datetime은 모듈이 아닌 함수를 적용해야 함
        y1.append(int(row[4]))
        y2.append(int(row[5]))#row안에는 str데이터가 있으므로 int로 바꿔서 그래프를 만든다


plt.plot(x1,y1, label="Tmax", color="black")
plt.plot(x1,y2, label="Tmax", color="red")
plt.fill_between(x1,y1,y2, alpha=0.3)
plt.xticks(rotation=270)
plt.show()