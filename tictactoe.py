#goal is to play tic tac toe
#first step is to create a board
#once board create X's and O's
#figure out where players want to go
#figure out who wins or draw
#
import numpy as np
board = np.chararray((3, 3))
rows, columns = board.shape
board[:] = "v"
print("Game Start:")
print(board)
#board[0,0] = "x"
#print(board)
gameover = False
turn = 0
#need to make all winning combos ie all horizontal,vertical,and both diagonals
winningcombos = [ [[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]], [[0,0],[1,1],[2,2]], [[2,0],[1,1],[0,2]] ]
while not gameover:
    #while game is active ask players what move they want
    #and repeat until win or draw
    #x will go on even turns and o will go on odd
    # modulo determines even or odd. Player X goes on even turns
    if turn % 2 == 0:
        xrow = input("Player X Row: ")
        xcol = input("Player X Col: ")
        #line 26 changes x row and x col from strings to integers
        #to index into board
        if board[int(xrow), int(xcol)] == b"v":
            board[int(xrow), int(xcol)] = "x"
            print(board)
        else:
            print("Player O is in Square")
            turn -= 1 # steiny's idea - good shit
    else:
        orow = input("Player O Row: ")
        ocol = input("Player O Col: ")
        print(board[int(orow), int(ocol)])
        if board[int(orow), int(ocol)] == b"v":
            board[int(orow), int(ocol)] = "o"
            print(board)
        else:
            print("Player X is in Square")
            turn -= 1
    #check to see if x or o won
    i = 0
    while not gameover and i < len(winningcombos):
        # get the positions for each tile in the winning postion
        xposone = winningcombos[i][0][0]
        yposone = winningcombos[i][0][1]
        xpostwo = winningcombos[i][1][0]
        ypostwo = winningcombos[i][1][1]
        xposthree = winningcombos[i][2][0]
        yposthree = winningcombos[i][2][1]
        # check if all winning tiles are x's
        if board[xposone][yposone] == b'x' and board[xpostwo][ypostwo] == b'x' and board[xposthree][yposthree] == b'x':
            gameover = True
            print("Player X wins")
        # check if all winning tiles are o's
        elif board[xposone][yposone] == b'o' and board[xpostwo][ypostwo] == b'o' and board[xposthree][yposthree] == b'o':
            gameover = True
            print("Player O wins")
        i += 1

    # scan through board and try to find a vacant tile
    vacantfound = False
    i = 0
    j = 0
    while not vacantfound and i < rows:
        # if vacant tile found, end loop
        if board[i][j] == b'v':
            vacantfound = True
        # else look in next column
        else:
            j += 1
        # if last column, switch to next row
        if j == columns:
            i += 1
            j = 0
    # if all tiles have been played and the game is over, end the game and say draw
    if not vacantfound and not gameover:
        gameover = True
        print("Draw Game")

    # next turn
    turn += 1

