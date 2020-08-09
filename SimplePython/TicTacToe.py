######################################################################
#
# Given n = 3, assume that player 1 is "X" and player 2 is "O"
# board = TicTacToe(3);
#
# board.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
#
# board.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
#
# board.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
#
# board.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
#
# board.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
#
# board.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
#
# board.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
#
######################################################################

M = 3
board = [['-'] * M for i in range(M)]
move = ""
player = 1


def gameState(x):
    if x == 'X':
        return 1
    elif x == 'O':
        return 0
    else:
        return 99


def gameEnded():
    noMove = False
    # If no more moves to play
    for i in range(M):
        if '-' not in board[i]:
            noMove = True
        else:
            noMove = False
    if noMove:
        print("----NO MORE MOVES TO PLAY----")
        return True

    # Row Check
    for i in range(M):
        res = sum(list(map(gameState, board[i])))
        if res == 3 or res == 0:
            return True

    # Column Check
    for i in range(M):
        col = []
        for j in range(M):
            col.append(board[j][i])
        res = sum(list(map(gameState, col)))
        if res == 3 or res == 0:
            return True

    # Diagnal Check-1
    diag = [board[i][i] for i in range(M)]
    res = sum(list(map(gameState, diag)))
    if res == 3 or res == 0:
        return True

    # Diagnal Check-2
    row = [i for i in range(M)]
    col = row[::-1]
    diag = [board[row[i]][col[i]] for i in range(M)]
    res = sum(list(map(gameState, diag)))
    if res == 3 or res == 0:
        return True


def printState():
    print("  0 1 2")
    for i in range(M):
        arr = []
        for j in range(M):
            arr.append(board[i][j])
        print(str(i) + " " + " ".join(arr))
    print("-------------------------------------")


def markMove(row, col, player):
    if board[row][col] == '-':
        print(move)
        if player == 1:
            board[row][col] = 'X'
        else:
            board[row][col] = 'O'
    else:
        print("INVALID MOVE. TRY AGAIN!!")
    printState()


def declareWinner():
    # If no more moves to play
    for i in range(M):
        if '-' in board[i]:
            print("WINNER IS " + move)
            return None
    print("DRAW MATCH!")


while not gameEnded():
    turn = list(map(int, input("Enter your turn in [row col] format: ").rstrip().split()))
    player = 1 - player
    move = "Player-" + str(player + 1)
    markMove(turn[0], turn[1], player + 1)

declareWinner()
