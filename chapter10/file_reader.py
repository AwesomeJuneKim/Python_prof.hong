#파일읽기의 정석
# with open('name.txt', encoding='utf-8') as file:
#     for element in file.readlines():
#         print(element.rstrip())
        
# def add(a,b):
#     return a+b

# print(add(1,2))

# -------------------
#외부파일 임포트
# import csv
# with open('grade.csv') as file:
#     reader=csv.reader(file)
#     for line in reader:
#         print(line)

# lst=[1,2,3,3,4,4,5,5,5]
#next함수는 반복가능한 객체에 적용가능하다 리스트도 반복가능하지만 next함수에 적용할 수 없는 예외 이므로
#반복가능한 객체에 적용할 수 있게 iter함수로 변환 후 사용가능하다.
# r=iter(lst)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

import os
from pathlib import Path
#운영체계가 다른 여러 컴퓨터를 사용하여 코딩하는 경우 path에서 문제가 생긴다.
# path=Path('./a.txt')
# contents=path.read_text()
# print(contents)
# dir_path=Path('./a.txt')
# print(dir_path)
# file_path=Path('./aaa/b.txt')
# print(file_path.exists())

# print(os.path.isdir(file_path))

#p268
# path=Path('./aaa/aa.txt')
# with open(path,'w') as file:
#     file .write('aaa\n')
#     file .write('bbb\n')
#     file .write('bbb')

#교수님 추가
# path=Path('./aaa/aaa.txt')
#+ if path.exists():#파일이 없어도 에러가 뜨지 않게 함 방법1
#+ try: #try-except를 이용해서 에러를 뜨지 않게 함 방법2
# with open(path) as file:
#     for line in file:
#         print(line)
#+ except Exception as e:
#+    pass
# ----------------------------------------
#JSON언어로 파일에 저장하기
from pathlib import Path
import json
# numbers=[2,3,5,7,11,13]
# path=Path('number.json')
# contents=json.dumps(numbers)
#     dumps함수는 리스트를 json문자열로 변환 함
# path.write_text(contents)

#저장한 JSON파일을 읽어오기
path=Path('number.json')
contents=path.read_text()#contents가 이미 텍스트로 읽혔으므로 load를 이용해 파이썬 객체로 만들어야 함
numbers=json.loads(contents)
print(numbers)
