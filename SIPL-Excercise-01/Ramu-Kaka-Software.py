import json
import operator

# Welcoming Ramu-Kaka. 
print("Welcome Mr.Ramu.")
msg1='''The facilities provided by your software are given below:
1. Calculation.
2. Adding customers data to database.
3. Retrieval of customer information on the basis of name.
4. Retrieval of customer information on the basis of amount.
'''
print(msg1)

def main():
    value=int(input("Select one option:"))
    if value <= 4:
        if value == 1:
            calculation()
            Condition()
        elif value == 2:
            loading()
            Condition()
        elif value == 3:
            retrieval_by_name()
            Condition() 
        elif value == 4:
            retrieval_by_amount()
            Condition()      

    else:
        print("Invalid input")        

def Condition():
    condition=input("Do you want any other facility?(Y/N)")
    if condition == "Y":
        main()
    else:
        print("Thankyou for using our services :)")        

# Helping Ramu-Kaka to simplify calculations.
def calculation():
    msg2=''' Software: Please select the desired option:
    1. Addition
    2. Substraction
    3. Multiplication
    4. Division'''
    print(msg2)
    n=int(input("Ramu Kaka enters:"))
    print("Software: Please enter 2 digits:")
    a,b=map(int,input("Ramu Kaka enters:").split())
    if(n==1):
        print("Software:",a+b)
    elif(n==2):
        print("Software:",a-b)
    elif(n==3):
        print("Software:",a*b)
    elif(n==4):
        try:
            print("Software:",a/b)
        except ZeroDivisionError:
            print("Can't divide by zero")    
        

    
# Adding customers data to database.
def loading():
    n=int(input("Enter the no. of customers:"))
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
    with open('customer-info1.json','a+') as f:
        j=json.dump(customer,f)

# Retrieval of customer information.
def retrieval_by_name():
    name=input("Enter customer name to search:")
    with open('customer-info1.json','r') as outfile:
        j1=json.load(outfile)
    j2={
    "Aisha" : "Saivee",
    "Bittu" : "Umang"
    }
    total=0
    if name in j2.keys():
        for i,j in j2.items():
            if name in i:
                for k,l in j1.items():
                    if j in k:
                        for total_value in l:
                            total=total+total_value[0]
                        print("Total:",total)
                        print("Details:")
                        for detail in l:
                            print(detail)

    else:
        for i,j in j1.items():
            if name in i:
                for total_value in j:
                    total=total+total_value[0]
                print("Total:",total)
                print("Details:")
                for detail in j1[name]:
                    print(detail)

# Retrieval of customer information on the basis of amount.
def retrieval_by_amount():
    with open('customer-info1.json','r') as outfile1:
        j3=json.load(outfile1)
    amount1=int(input("Enter amount:"))
    new_customer={}
    for i,j in j3.items():
        total=0
        for k in j:
            total=total+k[0]
        new_customer[i]=total
    sorted_new_customer=dict(sorted(new_customer.items(),key=operator.itemgetter(1),reverse=True))    
    for i,j in sorted_new_customer.items():
        if j>=amount1:
            print(i,":",j)

main()