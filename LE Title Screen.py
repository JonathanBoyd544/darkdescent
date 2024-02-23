import os
import time
import sys

##### Title Screen #####
def title_screen_selections():
    option = input("==> ").lower()
    if option == ("play"):
        setup_game() #placeholder until written
    elif option == ("help"):
        help_menu()
    elif option == ("quit"):
        sys.exit()
    while option not in ['play', 'help', 'quit']:
        print("Invalid command. Please try again.")
        option = input("==> ")
        if option == ("play"):
            setup_game() #placeholder until written
        elif option == ("help"):
            help_menu()
        elif option == ("quit"):
            sys.exit()
            
def title_screen():
    os.system('cls')
    print("##############################")
    print("###### Labyrinth's Edge ######")
    print("##############################")
    print("           -Play-            ")
    print("           -Help-            ")
    print("           -Quit-            ")
    print("Copyright 2024 JB Productions")
    print("")
    title_screen_selections()

def help_menu():
    os.system('cls')
    print("Insert help text here.")
    option = input("==> ").lower
    if option == ("menu"):
        pass
             
    else:
         pass
    
while(True):
    title_screen()

