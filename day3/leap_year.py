year = int(input("Enter any year you want to check :  "))

if year%4 == 0 :
    if year%100==0:
        if year%4==0 :
            print("Leap Year")
        else :
            print("Not a Leap Year")
    else:
            print ("Leap Year")

else :
    print("Not a Leap Year")