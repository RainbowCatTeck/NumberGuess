import random

def user_input():
    print("Your input:")
    player_input = int(input())
    if player_input > 100 or player_input < 1:
        return "Please choose a number between 1 and 100"
    return player_input

def __main__():
    print("please enter your desired attempt number")
    random_number = random.randint(1, 100)
    attempts = int(input())
    print("your attempts:" + str(attempts))
    while attempts > 0:
        player_input = user_input()
        if player_input == random_number:
            print("Congrats")
            break
        elif player_input > random_number:
            attempts -= 1
            print("Your guess was too high \n You have one less attempt \n" + str(attempts))
        elif player_input < random_number:
            attempts -= 1
            print("Your guess was too low. \n You have one less attempt \n" + str(attempts))
    else:
        print("Game Over \n You have no attempts left \n The answer was: " + str(random_number))

__main__()