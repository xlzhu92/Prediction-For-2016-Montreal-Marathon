'''
Created on Sep 18, 2016

@author: Xiliang Zhu
'''

import csv
import copy
import numpy as np


with open('Project1_data.csv')as datafile:
    reader = csv.reader(datafile)
    rawdata = []    
    for row in reader:
        rawdata.append(row)
rawdata.pop(0)

dateset = ['2015-09-20','2014-09-28','2013-09-22','2012-09-23']

data = copy.deepcopy(rawdata) #extract data for montreal events '12 to '15
for racer in data:
    i = 1
    while i < len(racer):
        if racer[i] in dateset and racer[i+2] == 'Marathon':
            i += 5            
        else:
            del racer[i:i+5]
xset = np.zeros(shape=(len(data),6),dtype=int) #14,13,12
yset = np.zeros(shape=(len(data),1),dtype=int) #15

i = 0 #count y set
for racer in data:
    if '2015-09-20' in racer:
        yset[i] = 1
    i += 1

r = 0 #count x set, features as '14+13,'14+12, '13+12
for racer in data:
    if '2014-09-28' in racer:
        xset[r][0] += 1
        if '2013-09-22' in racer:
            xset[r][0] += 1
    if '2014-09-28' in racer:
        xset[r][1] += 1
        if '2012-09-23' in racer:
            xset[r][1] += 1
    if '2012-09-23' in racer:
        xset[r][2] += 1
        if '2013-09-22' in racer:
            xset[r][2] += 1
    r += 1
#add sum as feature
for row in xset:
    row[3] = sum(row)
     
#add gender as feature
for i in range(len(data)):
    if len(data[i]) < 5:
        xset[i][4] = 0
    elif 'M' in data[i][5]:
        xset[i][4] = 1
    elif 'F' in data[i][5]:
        xset[i][4] = -1
    else:
        xset[i][4] = 0
#add age as feature   
for i in range(len(data)):
    if len(data[i]) < 5:
        xset[i][5] = 0
    elif data[i][5][1:3].isdigit() == True:
        xset[i][5] = int(data[i][5][1:3]) - 2
    else:
        xset[i][5] = 0

# compute all the probabilities needed for naive bayes
def quantizer(xset):
    for racer in xset:
        if 0 <= racer[5] < 10:
            racer[5] = 0
        elif 10 <= racer[5] < 20:
            racer[5] = 10
        elif 20 <= racer[5] < 30:
            racer[5] = 20
        elif 30 <= racer[5] < 40:
            racer[5] = 30
        elif 40 <= racer[5] < 50:
            racer[5] = 40
        elif 50 <= racer[5] < 60:
            racer[5] = 50
        else:
            racer[5] = 60
    return xset

xset = quantizer(xset)
xset.astype(int)

def countprob_y(yset,y):
    count = 0    
    for i in yset:
        if i == y:
            count += 1
    return float(count)/len(yset)

def countprob_x_02(xset,yset,y,k):
    res=[]
    count_0,count_1,count_2 = 0,0,0
    for i in range(len(xset)):
        if yset[i] == y and xset[i][k] == 0:
            count_0 += 1
        elif yset[i] == y and xset[i][k] == 1:
            count_1 += 1
        elif yset[i] == y and xset[i][k] == 2:
            count_2 += 1
    count_y = 0    
    for i in yset:
        if i == y:
            count_y += 1
    res = [float(count_0)/count_y,float(count_1)/count_y,float(count_2)/count_y]
    return res
        
def countprob_x_3(xset,yset,y):
    res = []
    count_0,count_1,count_2,count_3,count_4,count_5,count_6 = 0,0,0,0,0,0,0
    count_y = 0    
    for i in yset:
        if i == y:
            count_y += 1
    for i in range(len(xset)):
        if yset[i] == y and xset[i][3] == 0:
            count_0 += 1
        elif yset[i] == y and xset[i][3] == 1:
            count_1 += 1
        elif yset[i] == y and xset[i][3] == 2:
            count_2 += 1
        elif yset[i] == y and xset[i][3] == 3:
            count_3 += 1
        elif yset[i] == y and xset[i][3] == 4:
            count_4 += 1
        elif yset[i] == y and xset[i][3] == 5:
            count_5 += 1
        elif yset[i] == y and xset[i][3] == 6:
            count_6 += 1
    res = [float(count_0)/count_y,float(count_1)/count_y,float(count_2)/count_y,float(count_3)/count_y,float(count_4)/count_y,float(count_5)/count_y,float(count_6)/count_y] 
    return res

def countprob_x_4(xset,yset,y):
    count_y = 0    
    for i in yset:
        if i == y:
            count_y += 1
    count_0,count_1,count_m1 = 0,0,0
    for i in range(len(xset)):
        if yset[i] == y and xset[i][4] == 0:
            count_0 += 1
        elif yset[i] == y and xset[i][4] == 1:
            count_1 += 1
        elif yset[i] == y and xset[i][4] == -1:
            count_m1 += 1
    res = [float(count_0)/count_y,float(count_1)/count_y,float(count_m1)/count_y]
    return res

def countprob_x_5(xset,yset,y):
    count_y = 0    
    for i in yset:
        if i == y:
            count_y += 1
    count_0,count_1,count_2,count_3,count_4,count_5,count_6 = 0,0,0,0,0,0,0
    for i in range(len(xset)):
        if yset[i] == y and xset[i][5] == 0:
            count_0 += 1
        elif yset[i] == y and xset[i][5] == 10:
            count_1 += 1
        elif yset[i] == y and xset[i][5] == 20:
            count_2 += 1
        elif yset[i] == y and xset[i][5] == 30:
            count_3 += 1
        elif yset[i] == y and xset[i][5] == 40:
            count_4 += 1
        elif yset[i] == y and xset[i][5] == 50:
            count_5 += 1
        elif yset[i] == y and xset[i][5] == 60:
            count_6 += 1
    res = [float(count_0)/count_y,float(count_1)/count_y,float(count_2)/count_y,float(count_3)/count_y,float(count_4)/count_y,float(count_5)/count_y,float(count_6)/count_y] 
    return res

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(xset , yset, test_size=0.2, random_state=42)

def probset(xset,yset,y):
    return [countprob_x_02(xset,yset,y,0),countprob_x_02(xset,yset,y,1),countprob_x_02(xset,yset,y,2),countprob_x_3(xset,yset,y),countprob_x_4(xset,yset,y),countprob_x_5(xset,yset,y)]

train_probset_1 = probset(x_train,y_train,1)
train_probset_0 = probset(x_train,y_train,0)
train_dict_1 = [{'0':train_probset_1[0][0],'1':train_probset_1[0][1],'2':train_probset_1[0][2]},{'0':train_probset_1[1][0],'1':train_probset_1[1][1],'2':train_probset_1[1][2]},{'0':train_probset_1[2][0],'1':train_probset_1[2][1],'2':train_probset_1[2][2]},{'0':train_probset_1[3][0],'1':train_probset_1[3][1],'2':train_probset_1[3][2],'3':train_probset_1[3][3],'4':train_probset_1[3][4],'5':train_probset_1[3][5],'6':train_probset_1[3][6]},{'0':train_probset_1[4][0],'1':train_probset_1[4][1],'-1':train_probset_1[4][2]},{'0':train_probset_1[5][0],'10':train_probset_1[5][1],'20':train_probset_1[5][2],'30':train_probset_1[5][3],'40':train_probset_1[5][4],'50':train_probset_1[5][5],'60':train_probset_1[5][6]}]
train_dict_0 = [{'0':train_probset_0[0][0],'1':train_probset_0[0][1],'2':train_probset_0[0][2]},{'0':train_probset_0[1][0],'1':train_probset_0[1][1],'2':train_probset_0[1][2]},{'0':train_probset_0[2][0],'1':train_probset_0[2][1],'2':train_probset_0[2][2]},{'0':train_probset_0[3][0],'1':train_probset_0[3][1],'2':train_probset_0[3][2],'3':train_probset_0[3][3],'4':train_probset_0[3][4],'5':train_probset_0[3][5],'6':train_probset_0[3][6]},{'0':train_probset_0[4][0],'1':train_probset_0[4][1],'-1':train_probset_0[4][2]},{'0':train_probset_0[5][0],'10':train_probset_0[5][1],'20':train_probset_0[5][2],'30':train_probset_0[5][3],'40':train_probset_0[5][4],'50':train_probset_0[5][5],'60':train_probset_0[5][6]}]
y_train_1 = float(np.count_nonzero(y_train))/len(y_train)
y_train_0 = 1 - y_train_1    

def fitprob(xrow):
    xrow = map(str,xrow)
    p1 = y_train_1*train_dict_1[0][xrow[0]]*train_dict_1[1][xrow[1]]*train_dict_1[2][xrow[2]]*train_dict_1[3][xrow[3]]*train_dict_1[4][xrow[4]]*train_dict_1[5][xrow[5]]
    p0 = y_train_0*train_dict_0[0][xrow[0]]*train_dict_0[1][xrow[1]]*train_dict_0[2][xrow[2]]*train_dict_0[3][xrow[3]]*train_dict_0[4][xrow[4]]*train_dict_0[5][xrow[5]]
    ratio = p1/p0
    if ratio >= 1:
        return 1
    else:
        return 0

def gety(x):
    y = []
    for i in range(len(x)):
        a = fitprob(x[i])
        y.append(a)
    return y

y_predict_train = gety(x_train)
y_predict_test = gety(x_test)
    
#compute error rate for tesing&training set
def errorrate(y_actu,y_predict):
    error = 0
    for i in range(len(y_predict)):
        if y_predict[i] != y_actu[i]:
            error += 1        
    rate = float(error)/len(y_predict)
    return rate

error_rate_train = errorrate(y_train,y_predict_train)
error_rate_test = errorrate(y_test,y_predict_test)
#fit weghts to predict for '16
xdata = np.zeros(shape=(len(data),6),dtype=int)
r = 0 
for racer in data:
    if '2015-09-20' in racer:
        xdata[r][0] += 1
        if '2014-09-28' in racer:
            xdata[r][0] += 1
    if '2013-09-22' in racer:
        xdata[r][1] += 1
        if '2015-09-20' in racer:
            xdata[r][1] += 1
    if '2013-09-22' in racer:
        xdata[r][2] += 1
        if '2014-09-28' in racer:
            xdata[r][2] += 1
    r += 1
#add sum as feature
for row in xdata:
    row[3] = sum(row)
     
#add gender as features
for i in range(len(xdata)):
    xdata[i][4] = xset[i][4]
#add age as feature
for i in range(len(xdata)):
    xdata[i][5] = xset[i][5] + 1
xdata = quantizer(xdata)

#predict y for '16
y_predict_16 = gety(xdata)