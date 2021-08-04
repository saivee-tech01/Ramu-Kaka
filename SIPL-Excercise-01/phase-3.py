import json
n=int(input("Enter value:"))
customer={}
for i in range(n):
    customer_details={}
    name=input("Enter name:")
    
    amount=int(input("Enter amount:"))
    date=input("Enter date:")
    list=[amount,date]
    customer_details[name]=list
    for key,value in customer_details.items():
        if key not in customer:
            customer[key]=[value]
        else:
            customer[key].append(value)    
    
  
with open('customer-info.json','a+') as f:
    j=json.dump(customer,f)



    