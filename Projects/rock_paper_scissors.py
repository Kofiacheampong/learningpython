import random

choices = ['rock', 'paper', 'scissors']
user_wins = 0
computer_wins = 0

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, scissors? or Q to quit: ').lower()
        if player == 'q':
            break

    print('computer:', computer)
    print('player:', player)

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print("Player wins!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break
print(f'You won {user_wins}, times')
print(f'Computer {computer_wins}, times')

print("Goodbye!")