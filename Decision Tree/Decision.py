import math as m
class Desicion_T:
    def Entropy(self,data,col,boolcol):
        if type(col)==str:
            column_en={}
            c = data[boolcol]
            y=len(data[data[boolcol]=="Yes"])
            n=len(data[data[boolcol]=="No"])
            column_en[col]=self.formula(y,n)
            #print(column_en)
            s=set(list(data.loc[0:][col]))
            d={}
            for i in s:
                fil = data[data[col] == i]
                y=fil[boolcol]
                yes=no=0
                for j in y:
                    if j=="Yes":
                        yes+=1
                    else:
                        no+=1    
                d[i]=[yes,no]    
            #print(d)
            #return d
            d1={}
            for i in d.keys():
                if d[i][0]!=0 and d[i][1]!=0:
                    f=self.formula(d[i][0],d[i][1])
                    d1[i] = f
                    
                elif(d[i][0]==0):
                    d1[i] = 0
                elif(d[i][1]==0):
                    d1[i] = 1    
            return [column_en,{col:d1}]
        
        else:
            column_en={}
            c = data[boolcol]
            y=len(data[data[boolcol]=="Yes"])
            n=len(data[data[boolcol]=="No"])
            column_en[col[0]]=self.formula(y,n)
            #print(column_en)
            result={}
            for c in col:
                l=list(data.loc[0:][c])
                s=set(l)
                d={}
                for i in s:
                #fil=data[data[col]=="i"]
                    fil = data[data[c] == i]
                    y=fil[boolcol]
                    yes=no=0
                    for j in y:
                        if j=="Yes":
                            yes+=1
                        else:
                            no+=1    
                    d[i]=[yes,no]
                result[c]=d            
            return [column_en,self.final(result)]


    def final(self,diction):
        ent={}
        for i in diction.keys():
            d1={}
            for j in diction[i]:
                if (diction[i][j][0]!=0) and (diction[i][j][1]!=0):
                    f=self.formula(diction[i][j][0],diction[i][j][1])
                    d1[j]=f
                elif (diction[i][j][0]==0):
                       d1[j]=0
                elif (diction[i][j][1]==0):
                       d1[j]=0       
            ent[i]=d1
        return ent
    
    def formula(self,y,n):
        t=y+n
        s = (-y/t*(m.log2(y/t)))-(n/t*(m.log2(n/t)))
        return(s)  
    
    def gain(self,data1,col1,boolcol1):
        en=self.Entropy(data1,col1,boolcol1)

        tn=self.g_formula(en,data1)
        return tn 
    
    





    def g_formula(self,data2,ys):
            result1={}
            d={}
            for column_name in data2[1].keys():
                length=len(data2[1][column_name])
                
                s=set(list(ys.loc[0:][column_name]))
                
                for i in s:
                    fil = ys[ys[column_name] == i]
                    y=fil["PlayTennis"]
                    yes=no=0
                    for j in y:
                        if j=="Yes":
                            yes+=1
                        else:
                            no+=1    
                    d[i]=[yes,no]
                #print(d)
                q=list(data2[0].values())[0]
                s2=set(ys[column_name])
                for b in s2:
                    #print(f"{q}-(({d[b][0]}/{len(ys)})*{data2[1][column_name][b]})")
                    #print(data2[1][column_name][b])
                    q=q-((sum(d[b])/len(ys))*data2[1][column_name][b])

                result1[column_name]=q
            return(result1)    
            #print(data2[1].key)
    def show(self,data5):
        #print(data5)
        for i in data5[1].keys():
            print(i,":",round(data5[0]["Temp"],3))
            
            g = list(data5[1][i].keys())
            for j in g:
                print(j,":",round(data5[1][i][j],3))
                
            print()    
                
                    


            


    

    
      


