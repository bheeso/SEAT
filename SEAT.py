
import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import RobustScaler
from itertools import cycle
from sklearn.preprocessing import RobustScaler
import alg
import D_trim


class target():
    def __init__(self,Insured_sex=[0.4,0.6],Region=[0.1,0.9],
                 Insured_age=[0.16,0.21,0.24,0.22,0.17],Car_use=[0.175,0.5166,0.005,0.3034],random_state=0):
        self.Insured_sex=Insured_sex
        self.Region=Region
        self.Insured_age=Insured_age
        self.Car_use=Car_use
        self.random_state=random_state
        #self.N=N
        #self.Sigma=Sigma
        


    def conditional_D(self):
        # set adjustment factors
        adj_ind_p=[self.Insured_sex,self.Region,self.Insured_age,self.Car_use]
        adj_ratio=[]
        for i,j in zip(alg.ind_p,adj_ind_p):
            adj=[]
            for l,m in zip(i,j):
                adj.append(m/l)
            adj_ratio.append(adj)
        
        combined_p=[]
        for i,j in zip(alg.intersect_p,adj_ratio):
            com=[]
            for l,m in zip(i,cycle(j)):
                com.append(m*l)
            combined_p.append(com)
        
        conditional_p=[adj_ind_p[0]]
        for i in range(len(combined_p)-1):
            s=0
            com=[]
            for k in combined_p[i+1]:
                if s%(len(combined_p[i+1])/len(combined_p[i]))==0:
                    total=0
                    for j in range(int(len(combined_p[i+1])/len(combined_p[i]))):
                        total += combined_p[i+1][s+j]
                com.append(k/total)
                s+=1
            conditional_p.append(com)
            
        cum_conditional_p=[]
        u=(2,2,5,4)
        for i in range(len(conditional_p)):
            s=0
            com=[]
            if i==0:
                com=[conditional_p[i][i],conditional_p[i][i]+conditional_p[i][i+1]]
            else:
                for k in range(len(conditional_p[i])):
                    if s%(len(conditional_p[i])/len(conditional_p[i-1]))==0:
                        for j in range(int(len(conditional_p[i])/len(conditional_p[i-1]))):
                            if j==0:
                                c=conditional_p[i][s+j]
                            else:
                                c=c+conditional_p[i][s+j]
                            com.append(c)
                    s+=1
            cum_conditional_p.append(com)
        return cum_conditional_p

#import SEAT  
#SEAT.target([0.4,0.6],[0.1,0.9],[0.16,0.21,0.24,0.22,0.17],[0.175,0.5166,0.005,0.3034],100,0.1).conditional_D()

    def sample(self,N):
        # i is N, j is layer. 
        generation=[]
        i=0
        while i < N:
            w="f"
            for j in range(len(self.conditional_D())):
                #each layer need new random number
                np.random.seed(self.random_state+i+1+1000000*(j+1))
                a=np.random.uniform(0,1,1)
                if j==0:
                    k=0
                    while k < len(self.conditional_D()[j]):
                        if a <= self.conditional_D()[j][k]:
                            w=w+str(k+1)
                            c=k
                            break
                        else:
                            k+=1
                elif j>0:
                    k=0
                    while k < int(len(self.conditional_D()[j])/len(self.conditional_D()[j-1])):
                        if a <= self.conditional_D()[j][c*int(len(self.conditional_D()[j])/len(self.conditional_D()[j-1]))+k]:
                            w=w+str(k+1)
                            c=k
                            break
                        else:  
                            k+=1
            if w!="f1213":
                generation.append(w)
                i=i+1
        
        u=(2,2,5,4)
        h=[]
        for i in range(u[0]):
            w="f"
            w=w+str(i+1)
            for j in range(u[1]):
                z=w
                z=z+str(j+1)
                for k in range(u[2]):
                    f=z
                    f=f+str(k+1)
                    for m in range(u[3]):
                        g=f
                        g=g+str(m+1)
                        h.append(g)
        data=pd.read_pickle('original.pkl')
        data_collect=alg.data_collect
        newdata = pd.DataFrame(columns=data.columns)
        for i in range(len(generation)):
            for j in range(len(h)):
                if generation[i]==h[j]:
                    l=data_collect[j].sample()
                    newdata=newdata.append(l) 
        newdata.index=list(range(0,len(newdata)))
        return newdata

    def fit(self,N,sigma):
        try:
            newdata = pd.read_pickle("draft.pkl")
            if N!=len(newdata):
                newdata=self.sample(N)
        except FileNotFoundError:
            newdata=self.sample(N)
            newdata.to_pickle("draft.pkl")
        scaler = RobustScaler(quantile_range=(35.0, 65.0))
        scaler.fit(newdata)
        scale_newdata=scaler.transform(newdata)
        np.random.seed(self.random_state)
        noise = np.random.normal(0,sigma ,newdata.shape)
        sss=scale_newdata+noise
        DFnewdata=pd.DataFrame(scaler.inverse_transform(sss), columns =newdata.columns)   
        a=[1,2,5,6,7,8,10]
        aa=[]
        for i in a:
            aa.append(DFnewdata.columns[i])
        for i in aa:
            DFnewdata[i]=newdata[i]
        D_trim.trim(DFnewdata)
        return DFnewdata

#import SEAT
#a=SEAT.target([0.4,0.6],[0.1,0.9],[0.16,0.21,0.24,0.22,0.17],
#              [0.175,0.5166,0.005,0.3034]).fit(200,0.1,random_state=100)

