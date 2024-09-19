# Tic - Tac - Toe
# define the board
def game():
    board = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

    # print the board
    def printboard(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self[0][0], self[0][1], self[0][2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self[1][0], self[1][1], self[1][2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self[2][0], self[2][1], self[2][2]))
        print("\t     |     |")
        print("\n")

    def checkwinner(currplayer, self):
        # Checking for the winner in the row
        for x in range(0, 3):
            if self[x][0] == self[x][1] == self[x][2] and self[x][0] != '-':
                if self[x][0] == currplayer:
                    print("{} is winner".format(currplayer))
                    return True
        # used to check the winner in column
        for y in range(0, 3):
            if self[0][y] == self[1][y] == self[2][y] and self[0][y] != '-':
                if self[0][y] == currplayer:
                    print("{} is winner".format(currplayer))
                    return True
        # used to check winner in one diagonal
        if self[0][0] == self[1][1] == self[2][2] and self[0][0] != '-':
            if self[0][0] == currplayer:
                print("{} is winner".format(currplayer))
                return True
        # used to check winner in another diagonal
        if self[0][2] == self[1][1] == self[2][0] and self[0][2] != '-':
            if self[0][2] == currplayer:
                print("{} is winner".format(currplayer))
                return True
        return False

    printboard(board)
    col = 0
    row = 0
    playerTurn = "X"

    for counter in range(1, 10):
        validMove = False
        while not validMove:
            col = 0
            row = 0
            while col < 1 or col > 3:
                col = int(input(playerTurn + " player, select a column 1-3: "))
                if col < 1 or col > 3:
                    print("The column must be between 1 and 3.")
            while row < 1 or row > 3:
                row = int(input(playerTurn + " player, select a row 1-3: "))
                if row < 1 or row > 3:
                    print("The row must be between 1 and 3.")
            col -= 1
            row -= 1
            if board[row][col] == '-':
                board[row][col] = playerTurn
                validMove = True
            else:
                print("Oops, that spot was already taken. Please select another spot.")
                validMove = False
                row = 0
                col = 0

        printboard(board)
        if checkwinner(playerTurn, board):
            break

        if playerTurn == "X":
            playerTurn = "O"
        else:
            playerTurn = "X"
