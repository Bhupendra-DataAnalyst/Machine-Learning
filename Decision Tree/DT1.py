import DTLIB as dt
import pandas as pd
df = pd.read_excel("D://python/ML/Desicion Tree.xlsx")
entropy=dt.en(df,["Outlook","Temp"])   
print(entropy)
print(dt.entropy(0,9))



