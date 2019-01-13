from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import stats
import xlwt 
from xlwt import Workbook 
   
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
data = pd.read_csv('call10.csv')
data_df_o=data.time_stamp
print(len(data_df_o))
sheet1.write(0, 0,"id")
sheet1.write(0, 1,"day")
sheet1.write(0, 2,"seconds")
sheet1.write(0, 3,"tower_id")
wb.save('example.xls')
for i in range (len(data_df_o)):
    d=int(data_df_o[i].split()[0].split('-')[2])
    h=int(data_df_o[i].split()[1].split(':')[0])
    if(h==0):
        h=24
    m=int(data_df_o[i].split()[1].split(':')[1])
    t=h*60+m
    sheet1.write(i+1, 0,int(data.id[i]))
    sheet1.write(i+1, 1,d)
    sheet1.write(i+1, 2,t)
    sheet1.write(i+1, 3,int(data.tower_id[i]))
    wb.save('example.xls') 
