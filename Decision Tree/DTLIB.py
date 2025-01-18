import math as m
def en(data,col):
    if type(col)==str:
        l=list(data.loc[0:][col])
        s=set(l)
        d={}
        for i in s:
            fil = data[data[col] == i]
            y=fil["PlayTennis"]
            yes=no=0
            for j in y:
                if j=="Yes":
                    yes+=1
                else:
                    no+=1    
            d[i]=[yes,no]    
        #return d
        d1={}
        for i in d.keys():
            f=entropy(d[i][0],d[i][1])
            d1[i] = f
        return {col:d1}
    else:
        result={}
        for c in col:
            l=list(data.loc[0:][c])
            s=set(l)
            d={}
            for i in s:
            #fil=data[data[col]=="i"]
                fil = data[data[c] == i]
                y=fil["PlayTennis"]
                yes=no=0
                for j in y:
                    if j=="Yes":
                        yes+=1
                    else:
                        no+=1    
                d[i]=[yes,no]
            result[c]=d            
        return final(result)

def entropy(y,n):
    t=y+n
    s = (-y/t*(m.log2(y/t)))-(n/t*(m.log2(n/t)))
    return(s)

def final(diction):
    ent={}
    for i in diction.keys():
        d1={}
        for j in diction[i]:
            f=entropy(diction[i][j][0],diction[i][j][1])
            d1[j]=f
        ent[i]=d1
    return ent

