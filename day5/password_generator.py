import random 
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!","#","$","%","&","(",")","*","+"]

print ("Welcome to the random password generator!")
letters_in = int(input("How many Letters do you want in your password  "))
numbers_in = int(input("How many Numbers do you want in your password  "))
symbols_in = int(input("How many Symbols do you want in your password  "))

password_list = []
for char in range (1,letters_in+1):
   password_list.append(random.choice(letters))
    

for char in range (1,numbers_in+1):
       password_list.append(random.choice(numbers))


for char in range (1,symbols_in+1):
       password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)   
print(password_list)

password = ""
for char in password_list:
    password+=char

print("your password is :" ,password)
