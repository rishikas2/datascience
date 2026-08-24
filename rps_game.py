import random
while True:
    choices=('r','p','s')
    user_choice= input("Rock, Paper,Scissors (r, p, s)?: ").lower()
    computer_choice = random.choice(choices)
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 'p' and computer_choice == 'r') or \
        (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("Computer wins!")
    if input("Do you want to play again? (y/n): ").lower() != 'y':
        print("Thanks for playing!")

        break
    else:
        continue    