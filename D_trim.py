
import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import RobustScaler
from itertools import cycle


def trim(DFnewdata):
    # Round up and down(Discete R.V.)
    warnings.filterwarnings('ignore')
    a=[0,3,4,9,11,12,13,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]
    aa=[]
    for i in a:
        aa.append(DFnewdata.columns[i])
    for i in aa:
        DFnewdata[i]=DFnewdata[i].round(0).astype(int)
        
    # Duration min and max
    for i in range(len(DFnewdata)):
        if DFnewdata['Duration'][i]<22:
            DFnewdata['Duration'][i]=22
        elif DFnewdata['Duration'][i]>366:
            DFnewdata['Duration'][i]=366
            
    # Insured.age min and max
    for i in range(len(DFnewdata)):
        if DFnewdata['Insured.age'][i]<16:
            DFnewdata['Insured.age'][i]=16
        elif DFnewdata['Insured.age'][i]>103:
            DFnewdata['Insured.age'][i]=103
            
    # Insured.sex min and max
    for i in range(len(DFnewdata)):
        if DFnewdata['Insured.sex'][i]<0: 
            DFnewdata['Insured.sex'][i]=0
        elif DFnewdata['Insured.sex'][i]>1:
            DFnewdata['Insured.sex'][i]=1
    # Car.age min and max
    for i in range(len(DFnewdata)): 
        if DFnewdata['Car.age'][i]< -2:
            DFnewdata['Car.age'][i]= -2
        elif DFnewdata['Car.age'][i]>20:
            DFnewdata['Car.age'][i]=20
        
        
    # Marital min and max
    for i in range(len(DFnewdata)):
        if DFnewdata['Marital'][i]< 0:
            DFnewdata['Marital'][i]=0
        elif DFnewdata['Marital'][i]>1:
            DFnewdata['Marital'][i]=1
        
    # Car.use min and max
    jj=[]
    for i in range(5,9):
        jj.append(DFnewdata.columns[i])

    aa= pd.DataFrame(index=np.arange(len(DFnewdata)) ,columns=jj)

    for u in jj:
        for i in range(len(DFnewdata)):
            if DFnewdata[u][i]==max(DFnewdata[jj[0]][i],DFnewdata[jj[1]][i],DFnewdata[jj[2]][i],DFnewdata[jj[3]][i]):
                aa[u][i]=1
            else:
                aa[u][i]=0
    DFnewdata[jj]=aa

    # Credit.score min and max
    for i in range(len(DFnewdata)):
        if DFnewdata['Credit.score'][i]<420 :
            DFnewdata['Credit.score'][i]=420
        elif DFnewdata['Credit.score'][i]>900:
            DFnewdata['Credit.score'][i]=900

    # Region min and max
    for i in range(len(DFnewdata)):
        if DFnewdata['Region'][i]<0 :
            DFnewdata['Region'][i]=0
        elif DFnewdata['Region'][i]>1:
            DFnewdata['Region'][i]=1

    # delete negative value!
    j=range(9, len(DFnewdata.columns))
    jj=[]
    for i in j:
        jj.append(DFnewdata.columns[i])

    warnings.filterwarnings('ignore')
    for u in jj:
        for i in range(len(DFnewdata)):
            if DFnewdata[u][i]<0:
                DFnewdata[u][i]=0

    # Pct.drive.wkday adjustment
    for i in range(len(DFnewdata)):
        if DFnewdata['Pct.drive.wkday'][i]>1 :
            DFnewdata['Pct.drive.wkday'][i]=1

    c=1-DFnewdata['Pct.drive.wkday']
    DFnewdata['Pct.drive.wkend']=c


    # Weekdays... adjustment
    jjj=[]
    for i in range(16,23):
        jjj.append(DFnewdata.columns[i])

    a=DFnewdata[jjj[0]]+DFnewdata[jjj[1]]+DFnewdata[jjj[2]]+DFnewdata[jjj[3]]+DFnewdata[jjj[4]]+DFnewdata[jjj[5]]


    for i in range(len(DFnewdata)):
        if a[i]>1:
            bb=(a[i]-1)
            bbb=DFnewdata[jjj[0]][i]+DFnewdata[jjj[1]][i]+DFnewdata[jjj[2]][i]+DFnewdata[jjj[3]][i]+DFnewdata[jjj[4]][i]+DFnewdata[jjj[5]][i]
            for j in jjj[:-1]:
                DFnewdata[j][i]=DFnewdata[j][i]-bb*(DFnewdata[j][i]/bbb)
            DFnewdata[jjj[6]][i]=0  
        else:
            DFnewdata[jjj[6]][i]=1-a[i]


    for i in range(len(DFnewdata)):
        if DFnewdata['Years.noclaims'][i]<0:
            DFnewdata['Years.noclaims'][i]=0
        elif DFnewdata['Years.noclaims'][i]>79:
            DFnewdata['Years.noclaims'][i]=79

    for i in range(len(DFnewdata)):
        if DFnewdata['Annual.pct.driven'][i]<0:
            DFnewdata['Annual.pct.driven'][i]=0
        elif DFnewdata['Annual.pct.driven'][i]>1:
            DFnewdata['Annual.pct.driven'][i]=1

    for i in range(len(DFnewdata)):
        if DFnewdata['NB_Claim'][i]==0:
            DFnewdata['AMT_Claim'][i]=0
            DFnewdata['AMT_Claim'].astype(int)

    for i in range(len(DFnewdata)):
        if DFnewdata['Avgdays.week'][i]<0:
            DFnewdata['Avgdays.week'][i]=0
        elif DFnewdata['Avgdays.week'][i]>7:
            DFnewdata['Avgdays.week'][i]=7        

    n=[16,17,19,20,21,22,25,27,28,29,34,40,41,42,44,45,46,47,48,49,50,51,53,55,56,58]
    r=[15,18,18,18,23,23,24,26,30,30,33,39,39,43,43,43,43,43,52,52,52,52,52,54,57,59]
    for i in range(len(DFnewdata)):
        for j in range(len(n)):
            if DFnewdata['Territory'][i]==n[j]:
                DFnewdata['Territory'][i]=r[j]

    for i in range(len(DFnewdata)):
        if DFnewdata['Territory'][i]<11:
            DFnewdata['Territory'][i]=11
        elif DFnewdata['Territory'][i]>91:
            DFnewdata['Territory'][i]=91
    return DFnewdata
