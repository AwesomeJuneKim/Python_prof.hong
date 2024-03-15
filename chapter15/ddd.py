import matplotlib.pyplot as plt


fig, ax = plt.subplots()


# x=[50,70,20]
# y=[30,50,70]
# ax.scatter(x,y)
# for i, txt in enumerate(['HONG', 'LEE', 'KANG']):
#     ax.text(x[i], y[i], txt)

# ax.set_xlabel('Korean')
# ax.set_ylabel('English')
# plt.legend()
# plt.show()

#한 이름당 두개의 막대그래프를 그리고 싶었음-미완성
hong=[50,30]
lee=[70,50]
kang=[20,70]

x=['korean','english']
names=['Hong', 'Lee', 'Kang']

fig, ax = plt.subplots()
for i, scores in enumerate(zip(hong,lee,kang)):
    ax.bar(x, scores, label=names[i])
ax.set_xlabel('score')
ax.set_ylabel('name')
plt.legend()
plt.show()