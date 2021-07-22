def main():
    data=open('customer-data.txt','w')
    Customer_Name=input("Enter name of customer:")
    Amount=input("Enter amount:")
    Date=input("Enter date:")

    data.write(Customer_Name)
    data.write(Amount)
    data.write(Date)

    data.close()

main()