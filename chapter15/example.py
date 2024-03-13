import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()  # Create a figure containing a single axes.

random.randint(0,100)
x1=[1, 2, 3, 4]
y1=[2, 3, 4, 6]
#ax.plot(x1,y1, label="blue")
ax.set_aspect('equal')  # Plot some data on the axes.
ax.scatter(x1,y1, label="blue")

x2=[1,2,3,4]
y2=[1,2,3,4]
#ax.plot(x2,y2, label="red")
ax.scatter(x2,y2, label="red")


ax.set_title('Plot A and B')
ax.set_aspect('equal')
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.legend()
plt.savefig('example.png')
plt.show()