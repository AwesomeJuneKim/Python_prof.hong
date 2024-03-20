import requests
u='https://api.github.com/search/repositories?q=language:python+sort:stars'
import json
from matplotlib import pyplot as plt

# res=requests.get(u)
# print(type(res.json()))
# print(res.json())
nm=[]
st=[]
with open('repositories.json','r',encoding='utf-8') as f:
    res=json.load(f)
    for items in res['items']:
        nm.append(items['name'])
        st.append(items['stargazers_count'])
print(st)
print(nm)
plt.bar(nm,st)
plt.xticks(rotation=45)
plt.show()