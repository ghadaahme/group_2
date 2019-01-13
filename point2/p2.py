
import pandas as pd
from pandas import merge
import numpy as np
import matplotlib.pyplot as plt
import datetime 
from mpl_toolkits import mplot3d
from sklearn.cluster import KMeans
import xlwt 
from xlwt import Workbook
import matplotlib.dates as dates
import openpyxl
from openpyxl import load_workbook

import operator
from operator import itemgetter, attrgetter
#from prettytable import PrettyTable
#source venv/bin/activate




data = pd.read_csv('output2.csv')
data2 = pd.read_csv('towers.csv')
#combine=merge(data,data2,on='tower_id')


#combine = pd.DataFrame(np.sort(combine.values, axis=0), index=combine.index, columns=combine.columns)
# Workbook is created 
wb = Workbook() 
# add_sheet is used to create sheet. 
temp = wb.add_sheet('sheet1')
n=1
j=0
y=[]
f1=[]
f2=[]
f3=[]

output={}
#print(type(combine.seconds[0]))
for i in range (len(data)):
        sumx1=0
        sumy1=0
        count1=0
        sumx2=0
        sumy2=0
        count2=0
        if (data.id[i] == n):
            t=data.tower_id[i]
            f1.append(int(data.seconds[i]))
            f2.append(data2.Y_coordinate[t])
            f3.append(data2.X_coordinate[t])
        else :
            x = np.array(list(zip(f1,f2,f3)))
            kmeans = KMeans(n_clusters=2)
            kmeans = kmeans.fit(x)
            labels = kmeans.predict(x)
            L=labels[0]
            h=f1[0]/60
            if(h>=18 or h<=6):
                for i in range (len(labels)):
                    if (labels[i]==L):
                        #home
                        sumx1+=f3[i]
                        sumy1+=f2[i]
                        count1+=1
                    else :
                        #work
                        sumx2+=f3[i]
                        sumy2+=f2[i]
                        count2+=1
            else:
                for i in range (len(labels)):
                    if (labels[i]==L):
                        #work
                        sumx2+=f3[i]
                        sumy2+=f2[i]
                        count2+=1
                    else :
                        #home
                        sumx1+=f3[i]
                        sumy1+=f2[i]
                        count1+=1
            homepx=sumx1/count1
            homepy=sumy1/count1
            workpx=sumx2/count2
            workpy=sumy2/count2
            output[str(n)]=[[homepx,homepy],[workpx,workpy]]
            n+=1
            f1=[]
            f2=[]
            f3=[]
            t=data.tower_id[i]
            f1.append(int(data.seconds[i]))
            f2.append(data2.Y_coordinate[t])
            f3.append(data2.X_coordinate[t])



print('**************************************************************************************************')

print('*','User_Id','\t','Home_Position',5*'\t','Work_Position',10*'\t','*')
print('*********************************************************************************************')
for keys in range(1,len(output)-100):
    user=[]
    user=output[str(keys)]
    print('*',keys,'\t','|',user[0],'\t','|',user[1],'*')
    print('*','-------------------------------------------------------------------------------------','*')


    

            
            #temp.write(0,0,homepx)
#temp.write(1,0,workpy)
#wb.save('temp.xls')

#print(workpx)
#print(workpy)

#print(homepx)
#print(homepy)
    
'''
data3 = pd.read_csv('calls_10.csv')
datetime_object=[]
for i in range (len(data3.time_stamp)) :
    datetime_object.append(datetime.datetime.strptime(data3.time_stamp[i],'%Y-%m-%d %X'))
fig = plt.figure()
ax = plt.axes(projection='3d')
zdata = data3.tower_id
xdata = data3.id
ydata = dates.date2num(datetime_object)

ax.scatter3D(xdata, ydata, zdata, c=zdata,cmap='viridis', linewidth=0.5)
plt.xlim([0,260])
plt.ylim([dates.date2num(datetime.datetime(2013, 1, 9, 0, 0)),dates.date2num(datetime.datetime(2013, 1, 24, 23, 59))])
ax.set_xlabel('human_id')
ax.set_ylabel('time')
ax.set_zlabel('tower_id')

plt.show()
'''
#28064.369325,291742.390825


# In[ ]:





# In[ ]:





# In[ ]:




