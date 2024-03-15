# import datetime
# from datetime import datetime as dt

# first_date=dt.strptime('2024-03-15', '%Y-%m-%d')#날짜를 나타낸 문자열을 뒤의 타입으로 바꿈
# print(first_date+ datetime.timedelta(days=100))# 100일 이후의 날짜를 출력

# try:
#     with open('c.csv') as f:
#         for line in f:
#             print(line)
# except Exception as e:
#     # pass
#     print(e)#자바의 try-catch와 같은 역할



import json

data={"name":"kim", "age":"23"}
print(data["age"], json.dumps(data), type(json.dumps(data)))
res_data=json.dumps(data)
print(type(json.loads(res_data)))
