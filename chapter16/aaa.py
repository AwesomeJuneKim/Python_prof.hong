# with open('a.csv') as f:
#     for line in f:
#         print(line.rstrip().split(','))

from pathlib import Path
import matplotlib.pyplot as plt
import csv
x1=[]
y1=[]
x2=[]
y2=[]
COL_DATE = 2
T_MAX = 4

# with open(Path('data','a.csv')) as f:
with open('a.csv') as f:
    reader=csv.reader(f)
    header=next(reader)#header가 빠지고 출력되게 함
    for line in reader:
        # print(line)
        x1.append(line[COL_DATE])
        y1.append(line[T_MAX])
        x2.append(line[2])
        y2.append(line[5])
# print(f'x1: {x1}')
# print(f'y1: {y1}')
# print(f'x2: {x2}')
# print(f'y2: {y2}')

plt.plot(x1,y1, label='Tmax')
plt.plot(x2,y2, label='Tmin')
plt.fill_between(x1,y1,y2, color='red', alpha=0.3)
plt.xticks(rotation=90)
plt.legend()
plt.show()

for idx, h in enumerate(header):
    print(idx, h)