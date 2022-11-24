num1 = int ( input("Enter the number by where you want to print"))

for i in range (1,num1+1,1):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")

    elif ( i%3==0):
        print("fizz")

    elif (i%5 == 0):
        print("Buzz")
    else :
        print (i)


    
    
    
    
