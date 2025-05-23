import random
gsd_dgt=random.randint(1,50)
lives=10

print("Welcome to number guessing game \n ")
mode=input("Do you want to play in \'easy\' or \'hard\' mode : ").lower()

if mode=='hard':
        lives=5


while lives>0:
    
    try:
        ui=int(input("Enter a number between 1 and 50 : "))
    except ValueError:
        print("enter a valid input")
        continue
    
    if ui not in range(1,51):
        print("the number should be between 1 and 50 ")
        continue
    
    if ui>gsd_dgt:
        lives-=1
        print("your guess is higher ")
        print(f"you have {lives} guesses left")
    elif ui<gsd_dgt:
        lives-=1
        print("your guess is lower ")
        print(f"you have {lives} guesses left")
    elif ui ==gsd_dgt:
        print("You won")
        exit()
    
else:
    print("Lives over . you lose!!")