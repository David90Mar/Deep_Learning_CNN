print("LETTURA LIBRERIE")


import numpy as np
import pandas as pd



def f(x):
    min=x[0]-np.percentile(x,20)
    max=np.percentile(x[1:],80) - x[0]
    if min>max:
        
        return 1
    elif max>min:
        
        return 2
    else:
        return 0
        






print("lettura dataset")

df = pd.read_csv('EURUSD.csv')[0:]['Close'][:100]  
df=pd.DataFrame(df.values,columns=['t0'])
print(df.head())

print("aggiungo colonne")
for t in range(1,90):
    df['t+'+str(t)] = df['t0'].shift(t) #se positivo calcola t-1

df2=df[91:].reset_index(drop=True)
del df
print(df2.head())
df2['ris']=df2.iloc[:,59:].apply(f)

df2.to_csv("final2.csv")