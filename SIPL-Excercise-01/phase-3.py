def main():
    with open('customer-data.txt','a+') as f:


        Customer_Name=input("Enter name of customer:")
        Amount=input("Enter amount:")
        Date=input("Enter date:")

        f.write(Customer_Name+','+Amount+','+Date+'\n')
        f.close()

        

main()