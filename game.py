import sys
import random

def play():
    while True:
        p_choice = str(input("Welcome, which pokemon would you like to choose?\n'1': 'Charmander'\n'2':'Squirtle'\n"
                             "'Bulbasur': '3'"))
        if p_choice == '1':
            p_choice = 'Charmander'
        elif p_choice == '2':
            p_choice = 'Squirtle'
        elif p_choice == '3':
            p_choice = 'Bulbasur'
# Computer part
        cpu_random = random.randint(1,3)
        cpu_choice = cpu_random
        if cpu_random == 1:
            cpu_choice = "Charmander"
        elif cpu_random == 2:
            cpu_choice = 'Squirtle'
        elif cpu_random == 3:
            cpu_choice = 'Bulbasur'


        def battle():

            play_again = None

            if p_choice == cpu_choice:
                print("{} and {} have the same power so they started to mingle about thier powers".format(cpu_choice, p_choice))

            elif p_choice == 'Charmander' and cpu_choice == 'Squirtle':
                print("{} used water splash to wash down to wash down the fire of {}".format(cpu_choice,p_choice))
                play_again = input("Do you want to play again?")
            elif p_choice == 'Charmender' and cpu_choice == 'Bulbasur':
                print("{} has burned into a crisp because of fire flames from {}".format(cpu_choice, p_choice))
                play_again = input("Do you want to play again?")


            elif p_choice == 'Bulbasur' and cpu_choice == 'Charmander':
                print("{} wins".format(cpu_choice))
                play_again = input("Do you want to play again?")
            elif p_choice == 'Bulbasur' and cpu_choice == 'Squirtle':
                print("{} wins!".format(p_choice))
                play_again = input("Do you want to play again?")



            elif p_choice == "Squirtle" and cpu_choice == "Bulbasur":
                print('{} wins'.format(cpu_choice))
                play_again = input("Do you want to play again?")
            elif p_choice == 'Squirtle' and cpu_choice == "Charmander":
                print("{} wins".format(p_choice))
                play_again = input("Do you want to play again?")

            if play_again == "yes" and "y" and "Yes":
                play()
            elif play_again == 'No':
                print("Game Over!")
                sys.exit()
            else:
                print("Please try again")
                play_again = input("play again?")
                return play_again

        battle()


def start_game():
    while True:
        begin = input("Would you like to play pokemon(y/n): ")
        if begin == 'y':
            play()
            return begin
        while begin != 'y':
            if begin == 'n':
                print("Game Over")
                return begin
            else:
                print('Please try again')
                break

start_game()


