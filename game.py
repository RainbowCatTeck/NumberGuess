from random import randint 

def user_input():
    print("Your input:")
    player_input = int(input())
    if player_input > 100 or player_input < 1:
        return "Please choose a number between 1 and 100"
    return player_input

def __main__():
    random_number = randint(1, 100)
    print("Please enter your desired attempt number")
    attempts = int(input())
    while attempts > 0:
        print("Your attempts:" + str(attempts))
        player_input = user_input()
        if player_input == random_number:
            print("Congrats")
            break
        elif player_input > random_number:
            attempts -= 1
            print("Your guess was too high \n You have one less attempt")
        elif player_input < random_number:
            attempts -= 1
            print("Your guess was too low. \n You have one less attempt")
    else:
        print("Game Over \n You have no attempts left \n The answer was: " + str(random_number))

__main__()