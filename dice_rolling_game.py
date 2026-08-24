import random
while True:
    choice = input("Roll the dice?(y/n):")
    if choice =='y' or choice =='Y':
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        print(f"You rolled a", ({(roll1,roll2)}))
    elif choice =='n' or choice =='N':
        print("Game over. Thanks for playing!")
        break