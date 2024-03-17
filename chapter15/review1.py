import matplotlib.pyplot as plt
import random


# random.randint(1,100)
# x=[random.randint(2,11) for _ in range(10)]
# y=[i**2 for i in x]

fig, ax= plt.subplots()

# ax.hist(x, bins=5)
# plt.show()

data={
'hong':[70,50],
'lee':[50,90],
'kang':[45,85]
}

name=list(data.keys())
scoreK=[score[0] for score in data.values()]
scoreE=[score[1] for score in data.values()]

all_scores=scoreK+scoreE

for i, score in enumerate(all_scores):
    ax.bar([x+i for x in range(len(name))],score, label=f'Score{i+1}')

plt.show()
