import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

df1=pd.read_excel("procras_encoded.xlsx")
l=[]
for _ in df1['Score']:
    if _ <= 2.5:
        l.append('low')
    elif _ > 2.5 and _ <=3.5 :
        l.append('medium')
    elif _ > 3.5:
        l.append('high') 

df1['Score_cat']=l

df2=pd.read_excel('ams_encoded.xlsx')
l2=[]
for _ in df2['Score']:
    if _ <= 84:
        l2.append('less/not motivated')
    elif _ > 82 and _ <=140 :
        l2.append('motivated')
    elif _ > 140 and _ <= 196:
        l2.append('highly motivated')

df2['Score_cat']=l2

X=df1.drop(['Score_cat','Score'],axis=1)
y=df1['Score_cat']

from sklearn.linear_model import LogisticRegression 
logmodel=LogisticRegression()
logmodel.fit(X,y)

X_=df2.drop(['Score_cat','Score'],axis=1)
y_=df2['Score_cat']

from sklearn.svm import SVC
svc=SVC()
svc.fit(X_,y_)

pickle.dump(logmodel,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

pickle.dump(svc,open('model1.pkl','wb'))
model1=pickle.load(open('model1.pkl','rb'))   
   
   