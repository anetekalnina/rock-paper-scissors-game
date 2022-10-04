import random
turns = ['rock', 'paper', 'scissors']
human_turns = []
computer_turns = []

while(True):
    human_turn = input('Your turn or type exit: ')
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('Thank you for playing!')
        break

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    print(f'You: {human_turn} vs. Computer: {computer_turn}')
    if human_turn == computer_turn:
        print ('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print ('You win!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print ('You win!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print ('You win!')
    else:
        print ('You lose!')

print(f'You have played {len(human_turns)} times')
print(human_turns)
print(computer_turns)
