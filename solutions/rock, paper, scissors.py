import random


def input_choice():
    while True:
        user_input = input('Welcome to rock, paper, scissor game please Enter\n1(or r) for rock\n2(or p) for '
                           'paper\n3(or s) ''for scissor ')
        if str(user_input).isdigit() and int(user_input) in [1, 2, 3]:
            return int(user_input) - 1
        elif user_input.isalpha():
            return {'r': 0, 'p': 1, 's': 2}[user_input.lower()]
        else:
            print('please enter valid input')


def game():
    while True:
        player = input_choice()
        computer = random.randint(0, 2)     # random.choice(options) - 1
        print(f"\nYour choice is {convert[player]} and computer's choice is {convert[computer]}")
        print(determine_winner(player, computer))

        while True:
            x = str(input('\nDo you want to play again(y/n)')).lower()
            if x in ['y', 'yes', '', 'n', 'no']:
                break
            else:
                print('you must enter valid choices')

        if x == 'y' or x == 'yes' or x == '':
            print('\nPlaying again...\nAgain ',end='')
            continue
        elif x == 'n' or x == 'no':
            print('Exiting the game...')
            return None


determine_winner = lambda player_, computer_: result_graph[computer_][player_]

#                    rock         paper     scissor
result_graph = [['It\'s a draw', 'You won', 'You lose'],  # rock
                ['You lose', 'It\'s a draw', 'You won'],  # paper
                ['You won', 'You lose', 'It\'s a draw']  # scissor
                ]
convert = {0: 'rock', 1: 'paper', 2: 'scissor'}
game()
