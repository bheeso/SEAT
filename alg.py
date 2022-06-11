
import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import RobustScaler
from itertools import cycle


data=pd.read_pickle('original.pkl')

f1=data.loc[(data['Insured.sex']==0)]
f2=data.loc[(data['Insured.sex']==1)]
s11=data.loc[(data['Insured.sex']==0)&(data['Region']==0)]
s12=data.loc[(data['Insured.sex']==0)&(data['Region']==1)]
s21=data.loc[(data['Insured.sex']==1)&(data['Region']==0)]
s22=data.loc[(data['Insured.sex']==1)&(data['Region']==1)]
t111=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(data['Insured.age']<=29)]
t112=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)]
t113=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)]
t114=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)]
t115=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(59<data['Insured.age'])]
t121=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(data['Insured.age']<=29)]
t122=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)]
t123=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)]
t124=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)]
t125=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(59<data['Insured.age'])]
t211=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(data['Insured.age']<=29)]
t212=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)]
t213=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)]
t214=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)]
t215=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(59<data['Insured.age'])]
t221=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(data['Insured.age']<=29)]
t222=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)]
t223=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)]
t224=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)]
t225=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(59<data['Insured.age'])]
f1111=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Commercial']==1)]
f1112=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Commute']==1)]
f1113=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Farmer']==1)]
f1114=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Private']==1)]
f1121=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commercial']==1)]
f1122=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commute']==1)]
f1123=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Farmer']==1)]
f1124=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Private']==1)]
f1131=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commercial']==1)]
f1132=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commute']==1)]
f1133=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Farmer']==1)]
f1134=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Private']==1)]
f1141=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commercial']==1)]
f1142=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commute']==1)]
f1143=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Farmer']==1)]
f1144=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Private']==1)]
f1151=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Commercial']==1)]
f1152=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Commute']==1)]
f1153=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Farmer']==1)]
f1154=data.loc[(data['Insured.sex']==0)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Private']==1)]
f1211=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Commercial']==1)]
f1212=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Commute']==1)]
f1213=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Farmer']==1)]
f1214=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Private']==1)]
f1221=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commercial']==1)]
f1222=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commute']==1)]
f1223=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Farmer']==1)]
f1224=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Private']==1)]
f1231=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commercial']==1)]
f1232=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commute']==1)]
f1233=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Farmer']==1)]
f1234=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Private']==1)]
f1241=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commercial']==1)]
f1242=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commute']==1)]
f1243=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Farmer']==1)]
f1244=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Private']==1)]
f1251=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Commercial']==1)]
f1252=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Commute']==1)]
f1253=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Farmer']==1)]
f1254=data.loc[(data['Insured.sex']==0)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Private']==1)]
f2111=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Commercial']==1)]
f2112=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Commute']==1)]
f2113=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Farmer']==1)]
f2114=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(data['Insured.age']<=29)&(data['Car.use_Private']==1)]
f2121=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commercial']==1)]
f2122=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commute']==1)]
f2123=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Farmer']==1)]
f2124=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Private']==1)]
f2131=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commercial']==1)]
f2132=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commute']==1)]
f2133=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Farmer']==1)]
f2134=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Private']==1)]
f2141=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commercial']==1)]
f2142=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commute']==1)]
f2143=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Farmer']==1)]
f2144=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Private']==1)]
f2151=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Commercial']==1)]
f2152=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Commute']==1)]
f2153=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Farmer']==1)]
f2154=data.loc[(data['Insured.sex']==1)&(data['Region']==0)&(59<data['Insured.age'])&(data['Car.use_Private']==1)]
f2211=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Commercial']==1)]
f2212=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Commute']==1)]
f2213=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Farmer']==1)]
f2214=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(data['Insured.age']<=29)&(data['Car.use_Private']==1)]
f2221=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commercial']==1)]
f2222=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Commute']==1)]
f2223=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Farmer']==1)]
f2224=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(29<data['Insured.age'])&(data['Insured.age']<=39)&(data['Car.use_Private']==1)]
f2231=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commercial']==1)]
f2232=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Commute']==1)]
f2233=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Farmer']==1)]
f2234=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(39<data['Insured.age'])&(data['Insured.age']<=49)&(data['Car.use_Private']==1)]
f2241=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commercial']==1)]
f2242=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Commute']==1)]
f2243=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Farmer']==1)]
f2244=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(49<data['Insured.age'])&(data['Insured.age']<=59)&(data['Car.use_Private']==1)]
f2251=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Commercial']==1)]
f2252=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Commute']==1)]
f2253=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Farmer']==1)]
f2254=data.loc[(data['Insured.sex']==1)&(data['Region']==1)&(59<data['Insured.age'])&(data['Car.use_Private']==1)]

f=(f1,f2)
cf=[]
for i in f:
    cf.append(len(i)/len(data))

s=(s11,s12,s21,s22)
cs=[]
for i in s:
    cs.append(len(i)/len(data)) 
    
t=(t111,t112,t113,t114,t115,t121,t122,t123,t124,t125,t211,t212,t213,t214,t215,t221,t222,t223,t224,t225)
ct=[]
for i in t:
    ct.append(len(i)/len(data))
    
fo=(f1111,f1112,f1113,f1114,f1121,f1122,f1123,f1124,f1131,f1132,f1133,f1134,f1141,f1142,f1143,f1144,
    f1151,f1152,f1153,f1154,
f1211,f1212,f1213,f1214,f1221,f1222,f1223,f1224,f1231,f1232,f1233,f1234,f1241,f1242,f1243,f1244,
    f1251,f1252,f1253,f1254,
f2111,f2112,f2113,f2114,f2121,f2122,f2123,f2124,f2131,f2132,f2133,f2134,f2141,f2142,f2143,f2144,
    f2151,f2152,f2153,f2154,
f2211,f2212,f2213,f2214,f2221,f2222,f2223,f2224,f2231,f2232,f2233,f2234,f2241,f2242,f2243,f2244,
    f2251,f2252,f2253,f2254)
cfo=[]
for i in fo:
    cfo.append(len(i)/len(data))

intersect_p=[[1,1],cs,ct,cfo]


s1=data.loc[(data['Region']==0)]
s2=data.loc[(data['Region']==1)]

t1=data.loc[(data['Insured.age']<=29)]
t2=data.loc[(29<data['Insured.age'])&(data['Insured.age']<=39)]
t3=data.loc[(39<data['Insured.age'])&(data['Insured.age']<=49)]
t4=data.loc[(49<data['Insured.age'])&(data['Insured.age']<=59)]
t5=data.loc[(59<data['Insured.age'])]

fo1=data.loc[(data['Car.use_Commercial']==1)]
fo2=data.loc[(data['Car.use_Commute']==1)]
fo3=data.loc[(data['Car.use_Farmer']==1)]
fo4=data.loc[(data['Car.use_Private']==1)]

ind_p=[[1,1],[len(s1)/len(data),len(s2)/len(data)],
       [len(t1)/len(data),len(t2)/len(data),len(t3)/len(data),len(t4)/len(data),len(t5)/len(data)],
       [len(fo1)/len(data),len(fo2)/len(data),len(fo3)/len(data),len(fo4)/len(data)]]

data_collect=[f1111,f1112,f1113,f1114,f1121,f1122,f1123,f1124,
                      f1131,f1132,f1133,f1134,f1141,f1142,f1143,f1144,f1151,f1152,f1153,f1154,
                      f1211,f1212,f1213,f1214,f1221,f1222,f1223,f1224,
                      f1231,f1232,f1233,f1234,f1241,f1242,f1243,f1244,f1251,f1252,f1253,f1254,
                      f2111,f2112,f2113,f2114,f2121,f2122,f2123,f2124,
                      f2131,f2132,f2133,f2134,f2141,f2142,f2143,f2144,f2151,f2152,f2153,f2154,
                      f2211,f2212,f2213,f2214,f2221,f2222,f2223,f2224,
                      f2231,f2232,f2233,f2234,f2241,f2242,f2243,f2244,f2251,f2252,f2253,f2254]
