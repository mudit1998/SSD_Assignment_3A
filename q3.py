import os
import json
def check():
    sti=""
    for i in range(1,len(onlyfiles)+1):
        path="employee/Employee"+str(i)+".txt"
        f=open(path,'r')
        newline=f.read().replace("'","\"")
        emp_dict=json.loads(newline)
        s=emp_dict['Employee'+str(i)].keys()
        if(sti==""):
            sti=s
        else:
            if(s!=sti):
                flag=1
        f.close()

def input_user():
    slot=float(input())
    slot=int(slot*60)
    res3="slot duration:"+ str(float(slot/60)) + "hours \n"
    L.append(res3)
    return slot

def per_min():
    val1=val.split()
    if len(val1[0])==7:
        start=int(val1[0][0:2])*60 + int(val1[0][3:5])-min
    else:
        start=(int(val1[0][0:1])+12)*60+ int(val1[0][2:4])-min
    if len(val1[2])==7:
        end=int(val1[2][0:2])*60 + int(val1[2][3:5])-min
    else:
        end=(int(val1[2][0:1])+12)*60+ int(val1[2][2:4])-min
    for j in range(start,end):
        r[j]=False
        r1[j]=False

final={}
res1="Available slot \n"
L=[res1]
flag=0
files=open("output_3.txt","w")
onlyfiles = next(os.walk("employee"))[2] #dir is your directory path as string
check()       
if flag==1:
    files.write("no slot since dates are different")
else:
    ans=[]
    min=540
    r=[True for i in range(480)]
    for i in range(1,len(onlyfiles)+1):
        path="employee/Employee"+str(i)+".txt"
        # print(path)
        f=open(path,'r')
        newline=f.read().replace("'","\"")
        emp_dict=json.loads(newline)
        s=emp_dict['Employee'+str(i)].keys()
        s=str(s)
        s=s[12:-3]
        list=emp_dict['Employee'+str(i)][s]
        ans1=[]
        r1=[True for i in range(480)]
        for val in list:
            per_min()
        x=0    
        while(x<480):
            if(r1[x]==True):
                ind=x
                count=0
                while(x<480 and r1[x]==True ):
                    count=count+1
                    x=x+1
                str1=""
                if(int(ind/60)<3):
                    sa=int(ind/60)+9
                    str1=str1+str(sa)
                    str1=str1+':'
                    sa=ind%60
                    str1=str1+format(sa,'02d')
                    str1=str1+'AM'
                elif (int(ind/60)==3):
                    sa=int(ind/60)+9
                    str1=str1+str(sa)
                    str1=str1+':'
                    sa=ind%60
                    str1=str1+format(sa,'02d')
                    str1=str1+'PM'
                else:
                    sa=int(ind/60)-3
                    str1=str1+str(sa)
                    str1=str1+':'
                    sa=ind%60
                    str1=str1+format(sa,'02d')
                    str1=str1+'PM'
                str1=str1+' '+'-'+' '
                ind=ind+count
                if(int(ind/60)<3):
                    sa=int(ind/60)+9
                    str1=str1+str(sa)
                    str1=str1+':'
                    sa=ind%60
                    str1=str1+format(sa,'02d')
                    str1=str1+'AM'
                elif (int(ind/60)==3):
                    sa=int(ind/60)+9
                    str1=str1+str(sa)
                    str1=str1+':'
                    sa=ind%60
                    str1=str1+format(sa,'02d')
                    str1=str1+'PM'
                else:
                    sa=int(ind/60)-3
                    str1=str1+str(sa)
                    str1=str1+':'
                    sa=ind%60
                    str1=str1+format(sa,'02d')
                    str1=str1+'PM'
                ans1.append(str1)                
                #print(count)
                x=x-1
            x=x+1 
        res2="employee"+str(i)+":"+str(ans1)+"\n"
        L.append(res2)       

    slot=input_user()
    flags=0
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
                        sa=int(ind/60)+9
                        str1=str1+str(sa)
                        str1=str1+':'
                        sa=ind%60
                        str1=str1+format(sa,'02d')
                        str1=str1+'AM'
                    elif (int(ind/60)==3):
                        sa=int(ind/60)+9
                        str1=str1+str(sa)
                        str1=str1+':'
                        sa=ind%60
                        str1=str1+format(sa,'02d')
                        str1=str1+'PM'
                    else:
                        sa=int(ind/60)-3
                        str1=str1+str(sa)
                        str1=str1+':'
                        sa=ind%60
                        str1=str1+format(sa,'02d')
                        str1=str1+'PM'
                    str1=str1+' '+'-'+' '
                    ind=ind+count
                    if(int(ind/60)<3):
                        sa=int(ind/60)+9
                        str1=str1+str(sa)
                        str1=str1+':'
                        sa=ind%60
                        str1=str1+format(sa,'02d')
                        str1=str1+'AM'
                    elif (int(ind/60)==3):
                        sa=int(ind/60)+9
                        str1=str1+str(sa)
                        str1=str1+':'
                        sa=ind%60
                        str1=str1+format(sa,'02d')
                        str1=str1+'PM'
                    else:
                        sa=int(ind/60)-3
                        str1=str1+str(sa)
                        str1=str1+':'
                        sa=ind%60
                        str1=str1+format(sa,'02d')
                        str1=str1+'PM'                    
                    ans.append(str1)
                    flags=1
                    break
            if (flags==1):
                break
            x=x-1
        x=x+1 
    final[s]=ans
    res4=str(final)
    L.append(res4)
    files.writelines(L)
    files.close()        


