class Naiveclasifer():
    
    def predict(self,data,a,target):
        l=list(a.keys())

        #yes
        yes=len(data[data[target]=="Yes"])
        yd=data[data[target]=="Yes"]
        o_Yes =len(yd[yd[l[0]]==a[l[0]]])
        t_Yes =len(yd[yd[l[1]]==a[l[1]]])
        h_Yes =len(yd[yd[l[2]]==a[l[2]]])
        w_Yes =len(yd[yd[l[3]]==a[l[3]]])
        

        #NO
        no=len(data[data[target]=="No"])
        nd=data[data[target]=="No"]
        o_No =len(nd[nd[l[0]]==a[l[0]]])
        t_No =len(nd[nd[l[1]]==a[l[1]]])
        h_No =len(nd[nd[l[2]]==a[l[2]]])
        w_No =len(nd[nd[l[3]]==a[l[3]]])
        colist=(o_Yes+o_No)*(t_No+t_Yes)*(h_Yes+h_No)*(w_Yes+w_No)/(len(data)**4)
        f1=[o_Yes/yes,t_Yes/yes,h_Yes/yes,w_Yes/yes,yes/len(data)]
        f2=[o_No/no,t_No/no,h_No/no,w_No/no,no/len(data)]
        result=self.Formula(f1,f2,colist)
        return result

    def Formula(self,YL,NL,a):
        yf=YL[0]*YL[1]*YL[2]*YL[3]*YL[4]
        nf=NL[0]*NL[1]*NL[2]*NL[3]*NL[4]
        if yf/a > nf/a:
            result="Yes"
            return result

        elif yf/a < nf/a:
            result="No"
            return result 
        else:
            result="May be"
            return result       

    

    '''
    def naive_learn(self,data,target):
        no=len(data[data[target]=="No"])
        yes=len(data[data[target]=="Yes"])
        #yes
        yd=data[data[target]=="Yes"]
        o_Yes =len(yd[yd["Outlook"]=="Sunny"])
        t_Yes =len(yd[yd["Temp"]=="Cool"])
        h_Yes =len(yd[yd["Humidity"]=="High"])
        w_Yes =len(yd[yd["Wind"]=="Strong"])
        
        #print(o_Yes,t_Yes,h_Yes,w_Yes)

        #NO
        nd=data[data[target]=="No"]
        o_No =len(nd[nd["Outlook"]=="Sunny"])
        t_No =len(nd[nd["Temp"]=="Cool"])
        h_No =len(nd[nd["Humidity"]=="High"])
        w_No =len(nd[nd["Wind"]=="Strong"])
        colist=(o_Yes+o_No)*(t_No+t_Yes)*(h_Yes+h_No)*(w_Yes+w_No)/(len(data)**4)
        print(colist)
        #print(o_No,t_No,h_No,w_No)
        f1=[o_Yes/yes,t_Yes/yes,h_Yes/yes,w_Yes/yes,yes/len(data)]
        f2=[o_No/no,t_No/no,h_No/no,w_No/no,no/len(data)]
        self.Formula(f1,f2,colist)
        return(colist) 
        '''

        
        
        
        
