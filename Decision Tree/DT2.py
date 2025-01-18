import Desicion as dt
import pandas as pd
df = pd.read_excel("D://python/ML/Desicion Tree/Desicion Tree.xlsx")
dec1 = dt.Desicion_T()
k=dec1.Entropy(df,["Temp","Outlook","Wind"],"PlayTennis")
#print(k)
dec1.show(k)
l=dec1.gain(df,["Outlook","Temp","Wind"],"PlayTennis")
print(l)
