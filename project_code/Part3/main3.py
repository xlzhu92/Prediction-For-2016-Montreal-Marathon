import numpy as np
import readExcel
import datetime
import xlsxwriter



path = 'Project1_data.csv'
participants = readExcel.open_file(path)

def get_sec(time_str):
    	h, m, s = time_str.split(':')
	return int(h) * 3600 + int(m) * 60 + int(s)

def formxy(participants):
	i=-1
	x=np.zeros((8711,2))#3
	y=np.zeros((8711,1))
	z=np.zeros((8711,2))
	for id in range(1,8712):#8711
		R12=0
		R13=0
		R14=0
		R15=0
		for j in range(0,participants[id].total_marathons):
			if (participants[id].marathons[j].date=="2015-09-20") and (participants[id].marathons[j].name=="Marathon Oasis Rock 'n' Roll de Montreal") and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R15=0
				else:
					R15=get_sec(participants[id].marathons[j].time_finished)				
			
			if (participants[id].marathons[j].date=="2014-09-28")  and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R14=0
				else:
					R14=get_sec(participants[id].marathons[j].time_finished)
			
			if (participants[id].marathons[j].date=="2013-09-22") and (participants[id].marathons[j].name=="Marathon Oasis de Montreal") and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R13=0
				else:
					R13=get_sec(participants[id].marathons[j].time_finished)			
			
			if (participants[id].marathons[j].date=="2012-09-23") and (participants[id].marathons[j].name=="Marathon Oasis de Montreal") and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R12=0
				else:
					R12=get_sec(participants[id].marathons[j].time_finished)				
			
		

		if R15!=0:
			if R14!=0:
				if R13!=0:
					if R12!=0:
						i+=1
						x[i,:]=[(R12+R13+R14)/3,R14]
						y[i]=R15
						z[i,:]=[id,1]
					else:
						i+=1
						x[i,:]=[(R13+R14)/2,R14]
						y[i]=R15
						z[i,:]=[id,2]
					
				else:
					if R12!=0:
						i+=1
						x[i,:]=[(R12+R14)/2,R14]
						y[i]=R15
						z[i,:]=[id,3]
					else:
						i+=1
						x[i,:]=[R14,R14]
						y[i,:]=R15
						z[i,:]=[id,4]
					
				
			else:
				if R13!=0:
					if R12!=0:
						i+=1
						x[i,:]=[(R12+R13)/2,R13]		
						y[i]=R15
						z[i,:]=[id,5]
					else:
						i+=1
						x[i,:]=[R13,R13]
						y[i]=R15
						z[i,:]=[id,6]
					
				else:
					if R12!=0:
						i+=1
						x[i,:]=[R12,R12]
						y[i]=R15
						z[i,:]=[id,7]
	X=np.zeros((i,2))
	Y=np.zeros((i,1))
	Z=np.zeros((i,2))					
	for k in range(0,i):
		X[k,:]=x[k,:]
		Y[k,:]=y[k,:]
		Z[k,:]=z[k,:]	
	return (X,Y,Z)
	#return y
def linearreg(x,y):
	w=np.matrix(np.linalg.inv(np.matrix(x.T)*np.matrix(x)))*np.matrix(np.matrix(x.T)*np.matrix(y))
	return w

def crossreg(x,y):
	x1_train=np.delete(x,np.s_[0:49],0)
	y1_train=np.delete(y,np.s_[0:49],0)
	w1=linearreg(x1_train,y1_train)
	x1_true=x[0:49,:]
	y1_true=y[0:49]
	y1_pred=np.matrix(x1_true)*np.matrix(w1)
	y1_err=np.average(abs(np.divide((y1_pred-y1_true),y1_true)))
	y1_err_train=np.average(np.divide(abs(y1_train-np.matrix(x1_train)*np.matrix(w1)),y1_train))

	x2_train=np.delete(x,np.s_[50:100],0)
	y2_train=np.delete(y,np.s_[50:100],0)
	w2=linearreg(x2_train,y2_train)
	x2_true=x[50:100,:]
	y2_true=y[50:100]
	y2_pred=np.matrix(x2_true)*np.matrix(w2)
	y2_err=np.average(abs(np.divide((y2_pred-y2_true),y2_true)))
	y2_err_train=np.average(np.divide(abs(y2_train-np.matrix(x2_train)*np.matrix(w2)),y2_train))

	x3_train=np.delete(x,np.s_[101:150],0)
	y3_train=np.delete(y,np.s_[101:150],0)
	w3=linearreg(x3_train,y3_train)
	x3_true=x[101:150,:]
	y3_true=y[101:150]
	y3_pred=np.matrix(x3_true)*np.matrix(w3)
	y3_err=np.average(abs(np.divide((y3_pred-y3_true),y3_true)))
	y3_err_train=np.average(np.divide(abs(y3_train-np.matrix(x3_train)*np.matrix(w3)),y3_train))

	x4_train=np.delete(x,np.s_[151:210],0)
	y4_train=np.delete(y,np.s_[151:210],0)
	w4=linearreg(x4_train,y4_train)
	x4_true=x[151:210,:]
	y4_true=y[151:210]
	y4_pred=np.matrix(x4_true)*np.matrix(w4)
	y4_err=np.average(abs(np.divide((y4_pred-y4_true),y4_true)))
	y4_err_train=np.average(np.divide(abs(y4_train-np.matrix(x4_train)*np.matrix(w4)),y4_train))

	y_err=(y1_err+y2_err+y3_err+y4_err)/4
	y_err_train=(y1_err_train+y2_err_train+y3_err_train+y4_err_train)/4

	data=[[y1_err,y1_err_train],[y2_err,y2_err_train],[y3_err,y3_err_train],[y4_err,y4_err_train],[y_err,y_err_train]]

 
     
	return(data)

	



x,y,z=formxy(participants)

validation=crossreg(x,y)

w=linearreg(x,y)


def predicty(participants,w):
	x=np.zeros((8711,2))#3
	for id in range(1,8712):#8711
		i=id-1
		R12=0
		R13=0
		R14=0
		R15=0
		for j in range(0,participants[id].total_marathons):
			if (participants[id].marathons[j].date=="2015-09-20") and (participants[id].marathons[j].name=="Marathon Oasis Rock 'n' Roll de Montreal") and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R15=0
				else:
					R15=get_sec(participants[id].marathons[j].time_finished)				
			
			if (participants[id].marathons[j].date=="2014-09-28")  and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R14=0
				else:
					R14=get_sec(participants[id].marathons[j].time_finished)
			
			if (participants[id].marathons[j].date=="2013-09-22") and (participants[id].marathons[j].name=="Marathon Oasis de Montreal") and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R13=0
				else:
					R13=get_sec(participants[id].marathons[j].time_finished)			
			
			if (participants[id].marathons[j].date=="2012-09-23") and (participants[id].marathons[j].name=="Marathon Oasis de Montreal") and (participants[id].marathons[j].type=="Marathon"): 
				if participants[id].marathons[j].time_finished=="-1":
					R12=0
				else:
					R12=get_sec(participants[id].marathons[j].time_finished)				
			
		

		if R15!=0:
			if R14!=0:
				if R13!=0:
					if R12!=0:
						x[i,:]=[(R12+R13+R14+R15)/4,R15]
					else:
						x[i,:]=[(R13+R14+R15)/3,R15]
				else:
					if R12!=0:
						x[i,:]=[(R12+R14+R15)/3,R15]
					else:
						x[i,:]=[(R14+R15)/2,R15]
			else:
				if R13!=0:
					if R12!=0:
						x[i,:]=[(R12+R13+R15)/3,R15]		
					else:
						x[i,:]=[(R13+R15)/2,R15]
				else:
					if R12!=0:
						x[i,:]=[(R12+R15)/2,R15]
					else:
						x[i,:]=[R15,R15]
		else:
			if R14!=0:
				if R13!=0:
					if R12!=0:
						x[i,:]=[(R12+R13+R14)/3,R14]
					else:
						x[i,:]=[(R13+R14)/2,R14]
				else:
					if R12!=0:
						x[i,:]=[(R12+R14)/2,R14]
					else:
						x[i,:]=[R14,R14]
			else:
				if R13!=0:
					if R12!=0:
						x[i,:]=[(R12+R13)/2,R13]		
					else:
						x[i,:]=[R13,R13]				
				else:
					if R12!=0:
						x[i,:]=[R12,R12]
					else:
						x[i,:]=[0,0]#flag that no montreal marathons have been run
	y_sec=np.matrix(x)*np.matrix(w)
	y=[]


	for i in range(0,8711):
		if y_sec[i]==0:
			y_sec[i]=4.5*3600 #no data on montreal marathon then guess 4.5 hours
		y.append(str(datetime.timedelta(seconds=int(y_sec[i]))))

	return (y)

time_prediction=predicty(participants,w)

#print(time_prediction)

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('predictions.xlsx')
worksheet = workbook.add_worksheet()



for i in range(0,8711):
	worksheet.write(i, 0, time_prediction[i])

workbook.close()

	