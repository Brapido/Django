import tkinter as tk
from tkinter import ttk
import Notes
import TicTacToe as t
import budget


# change check sent back

def exitq():
    decide = input("Continue? ")
    if decide == "n":
        print("Goodbye!")
        return 1
    else:
        print("\n")
        return 0


def menu():
    print("What would you like to do?")
    print("1: Fibonacci sequence")
    print("2: Word scramble")
    print("3: Dictionary example")
    print("4: Play TicTacToe?")
    print("5: Work on the budget?")
    return int(input())


if __name__ == "__main__":
    # setup
    window = tk.Tk()
    window.title('Project')
    window.geometry('500x500')
    
    


    # run
    window.mainloop()


    loop = 0
    while loop == 0:
        choice = menu()
        match choice:
            case 1:
                print('This program outputs the\n'
                      'Fibonacci sequence step-by-step,\n'
                      'starting after the first 0 and 1.\n')
                x = int(input('How many steps would you like? '))
                Notes.fib(0, 1, x)
            case 2:
                word = input("Enter a word to be scrambled: ")
                Notes.scramble(word, "")
            case 3:
                Notes.dictionary()
            case 4:
                t.game()
            case 5:
                choice = ''
                # checking to make sure file is there and valid
                tempList = budget.readFile()
                # while loop goes until user chooses option 3 to quit.
                while True:
                    # Displaying main menu
                    budget.displayMenu()
                    choice = input("Please type 1, 2 or 3: ")
                    # calls input data from budget.py
                    if choice == '1':
                        budget.inputData(tempList)
                    # calls get data from budget.py
                    elif choice == '2':
                        budget.getData(tempList)
                    # quits the prog by breaking the loop
                    elif choice == '3':
                        print('Good bye')
                        break
                    # catches any invalid entry and starts the while loop over.
                    else:
                        print('Invalid option please try again.\n')
            case default:
                print("Invalid choice try again")

        loop = exitq()
