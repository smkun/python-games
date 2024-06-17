import os
from Hangman.Hangman import play_hangman
from Landscaper.Landscaper import main as play_landscaper
from pong.pong import main as play_pong
from Tic_Tac_Toe.tic_tac_toe import play_game as play_tic_tac_toe

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main_menu():
    while True:
        clear_screen()
        print("=== Main Menu ===")
        print("1. Hangman")
        print("2. Landscaper")
        print("3. Pong")
        print("4. Tic-Tac-Toe")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            play_hangman()
        elif choice == "2":
            play_landscaper()
        elif choice == "3":
            play_pong()
        elif choice == "4":
            play_tic_tac_toe()
        elif choice == "5":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()