import sys
import csv

# setting my preset budget file
fName = 'budget.csv'


# -----------------------------------------------------------
# This function reads the file and makes sure that its valid otherwise it will close
def readFile():
    try:
        budget = []
        with open(fName, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                budget.append(row)
            return budget
    except FileNotFoundError as error:
        print(f'Could not find {fName} file.\n', error)
        print('Closing program')
        sys.exit()
    except Exception as e:
        print(type(e), e)
        print('Closing program')
        sys.exit()


# -----------------------------------------------------------
# Displays initial menu options
def displayMenu():
    print('Option 1: Input')
    print('Option 2: Get')
    print('Option 3: Quit')


# -----------------------------------------------------------
# Takes input from user to add data to csv file.  Requests who bought the item
# and how much it is.  If an invalid option is selected prog will loop back to
# beggining.
def inputData(self):
    choice = input('Who made the transaction (1)Mom or (2)Dad?: ')
    if choice == '1':
        itCost = input('How much did the it cost? ')
        if itCost.isdigit():
            tempList = ['mom', itCost]
            self.append(tempList)
            AddToFile(self)
            print()
        else:
            print('Invalid cost, start over.\n')
    elif choice == '2':
        itCost = input('How much did the it cost? ')
        if itCost.isdigit():
            tempList = ['dad', itCost]
            self.append(tempList)
            AddToFile(self)
            print()
        else:
            print('Invalid cost, start over.\n')
    else:
        print('Invalid parent.  Try again.\n')
        return


# -----------------------------------------------------------
# Takes list as input and writes to csv file.
def AddToFile(self):
    try:
        with open(fName, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self)
    except Exception as e:
        print(type(e), e)
        print('Closing program')


# -----------------------------------------------------------
# Takes user input and sums up total spent or total spent by either pareny by enumerating
# through csv file.
def getData(self):
    choice = getDataMenu()
    total = 0
    if choice == '1':
        for i, self in enumerate(self, start=1):
            total = total + int(self[1])
        print(f'The total spent is : ${total}\n')
    elif choice == '2':
        parent = input('Which parent (1)Mom or (2)Dad: ')
        if parent == '1':
            for i, self in enumerate(self, start=1):
                if self[0].lower() == 'mom':
                    total = total + int(self[1])
            print(f'The total Mom spent is : ${total}\n')
        elif parent == '2':
            for i, self in enumerate(self, start=1):
                if self[0].lower() == 'dad':
                    total = total + int(self[1])
            print(f'The total Dad spent is : ${total}\n')
        else:
            print('Invalid choice, Start over!')
    elif choice == '3':
        return
    else:
        print('Invalid option, Start over!')


# -----------------------------------------------------------
# Displays sub menu for getting data
def getDataMenu():
    print('1: Total spent overall')
    print('2: Total spent by Mom or Dad')
    print('3: Quit')
    choice = input('What would you like to get? 1, 2 or 3: ')
    return choice
# -----------------------------------------------------------
