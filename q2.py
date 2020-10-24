m_days=[31,28,31,30,31,30,31,31,30,31,30,31]
path='date_calculator.txt'
f=open(path,'r')
for line in f:
    if line[4]=='1':
        line=line[7:]
        #print(len(line))
        if len(line)==11:
            d1=int(line[0:2])
            y1=int(line[-5:-1])
            m1=int(line[3:5])
            # print(m1)
            # print(y1)
            # print(d1)
        else:
            d1=int(line[0:2])
            y1=int(line[-5:-1])
            s1=line[5:-6]
            if s1=='January' or s1=='Jan':
                m1=1
            elif s1=='February' or s1=='Feb':
                m1=2
            elif s1=='March' or s1=='Mar':
                m1=3
            elif s1=='April' or s1=='Apr':
                m1=4
            elif s1=='May':
                m1=5
            elif s1=='June' or s1=='Jun':
                m1=6
            elif s1=='July' or s1=='Jul':
                m1=7
            elif s1=='August' or s1=='Aug':
                m1=8
            elif s1=='September' or s1=='Sep':
                m1=9
            elif s1=='October' or s1=='Oct':
                m1=10
            elif s1=='November' or s1=='Nov':
                m1=11
            elif s1=='December' or s1=='Dec':
                m1=12      
            # print(y1)
            # print(m1)
            # print(d1)                               
        n1=y1*365+d1
        for i in range(0,m1-1):
            n1+=m_days[i]
        if(m1<=2):
            y1-=1
        n1+=int(y1//4+y1//400-y1//100)            
    else:
        line=line[7:]
        if len(line)==11:
            d2=int(line[0:2])
            y2=int(line[-5:-1])
            m2=int(line[3:5])
            
        else:
            d2=int(line[0:2])
            y2=int(line[-5:-1])
            s2=line[5:-6]
            #print(type(s2))
            if s2=='January' or s2=='Jan':
                m2=1
            elif s2=='February' or s2=='Feb':
                m2=2
            elif s2=='March' or s2=='Mar':
                m2=3
            elif s2=='April' or s2=='Apr':
                m2=4
            elif s2=='May':
                m2=5
            elif s2=='June' or s2=='Jun':
                m2=6
            elif s2=='July' or s2=='Jul':
                m2=7
            elif s2=='August' or s2=='Aug':
                m2=8
            elif s2=='September' or s2=='Sep':
                m2=9
            elif s2=='October' or s2=='Oct':
                m2=10
            elif s2=='November' or s2=='Nov':
                m2=11
            elif s2=='December' or s2=='Dec':
                m2=12
            # print(y2)
            # print(m2)
            # print(d2)                     
        n2=y2*365+d2
        for i in range(0,m2-1):
            n2+=m_days[i]
        if(m2<=2):
            y2-=1
        n2+=int(y2//4+y2//400-y2//100) 
l="Date Difference:"+ str(abs(n2-n1))
f.close()
files=open("output_2.txt","w")
files.write(l)    
files.close()