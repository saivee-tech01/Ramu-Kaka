import pickle
def createFile():
    file = open("customer.dat","ab")
    n=int(input("Enter customers:"))
    for i in range(n):
        CustomerNo = int(input("Enter customer number: "))
        Customer_Name = input("Enter customer Name: ")
    
        Amount = int(input("Enter amount: "))
        Date =input("Enter date: ")
        records = [CustomerNo, Customer_Name, Amount, Date]
        pickle.dump(records, file)


           

createFile()
        
    
    