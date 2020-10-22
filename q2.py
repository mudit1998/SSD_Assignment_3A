m_days=[31,28,31,30,31,30,31,31,30,31,30,31]
path='date_calculator.txt'
f=open(path,'r')
for line in f:
    if line[4]=='1':
        line=line[7:]
        if len(line)==11:
            d1=int(line[0:2])
            y1=int(line[-5:-1])
            m1=int(line[3:5])
            
        else:
            d1=int(line[0:2])
            y1=int(line[-5:-1])
            s1=line[5:-6]
            if s1=="January" or "Jan":
                m1=1
            elif s1=="February" or "Feb":
                m1=2
            elif s1=="March" or "Mar":
                m1=3
            elif s1=="April" or "Apr":
                m1=4
            elif s1=="May":
                m1=5
            elif s1=="June" or "Jun":
                m1=6
            elif s1=="July" or "Jul":
                m1=7
            elif s1=="August" or "Aug":
                m1=8
            elif s1=="September" or "Sep":
                m1=9
            elif s1=="October" or "Oct":
                m1=10
            elif s1=="November" or "Nov":
                m1=11
            else:
                m1=12                                             
        n1=y1*365+d1
        for i in range(0,m1-1):
            n1+=m_days[i]
        if(m1<=2):
            y1-=1
        n1+=int(y1/4+y1/400-y1/100)            
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
            if s2=="January" or "Jan":
                m2=1
            elif s2=="February" or "Feb":
                m2=2
            elif s2=="March" or "Mar":
                m2=3
            elif s2=="April" or "Apr":
                m2=4
            elif s2=="May":
                m2=5
            elif s2=="June" or "Jun":
                m2=6
            elif s2=="July" or "Jul":
                m2=7
            elif s2=="August" or "Aug":
                m2=8
            elif s2=="September" or "Sep":
                m2=9
            elif s2=="October" or "Oct":
                m2=10
            elif s2=="November" or "Nov":
                m2=11
            else:
                m2=12                 
        n2=y2*365+d2
        for i in range(0,m2-1):
            n2+=m_days[i]
        if(m2<=2):
            y2-=1
        n2+=int(y2/4+y2/400-y2/100) 
print("Date Difference:", abs(n2-n1))
f.close()    