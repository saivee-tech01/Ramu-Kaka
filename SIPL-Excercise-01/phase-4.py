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
    
    data=pickle.load(infile)
    if data[1]== Cust_name:
        print(data[2],"",data[3]) 
    infile.close()       





Customer_Name = input('Enter customer name to search: ')
n=total(Customer_Name)
print("Total:",n)
details(Customer_Name)

    

