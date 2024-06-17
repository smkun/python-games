import os
import subprocess

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
            subprocess.call(["python", "Hangman/Hangman.py"])
        elif choice == "2":
            subprocess.call(["python", "Landscaper/Landscaper.py"])
        elif choice == "3":
            subprocess.call(["python", "pong/pong.py"])
        elif choice == "4":
            subprocess.call(["python", "Tic-Tac-Toe/tic-tac-toe.py"])
        elif choice == "5":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()