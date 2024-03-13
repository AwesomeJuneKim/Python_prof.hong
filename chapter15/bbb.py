import matplotlib.pyplot as plt
import random

# x=list(range(100))
# y=list(range(100,200))

x=[random.randint(0,10) for _ in range(100)]
y=[random.randint(10,20) for _ in range(100)]

x_walks=[5,-5]
y_walks=[5,-5]
x_data, y_data=[],[]
x,y=0,0
x_data.append(x)
y_data.append(y)
for x_move,y_move in zip(x_walks, y_walks):
    x,y=x_move,y_move
    x_data.append(x)
    y_data.append(y)
    print(x,y)

# print(x, y)
fig, ax=plt.subplots()
# ax.plot(x[:50],y[:50], color='red')
# ax.plot(x[50:],y[50:], color='green')
ax.plot(x_data,y_data)
plt.show()