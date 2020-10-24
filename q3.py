import json
final={}
path1='Employee1.txt'
path2='Employee2.txt'
f1=open(path1,'r')
f2=open(path2,'r')
newline1=f1.read().replace("'","\"")
newline2=f2.read().replace("'","\"")    
# print(newline1)
emp1_dict=json.loads(newline1)
emp2_dict=json.loads(newline2)
s1=emp1_dict['Employee1'].keys()    
s2=emp2_dict['Employee2'].keys()
if s1!=s2:
    print("no slot since dates are different")
else:
    s1=str(s1)
    s1=s1[12:-3]
    s2=str(s2)
    s2=s2[12:-3]
    list1=emp1_dict['Employee1'][s1]
    list2=emp2_dict['Employee2'][s2]
    # print(list1)
    # print(list2)
    min=540
    ans1=[]
    ans2=[]
    ans=[]
    r1=[True for i in range(480)]
    r2=[True for i in range(480)]
    r=[True for i in range(480)]
    for val in list1:
        val1=val.split()
        if len(val1[0])==7:
            start=int(val1[0][0:2])*60 + int(val1[0][3:5])-min
        else:
            start=(int(val1[0][0:1])+12)*60+ int(val1[0][2:4])-min
        if len(val1[2])==7:
            end=int(val1[2][0:2])*60 + int(val1[2][3:5])-min
        else:
            end=(int(val1[2][0:1])+12)*60+ int(val1[2][2:4])-min
        for i in range(start,end):
            r[i]=False
            r1[i]=False
    x=0 
    #print(r1)   
    while(x<480):
        if(r1[x]==True):
            ind=x
            #print(ind)
            count=0
            while(x<480 and r1[x]==True ):
                count=count+1
                x=x+1
            str1=""
            if(int(ind/60)<3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'AM'
            elif (int(ind/60)==3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            else:
                s=int(ind/60)-3
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            str1=str1+' '+'-'+' '
            ind=ind+count
            if(int(ind/60)<3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'AM'
            elif (int(ind/60)==3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            else:
                s=int(ind/60)-3
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            ans1.append(str1)                
            #print(count)
            x=x-1
        x=x+1

    for val in list2:
        val1=val.split()
        if len(val1[0])==7:
            start=int(val1[0][0:2])*60 + int(val1[0][3:5])-min
        else:
            start=(int(val1[0][0:1])+12)*60+ int(val1[0][2:4])-min
        if len(val1[2])==7:
            end=int(val1[2][0:2])*60 + int(val1[2][3:5])-min
        else:
            end=(int(val1[2][0:1])+12)*60+ int(val1[2][2:4])-min
        for i in range(start,end):
            r[i]=False
            r2[i]=False
    x=0 
    #print(r1)   
    while(x<480):
        if(r2[x]==True):
            ind=x
            #print(ind)
            count=0
            while(x<480 and r2[x]==True ):
                count=count+1
                x=x+1
            str1=""
            if(int(ind/60)<3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'AM'
            elif (int(ind/60)==3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            else:
                s=int(ind/60)-3
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            str1=str1+' '+'-'+' '
            ind=ind+count
            if(int(ind/60)<3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'AM'
            elif (int(ind/60)==3):
                s=int(ind/60)+9
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            else:
                s=int(ind/60)-3
                str1=str1+str(s)
                str1=str1+':'
                s=ind%60
                str1=str1+format(s,'02d')
                str1=str1+'PM'
            ans2.append(str1)                
            #print(count)
            x=x-1
        x=x+1        
    # print(r1)
    #print(ans1)
    #print(ans2)
    slot=float(input())
    slot=int(slot*60)
    #print(slot)
    flag=0
    x=0
    while(x<480):
        if(r[x]==True):
            ind=x
            count=0
            while(x<480 and r[x]==True):
                count=count+1
                x=x+1
                if(count==slot):
                    str1=""
                    if(int(ind/60)<3):
                        s=int(ind/60)+9
                        str1=str1+str(s)
                        str1=str1+':'
                        s=ind%60
                        str1=str1+format(s,'02d')
                        str1=str1+'AM'
                    elif (int(ind/60)==3):
                        s=int(ind/60)+9
                        str1=str1+str(s)
                        str1=str1+':'
                        s=ind%60
                        str1=str1+format(s,'02d')
                        str1=str1+'PM'
                    else:
                        s=int(ind/60)-3
                        str1=str1+str(s)
                        str1=str1+':'
                        s=ind%60
                        str1=str1+format(s,'02d')
                        str1=str1+'PM'
                    str1=str1+' '+'-'+' '
                    ind=ind+count
                    if(int(ind/60)<3):
                        s=int(ind/60)+9
                        str1=str1+str(s)
                        str1=str1+':'
                        s=ind%60
                        str1=str1+format(s,'02d')
                        str1=str1+'AM'
                    elif (int(ind/60)==3):
                        s=int(ind/60)+9
                        str1=str1+str(s)
                        str1=str1+':'
                        s=ind%60
                        str1=str1+format(s,'02d')
                        str1=str1+'PM'
                    else:
                        s=int(ind/60)-3
                        str1=str1+str(s)
                        str1=str1+':'
                        s=ind%60
                        str1=str1+format(s,'02d')
                        str1=str1+'PM'                    
                    ans.append(str1)
                    flag=1
                    break
            #print(count)
            if (flag==1):
                break
            x=x-1
        x=x+1 
    #print(ans)           
    final[s1]=ans
    #print(final)
str1="Available slot \n"
str2="employee1:"+ str(ans1) +"\n"
str3="employee2:"+ str(ans2) +"\n"
str4="slot duration:"+ str(slot) + "minutes \n"
str5=str(final)  
L = [str1,str2,str3,str4,str5]  
files=open("output_3.txt","w")
files.writelines(L)
files.close()        
    


