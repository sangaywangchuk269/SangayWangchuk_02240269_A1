import random

def menu_UI():
    print('1. Number Guessing game\n2. Rock, Paper, Scissor game\n3. Quit')

def num_game():
    print('Welcome, you have selected the secret number guessing game')
    secret_num = random.randint(1, 15)
    
    while True:
        user_input = input('Choose a secret number between 1 and 15 (type Q to quit): ')
        
        if user_input.lower() == 'q':
            print('Thank you for playing')
            break
        
        if not user_input.isdigit():
            print('Invalid input, please enter a number or Q to quit.')
            continue
        
        user_num = int(user_input)
        
        if user_num == secret_num:
            print('Congratulations, you have won the game! Type Q to reset the secret number.')
        elif user_num > secret_num:
            print('Your number is higher than the secret number.')
        else:
            print('Your number is lower than the secret number.')

def RPS_game():
    print("Choose the following option (1-3). Type 'Q' to quit the game.")
    print("1. Rock\n2. Paper\n3. Scissor")
    
    while True:
        choices = ['Rock', 'Paper', 'Scissor']
        user = input("Enter one of the above options: ")
        
        if user.lower() == 'q':
            print("Exiting Rock, Paper, Scissor game.")
            break
        
        if user not in choices:
            print("Invalid option, try again.")
            continue
        
        computer = random.choice(choices)
        print(f"Computer choice is {computer}")
        
        if user == computer:
            print("It's a tie!")
        elif (user == 'Rock' and computer == 'Scissors') or (user == 'Paper' and computer == 'Rock') or (user == 'Scissors' and computer == 'Paper'):
            print("Yes! You won!")
        else:
            print("Sorry, you lose.")

def main():
    menu_UI()
    user_input = input('What option do you wish to choose: ')
    
    if user_input == '1':
        num_game()
    elif user_input == '2':
        RPS_game()
    elif user_input == '3':
        print('Quitting the game')
        pass
    else:
        print('Invalid input')


main()
