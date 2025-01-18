import itertools as i
import pandas as pd
import naivelib as nv
df = pd.read_excel("D://python/ML/Naive byes/Desicion Tree.xlsx")
n=nv.Naiveclasifer()
O=list(set(df["Outlook"]))
T=list(set(df["Temp"]))
H=list(set(df["Humidity"]))
W=list(set(df["Wind"]))
k=list(i.product(O,T,H,W))
for i in k:
    k=n.predict(df,{"Outlook":i[0],"Temp":i[1],"Humidity":i[2],"Wind":i[3]},"PlayTennis")
    print(f"{i} - {k}")
    