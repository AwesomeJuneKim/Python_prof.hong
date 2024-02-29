# def gugudan():
#     for i in range(2,10):
#         # print("=={}단".format(i))
#         for j in range(1,10):
#             print("{}x{}={}".format(i,j,i*j))
            
# if __name__=="__main__":
#     gugudan()


year= int(input())
year<=4000 and year>=1
if year%4==0 and (year%100!=0 or year%400==0):
    print("1")
else:
    print("0")
    