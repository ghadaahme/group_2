#!/usr/bin/env python
# coding: utf-8

# In[1]:



from datetime import datetime
import pandas as pd
import numpy
import numpy as np
import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

from scipy import stats
import numpy as np
import pandas as pd
user_data = pd.read_csv('output1.csv')
f=[]
n=1
arr=[]
ind=[]
ind2=[]
for i in range (len(user_data)):
    if(user_data.id[i]==n):
        arr.append(user_data.seconds[i]) 
        ind.append(i) 
        if i == len(user_data)-1 :
            elements = numpy.array(arr)
            mean = numpy.mean(elements, axis=0)
            sd = numpy.std(elements, axis=0)
            ind1=[]
            ff=[]
            for x in range (len(arr)):
                if (arr[x] > mean - 1.5 * sd):
                    f.append(arr[x])
                    ind1.append(ind[x])
            for x in range (len(f)):
                if (f[x] < mean + 1.5 * sd):
                    ff.append(f[x])
                    ind2.append(ind1[x])
    else:
        n+=1
        elements = numpy.array(arr)
        mean = numpy.mean(elements, axis=0)
        sd = numpy.std(elements, axis=0)
        ind1=[]
        
        ff=[]
        for x in range (len(arr)):
            if (arr[x] > mean - 1.5 * sd):
                f.append(arr[x])
                ind1.append(ind[x])
              
        for x in range (len(f)):
            if (f[x] < mean + 1.5 * sd):
                ff.append(f[x])
                ind2.append(ind1[x])
        ind=[]
        ind1=[]
        arr=[]
        f=[]
        ff=[]
        i=i-1
    
      
    
print(len(ind2))
for count in range (len(ind2)):
    sheet1.write(count, 0,int(user_data.id[ind2[count]] ))
    sheet1.write(count, 1,int(user_data.day[ind2[count]]) )
    sheet1.write(count, 2,int(user_data.seconds[ind2[count]]) )
    sheet1.write(count, 3,int(user_data.tower_id[ind2[count]])  )
    wb.save('output2.xls')
    


# In[ ]:




