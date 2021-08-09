import json
import operator

with open('customer-info.json','r') as outfile:
        j1=json.load(outfile)
amount=int(input("Enter amount:"))
new_customer={}
for i,j in j1.items():
    total=0
    for k in j:
        total=total+k[0]
    new_customer[i]=total

sorted_new_customer=dict(sorted(new_customer.items(),key=operator.itemgetter(1),reverse=True))    
for i,j in sorted_new_customer.items():
    if j>=amount:
        print(i,":",j)
              