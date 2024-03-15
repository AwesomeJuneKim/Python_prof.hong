import random

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# x = [i * 2 for i in range(4)]
# plt.plot(x, y)
# plt.scatter(x, y)


x = [random.randint(0, 9) for _ in range(10)]
y = [i ** 2 for i in x]
x1 = [i * 3 for i in range(10)]
y1=[i ** 2 for i in x1]
# plt.hist(x)


fig, ax = plt.subplots()
ax.scatter(x,y, label="scatter", color="orange")
ax.plot(x1,y1, label="plot", color="black", linestyle='dashdot')
ax.scatter(x1,y1, color='red')
# ax.scatter(x,y)
ax.set_title('Matplotlib')
ax.set_xlabel('x1')
ax.set_ylabel('y1')
# ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.xaxis.set_major_locator(MultipleLocator(1))
plt.legend()#위의 레이블을 나타나게 함
plt.show()

