number= int(input("enter the number"))
choice=input("factoriel or even or odd (f/e)") 
if choice=="f" :
    r=1
    t=number
    while t>0:
        r=r*t
        t=t-1
    print(f"{number}:{r}")
    
elif choice=="e":
    if number%2==0:
       print("even")
    else:
        print("odd")
"""elif choice == "e":
    if number%2!=0:
       print ("odd")"""