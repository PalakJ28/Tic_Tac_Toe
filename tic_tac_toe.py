import random
board = ['_' ,'_' ,'_',
         '_' ,'_' ,'_',
         '_' ,'_' ,'_',
        ]
current_player = 'X'

winner = None
game_running = True

def print_board():
    print('\n')
    print(board[0] +' | '+board[1]+' | '+board[2] +'\t' + '1 |2 |3')
    print(board[3] +' | '+board[4]+' | '+board[5] +'\t' + '4 |5 |6')
    print(board[6] +' | '+board[7]+' | '+board[8] +'\t' + '7 |8 |9')
    print('\n')

s=[]
def handle_turn(player):
    while game_running:
        print('\n')
        print(player + "'s turn.")
        position = input('Choose a position from 1-9: ')
        valid = False
        while not valid:
            while position not in ['1','2','3','4','5','6','7','8','9']:
                position = input('Choose a position from 1-9: ')
            if position != s:
                x = int(position) - 1
                if board[x] == '_':
                    s.append(int(position))
                    board[x] = player
                    valid = True
                else:
                    position = input('Choose a position from 1-9: ')
        board[x] = player
        print_board()
        return player


def compuer_flip_player():
    global current_player
    if current_player == 'X':
        random_place(board, current_player)
        current_player = '0'
    elif current_player == '0':
        handle_turn(current_player)
        current_player = 'X'


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    elif current_player == '0':
        current_player = 'X'


def random_place(board, player):
    while game_running:
        # print('computers turn')
        l=[0,1,2,3,4,5,6,7,8]
        current_loc = str(random.choice(l))
        current_loc = int(current_loc)
        x = int(current_loc) - 1
        if current_loc in s:
            continue
        else:
            print('computers turn:',current_loc)
            s.append(current_loc) 
            board[x] = player
            print_board()
            return(board)
   

def check_row():
    global game_running
    row_1 = board[0] == board[1] == board[2] != '_' 
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'
    if row_1 or row_2 or row_3:
        game_running = False   
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_column():
    global game_running
    column_1 = board[0] == board[3] == board[6] != '_'  
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'
    if column_1 or column_2 or column_3:
        game_running = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonal():
    global game_running
    diagonal_1 = board[0] == board[4] == board[8] != '_'    
    diagonal_2 = board[2] == board[4] == board[6] != '_'
    if diagonal_1 or diagonal_2:
        game_running = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def tie():
    global game_running
    if "_" not in board:
        game_running = False
        print("Tie.")
        return True
    else:
        return False

def check_winner():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
        print(winner,'won')
    elif column_winner:
        winner = column_winner
        print(winner,'won')
    elif diagonal_winner:
        winner = diagonal_winner
        print(winner,'won')
    else:
          winner = None


def play():
    print_board()
    while game_running:
        # print_board()
        handle_turn(current_player)
        # game_over()
        check_winner()
        tie()
        flip_player()


def computer_play():
    print_board()
    while game_running:
        compuer_flip_player()
        check_winner()
        tie()
       

while True:
    choice = input('1.Player vs Player\n2.Player vs Computer\n3.Smart play\n4.Quit\nEnter your choice:')
    if choice.isnumeric()==True:
        choice=int(choice)
        if choice == 1:
            play()
            break
        elif choice == 2:
            game_running = True
            computer_play()
            break
        elif choice == 3:
            board = [' ' for x in range(10)]

            def insertLetter(letter, pos):
                board[pos] = letter

            def spaceIsFree(pos):
                return board[pos] == ' '

            def printBoard(board):
                print('\n')
                print(board[1] + ' | ' + board[2] + ' | ' + board[3]+'\t' + '1 |2 |3')
                print(board[4] + ' | ' + board[5] + ' | ' + board[6]+'\t' + '4 |5 |6')
                print(board[7] + ' | ' + board[8] + ' | ' + board[9]+'\t' + '7 |8 |9')
                print('\n')
       

            def isWinner(bo, le):
                return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
                        (bo[4] == le and bo[5] == le and bo[6] == le) or 
                        (bo[1] == le and bo[2] == le and bo[3] == le) or 
                        (bo[1] == le and bo[4] == le and bo[7] == le) or  
                        (bo[2] == le and bo[5] == le and bo[8] == le) or 
                        (bo[3] == le and bo[6] == le and bo[9] == le) or 
                        (bo[1] == le and bo[5] == le and bo[9] == le) or  
                        (bo[3] == le and bo[5] == le and bo[7] == le))


            def playMove():
                run = True
                while run:
                    move = input('Please select a position between 1-9 ')
                    if move.isnumeric()== False:
                        continue
                    else:
                        move = int(move)
                        if move > 0 and move < 10 :
                            if spaceIsFree(move):
                                run = False
                                insertLetter('X', move)
                            else:
                                print('This space is occupied')
                        else:
                            print('Please choose between 1-9')


            def compMove():
                possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
                move = 0
                for move in range(1,9):
                    for let in ['0','X']:
                        for i in possibleMoves:
                            boardCopy = board[:]
                            boardCopy[i] = let
                            if isWinner(boardCopy, let):
                                move = i
                                return move
                if 5 in possibleMoves and spaceIsFree(5):
                    move = 5 
                    return move
                if 5 not in possibleMoves and spaceIsFree(1):
                    move = 1
                    return move       
                if board[1] == board[2] == 'X' and spaceIsFree(3):
                    move = 3
                elif board [1] == board [4] == 'X' and spaceIsFree(7):
                    move = 7
                elif board [1] == board [7] == 'X' and spaceIsFree(4):
                    move = 4
                elif board [1] == board [5] == 'X' and spaceIsFree(9):
                    move = 9
                elif board [2] == board [5] == 'X' and spaceIsFree(8):
                    move = 8
                elif board [4] == board [5] == 'X' and spaceIsFree(6):
                    move = 6
                elif board [6] == board [5] == 'X' and spaceIsFree(4):
                    move = 4
                elif board [3] == board [5]== 'X' and spaceIsFree(7):
                    move = 7
                elif board [7] == board [8] =='X' and spaceIsFree(9):
                    move = 9
                elif board [9] == board [8]== 'X' and spaceIsFree(7):
                    move = 7
                elif board [3] == board [6]== 'X' and spaceIsFree(9):
                    move = 9
                elif board [3] == board [5] =='X' and spaceIsFree(7):
                    move = 7
                elif board [3] == board [2] == 'X' and spaceIsFree(1):
                    move = 1
                elif board[1] == 'X' and spaceIsFree(5):
                    move = 5
                elif board[5] == 'X' and spaceIsFree(1):
                    move = 1
                elif spaceIsFree(9):
                    move = 9
                return move

            def isBoardFull(board):
                if board.count(' ') > 1:
                    return False
                else:
                    return True

            def smart():
                choice = int(input('1.Player has first chance\n2. Computer has first chnace\nEnter choice:'))
                if choice == 1:
                    printBoard(board)
                    while not(isBoardFull(board)):
                        if not(isWinner(board, '0')):
                            playMove()
                            printBoard(board)
                        else:
                            print('Sorry,Computer won! ')
                            break
                        if not(isWinner(board, 'X')):
                            move  = compMove()
                            if move == 0:
                                print('Tie game')
                            else:
                                insertLetter('0', move)
                                print('Computer move:', move)
                                printBoard(board)
                        else:
                            print('Player won.')
                            break
                    if isBoardFull(board):
                        print('Tie game')
                elif choice == 2:
                    printBoard(board)
                    while not(isBoardFull(board)):
                        if not(isWinner(board, 'X')):
                            move  = compMove()
                            if move == 0:
                                print('Tie game')
                            else:
                                insertLetter('0', move)
                                print('Computer move:', move)
                                printBoard(board)
                        else:
                            print('Player won.')
                            break
                        if not(isWinner(board, '0')):
                            playMove()
                            printBoard(board)
                        else:
                            print('Sorry,Computer won! ')
                            break
                    if isBoardFull(board):
                        print('Tie game')
                else:
                    print('please enter valid choice')

            smart()
            break
        elif choice == 4:
            break
        else:
            print('Please select valid choice')
    else:
        print('Please enter number')
        continue