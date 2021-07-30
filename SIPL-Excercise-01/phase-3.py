import json

n=int(input("Enter value:"))
customer={}

for i in range(n):
    name=input("Enter name:")
    data=[]
    amount=int(input("Enter amount:"))
    date=input("Enter date:")
    list=[amount,date]
    data.append(list)
    customer[name]=data
    
    



with open('customer.json','a+') as f:
    j=json.dump(customer,f)
