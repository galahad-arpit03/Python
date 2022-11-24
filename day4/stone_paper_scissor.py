import random 

user_choice = int (input("What do you choose ? \n type 0 for rock,  1 for paper,  2 for Scissors \n "))

computer_chioce = random.randint(0, 2) 
if computer_chioce == user_choice:
    print(f"Computer choose  {computer_chioce}")    
    print("it's a draw")

elif user_choice == 0 and computer_chioce ==2 :
    print(f"Computer choose  {computer_chioce}")  
    print("You win")

elif computer_chioce > user_choice :
    print(f"Computer choose  {computer_chioce}")  
    print ("you loose")

elif user_choice > 3 :
    print ("Wrong Input")
    
elif computer_chioce < user_choice: 
    print(f"Computer choose  {computer_chioce}")  
    print ("You win")


else :
    print("nothing")