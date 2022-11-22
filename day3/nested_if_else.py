# program to check the elegiblity of person to ride

age = int(input("Enter your age "))
height = int(input("Enter your height in centimeter"))

if height > 120 :
    print("You can ride")

    if age <=18 :
        print ("You must pay $7")
    else :
        print ("you must pay $12")

else :
    print("you cannot ride")