import json
name=input("Enter customer name to search:")
with open('customer-info.json','r') as outfile:
        j1=json.load(outfile)

def display_customer_details():
    if name in j1.keys():
        print("Details:")
        for i in j1[name]:
            print(i)
        
def display_total():
    total=0
    for a,value in j1.items():
        if name in a:
            for i in value:
                total=total+i[0]
            print("Total:",total)
                
                    
                
        
            

def main():
    display_total()
    display_customer_details()

main()

