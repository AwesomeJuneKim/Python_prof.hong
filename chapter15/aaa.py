import matplotlib.pyplot as plt
import seaborn as sns


x=list(range(1,101))
square=[i**2 for i in x]
# square=lambda x:[i**2 for i in x] ????????????

fig, ax=plt.subplots()
scatter=ax.scatter(x, square, c=square, cmap=plt.cm.Blues)
ax.set_title('Square', fontsize=30)
ax.set_xlabel('x line', fontsize=10)
ax.set_ylabel('y line', fontsize=10)
plt.colorbar
#아래는 3차원 시각화 도표에서 많이 쓰이는 방법(고저를 표현할 수 있다.)
plt.colorbar(scatter, ax=ax, label='Square')

# ax.set_xlime(0.20)
# ax.set_ylime(0.20)
ax.tick_params(labelsize=20)
sns.set_style('dark')
# for s in plt.style.available:
#     print(s)
ax.ticklabel_format(style='plain')
plt.savefig('colorbar.png')
plt.show()