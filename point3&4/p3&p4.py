
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import stats
from sklearn.cluster import DBSCAN
from matplotlib import pyplot
x = []
places = {}
visited = {}
temp = {}
temp2 = {}
common = 0
groups={}
color=["r","g","b","k","c","m","y"]
tower_data = pd.read_csv('towers.csv')
user_data = pd.read_csv('output2.csv')
for i in range(len(tower_data)) :
    x.append([tower_data.x[i] , tower_data.y[i]])
clustering = DBSCAN(eps=1600, min_samples=1).fit(x)
result = clustering.labels_


for i in range(1,len(result)) :
    if str(result[i]) not in places :
        places[str(result[i])] = [tower_data.ID[i]]
        groups[str(result[i])] = []
    else:
        places[str(result[i])].append(tower_data.ID[i])
        
for i in range(len(user_data.tower_id)) :
    for j in places :
        if str(user_data.tower_id[i]) in j :
            if j in visited :
                if  str(user_data.id[i]) not in temp :
                    temp[str(user_data.id[i])] = [user_data.day [i]]
                    visited[j] = visited[j] + 1
                    groups[j].append(user_data.id[i])
                elif user_data.day[i] not in temp[str(user_data.id[i])] :
                    temp[str(user_data.id[i])].append(user_data.day[i])
                    visited[j] = visited[j] + 1
            else :
                visited[j] = 1
                groups[j].append(user_data.id[i])
                

{int(key):visited[key] for key in visited}
#plt.scatter(visited.keys(),visited.values())
plt.figure(figsize=(11,7), dpi=80)
pyplot.plot(visited.keys(), visited.values())
plt.xlabel("places")
plt.ylabel("visiting frequency")
plt.show()


j=0

plt.figure(figsize=(11,7), dpi=80)
plt.xlabel("places")
plt.ylabel("users")
for k, v in groups.items():
    for i in range (len(v)):
        plt.scatter(int(k),v[i],c=color[j])
    j+=1
    if(j==len(color)):
        j=0

#plt.scatter(groups.keys(),groups.values())

#pyplot.plot(groups.keys(), groups.values())


for i in range(len(user_data.id)) :
    for j in places :
        if str(user_data.tower_id[i]) in j :
            if str(user_data.id[i]) in temp2 :
                if j not in temp2[str(user_data.id[i])] :
                    temp2[str(user_data.id[i])].append(j) 
                    common = common + 1
            else :
                temp2[str(user_data.id[i])] = [j]
                common = common + 1


average = common / 260 
print ("The common number of visited places" , int(average))
