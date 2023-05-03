import random

def get_choice_name(choice):
    choices = {
        0: 'rock',
        1: 'paper',
        2: 'scissors',
        3: 'lizard',
        4: 'spock'
    }
    return choices[choice]

def get_choice_number(choice_name):
    choices = {
        'rock': 0,
        'paper': 1,
        'scissors': 2,
        'lizard': 3,
        'spock': 4
    }
    return choices[choice_name]

def winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player - computer) % 5 in [1, 3]:
        return 'player'
    else:
        return 'computer'

def play_game():
    print("Welcome to Rock-Paper-Lizard-Spock!")
    
    player_score = 0
    computer_score = 0

    while player_score < 2 and computer_score < 2:
        print("Please enter your choice:")
        
        while True:
            player_choice = input("rock, paper, scissors, lizard, or spock: ").lower()
            
            if player_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
                break
            else:
                print("Invalid choice, please try again.")
        
        computer_choice = random.randint(0, 4)
        
        print(f"\nPlayer chooses: {player_choice}")
        print(f"Computer chooses: {get_choice_name(computer_choice)}")
        
        result = winner(get_choice_number(player_choice), computer_choice)
        
        if result == 'tie':
            print("It's a tie!")
        elif result == 'player':
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print(f"Score: Player {player_score} - Computer {computer_score}\n")

if __name__ == "__main__":
    play_game()
