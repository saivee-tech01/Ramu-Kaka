msg=''' Software: Please select the desired option:
  1. Addition
  2. Substraction
  3. Multiplication
  4. Division'''
print(msg)
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
        

    
    

