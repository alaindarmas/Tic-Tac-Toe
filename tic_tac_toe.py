import math  

#Initializes the board as a 3x3 grid with empty spaces
board = [[' ' for _ in range(3)] for _ in range(3)]

#Initializes the move counters for both players
playerXMoves = 0
playerOMoves = 0

#Used to print the current board state
def printBoard():
    for row in board:
        print(' '.join('_' if cell == ' ' else cell for cell in row))

#Checks if the specified player has won
def checkWinner(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

#Checks if the board is full (no empty cells)
def checkFullBoard():
    return all(cell != ' ' for row in board for cell in row)

#Minimax function to evaluate the best move for the computer
def minimax(isMaximizing):
    if checkWinner('X'):
        return -1
    if checkWinner('O'):
        return 1
    if checkFullBoard():
        return 0
    
    bestScore = -math.inf if isMaximizing else math.inf
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O' if isMaximizing else 'X'
                score = minimax(not isMaximizing)
                board[i][j] = ' '
                bestScore = max(score, bestScore) if isMaximizing else min(score, bestScore)
    return bestScore

#Used to make a move for the computer based on minimax evaluation
def computerMove():
    global playerOMoves
    bestScore = -math.inf
    bestMove = None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(False)
                board[i][j] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = (i, j)
    if bestMove:
        board[bestMove[0]][bestMove[1]] = 'O'
        playerOMoves += 1

#Used to allow the player to make a move
def playerMove():
    global playerXMoves
    while True:
        try:
            x, y = map(int, input("Enter your move as row and column (1-3 each, separated by space): ").split())
            if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == ' ':
                board[x - 1][y - 1] = 'X'
                playerXMoves += 1
                break
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter numbers only.")

#Main game function, controls the game flow
def playGame():
    print("Welcome to Tic-Tac-Toe!")
    printBoard()
    while True:
        playerMove()
        print("Your move:")
        printBoard()
        if checkWinner('X'):
            print("Congratulations, you won!")
            break
        if checkFullBoard():
            print("It's a draw!")
            break
        
        computerMove()
        print("Computer's move:")
        printBoard()
        if checkWinner('O'):
            print("Computer wins!")
            break
        if checkFullBoard():
            print("It's a draw!")
            break

    #Prints the number of moves made by each player
    print(f"Player X performed {playerXMoves} moves.")
    print(f"Player O performed {playerOMoves} moves.")

#Starts the game 
playGame()
