import random

choices = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input('rock, paper, scissors?: ').lower()

    print('computer:', computer)
    print('player:', player)

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print("Player wins!")
    else:
        print("Computer wins!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Goodbye!")