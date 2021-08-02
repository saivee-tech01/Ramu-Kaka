import json
name=input("Enter customer name to search:")
with open('customer.json','r') as outfile:
        j1=json.load(outfile)

def display_customer_details():
    if name in j1.keys():
        print("Details:\n",j1[name])

def display_total():
    total=100
    if name in j1.keys():
        total=total+j1[name][0][0]
        print("Total:",total)

def main():
    display_total()
    display_customer_details()

main()

