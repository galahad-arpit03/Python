height = input("Enter the height in meter  ")
weight = input("Enter the weight in kilograms  ")

bmi = int(weight) / float(height)**2
print("your BMI is ", int(bmi))


if bmi <18.5 :
    print("you are underweight")

elif bmi>=18.5 and bmi<=24.5 :
    print("you are Healthy")

else :
    print("you are overweight")


