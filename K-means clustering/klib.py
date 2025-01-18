import pandas as pd
from math import sqrt

class k_means :
    def k_cluster(self,data,x,y):
        cluster1 = self.euclidean(data.loc[0,x],data.loc[0,x],data.loc[0,y],data.loc[0,y])
        #print(cluster1)
        h1=[data.loc[0,x],data.loc[0,y],1]
        h2=[data.loc[0+1,x],data.loc[0+1,y],2]
        cluster2 = self.euclidean(data.loc[0+1,x],data.loc[0,x],data.loc[0+1,y],data.loc[0,y])
        #print(cluster2)
        data_frame=pd.DataFrame([h1,h2],columns=["X","Y","Cluster"])
        #print(data_frame)
        centroid=pd.DataFrame([h1,h2],columns=["X","Y","Cluster"])
        #checking data for cluster
        c=2
        for i in range(len(data)-2):
            check1=cluster1 = self.euclidean(data.loc[c,x],centroid.loc[0,x],data.loc[c,y],centroid.loc[0,y])
            check2=cluster1 = self.euclidean(data.loc[c,x],centroid.loc[1,x],data.loc[c,y],centroid.loc[1,y])
            if check1>check2:
                centroid.loc[1,x] =(data.loc[c,x]+centroid.loc[1,x])/2
                centroid.loc[1,y]=(data.loc[c,y]+centroid.loc[1,y])/2
                data_frame.loc[c]=[data.loc[c,x],data.loc[c,x],2]
            else:
                centroid.loc[0,x] =(data.loc[c,x]+centroid.loc[0,x])/2
                centroid.loc[0,y]=(data.loc[c,y]+centroid.loc[0,y])/2
                data_frame.loc[c]=[data.loc[c,x],data.loc[c,y],1]
            #print(centroid)
            c+=1
        return ([data_frame,centroid])
    
    def predict(self,k1,x1,y1):
        check1 = self.euclidean(x1,k1.loc[0,"X"],y1,k1.loc[0,"Y"])
        check2 = self.euclidean(x1,k1.loc[1,"X"],y1,k1.loc[1,"Y"])
        if check1<check2:
            print((f"Value of X = {x1}, Y = {y1} is a part of cluster 1"))

        else:
            print((f"Value of X = {x1}, Y = {y1} is a part of cluster 2"))
                
        





    def euclidean(self,x,a,y,b):
        f= sqrt(((x-a)**2)+((y-b)**2))
        return f
    