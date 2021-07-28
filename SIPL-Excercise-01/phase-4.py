import pickle
def total(Customer_Name):
    infile = open("customer.dat","rb")
    try:
        total = 0
        while True:
            record = pickle.load(infile)
            if record[1]==Customer_Name:
                total += record[2]
                
    except EOFError:
        pass
    return total

def details(Cust_name):
    infile=open('customer.dat','rb')
    list=[]
    data=pickle.load(infile)
    temp=[data]
    list.append(temp)
    for i in list:
        if list[0]==Cust_name:
            print(list[2],"",list[3])    





Customer_Name = input('Enter customer name to search: ')
n=total(Customer_Name)
print("Total:",n)
details(Customer_Name)

    

