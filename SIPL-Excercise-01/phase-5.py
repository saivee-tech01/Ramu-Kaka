import json
name=input("Enter customer name to search:")

with open('customer-info.json','r') as outfile:
        j1=json.load(outfile)

j2={
    "Aisha" : "Saivee",
    "Bittu" : "Rishabh"
}


def map_func():
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



map_func()
