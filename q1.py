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
num1=int(input())
num2=int(input())
a=num1
b=num2
if num1==k or num2==k:
    print("leader not found")
elif num1==num2:
    ans=my_dict[a][1]
    print("leader is:",ans)
    print(ans , "is 1 level above " , num1)
else:
    while (a!=b):
        if my_dict[a][0]==my_dict[b][0]:
            a=my_dict[a][1]
            b=my_dict[b][1]
        elif my_dict[a][0]>my_dict[b][0]: 
            a=my_dict[a][1]
        elif my_dict[a][0]<my_dict[b][0]:
            b=my_dict[b][1]
    if a==num1:
        ans=my_dict[a][1]
        print("leader is:",ans)
        print(ans , "is 1 level above " , num1) 
        print(ans , "is",my_dict[num2][0]-my_dict[ans][0],"level above " , num2)                
    elif b==num2:
        ans=my_dict[b][1]
        print("leader is:",ans)
        print(ans , "is 1 level above " , num2) 
        print(ans , "is",my_dict[num1][0]-my_dict[ans][0],"level above " , num1)
    else:
        ans=a
        print("leader is:",ans)
        print(ans , "is",my_dict[num1][0]-my_dict[ans][0],"level above " , num1)
        print(ans , "is",my_dict[num2][0]-my_dict[ans][0],"level above " , num2) 

        

        