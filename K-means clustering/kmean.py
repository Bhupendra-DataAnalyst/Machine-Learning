import pandas as pd
import klib as km
df = pd.read_excel("D://python/ML/K mean/K mean data.xlsx")

k = km.k_means()
clusterlist=k.k_cluster(df,"X","Y")
print(clusterlist[0].to_string())
print()
k.predict(clusterlist[1],170,56)
