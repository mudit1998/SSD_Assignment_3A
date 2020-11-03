import json
my_dict={}
with open('org.json','r') as f:
    org_dict=json.load(f)   
for org in org_dict:
    for i in range(0,len(org_dict[org])):
        lists=[]
        if len(org_dict[org][i])==1:
            lists.append(int(org[1:]))
            k=int(org_dict[org][i]['name'])
        else:
            lists.append(int(org[1:]))
            lists.append(org_dict[org][i]['parent'])
        my_dict[org_dict[org][i]['name']]=lists           
L=[]
flag=0
total=int(input())
for i in range(0,total):
    num=int(input())
    if num==k:
        flag=1
    L.append(num)
if flag==1:
    print("leader not found")
else:
    a=L[0]
    for i in range(1,total):
        b=L[i]
        while(a!=b):
            if my_dict[a][0]==my_dict[b][0]:
                z=a
                a=my_dict[a][1]
                b=my_dict[b][1]
            elif my_dict[a][0]>my_dict[b][0]: 
                a=my_dict[a][1]
                z=a
            elif my_dict[a][0]<my_dict[b][0]:
                b=my_dict[b][1]
                z=b 
        a=z
    ans=my_dict[a][1]
    print("leader is:",ans)
    for val in L:
        print(ans , "is",my_dict[val][0]-my_dict[ans][0],"level above " , val)
        

        