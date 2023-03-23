# TIC-TAC-TOE-GAME

Python Project

### OBJECTIVE:
This project for EE-551 aims to develop a Tic Tac Toe game using python. It mainly consists of developing and implementing a computer program that plays Tic Tac Toe against another player.
In order to understand what Tic Tac Toe game is and how to play the game, below is the description.

### GAME DESCRIPTION:
Tic Tac Toe is a two-player game (one of them being played by computer or human). In this game, there is a board with 3 x 3 squares.

The two players take turns putting marks on a 3x3 board. The goal of Tic Tac Toe game is to be one of the players to get three same symbols in a row - horizontally, vertically or diagonally on a 3 x 3 grid.  The player who first gets 3 of his/her symbols (marks) in a row - vertically, horizontally, or diagonally wins the game, and the other loses the game. 
The game can be played by two players. There are two options for players: (a) Human  (b) Computer

### GAME RULES:
A player can choose between two symbols with his opponent, usual game uses “X” and “O”. 
1.	The player that gets to play first will get the "X" mark (we call him/her player 1) and the player that gets to play second will get the "O" mark (we call him/her player 2).

2.	Player 1 and 2 take turns making moves with Player 1 playing mark “X” and Player 2 playing mark “O”.

3.	A player marks any of the 3x3 squares with his mark (“X” or “O”) and their aim is to create a straight line horizontally, vertically or diagonally with two intensions:
a.	One of the players gets three of his/her marks in a row (vertically, horizontally, or diagonally) i.e. that player wins the game.
b.	If no one can create a straight line with their own mark and all the positions on the board are occupied, then the game ends in a  draw/tie.

### IMPLEMENTATION PLAN:
The implementation workflow for this project is as follows:

mport random
board = ['_' ,'_' ,'_',
         '_' ,'_' ,'_',
         '_' ,'_' ,'_',
        ]
current_player = 'X'

winner = None
game_running = True

In order to visualize the defined game rules and description, the game is shown in given code.

First the game will start with empty board>

def print_board():
    print('\n')
    print(board[0] +' | '+board[1]+' | '+board[2] +'\t' + '1 |2 |3')
    print(board[3] +' | '+board[4]+' | '+board[5] +'\t' + '4 |5 |6')
    print(board[6] +' | '+board[7]+' | '+board[8] +'\t' + '7 |8 |9')
    print('\n')

Then Player 1 will make his/her move by playing mark “X” on this board. Then Player 2 will make his/her move by playing mark “O” on this board. This will keep on continuing until the board is full of marks.

Then the program will check if Player 1 with “X” wins or Player 2 with “O” wins and that scenario will be follows: (could be vertically, horizontally or diagonally).  

if row_winner:
        winner = row_winner
        print(winner,'won')
    elif column_winner:
        winner = column_winner
        print(winner,'won')

If none of the players win, the program will check for draw.

elif diagonal_winner:
        winner = diagonal_winner
        print(winner,'won')
    else:
          winner = None

All this decision making is done by using Minimax algorithm.

#### Explanation with Example

To apply this, let's take an example from near the end of a game, where it is my turn. I am X. My goal here, obviously, is to maximize my end game score.
If the top of this image represents the state of the game when it is my turn, then I have some choices to make, there are three places I can play, one of which clearly results in me wining and earning the 10 points. If I don't make that move, O could very easily win. And I don't want O to win, so my goal here, as the first player, should be to pick the maximum scoring move.

#### Describing Minimax

The key to the Minimax algorithm is a back and forth between the two players, where the player whose "turn it is" desires to pick the move with the maximum score. In turn, the scores for each of the available moves are determined by the opposing player deciding which of its available moves has the minimum score. And the scores for the opposing players moves are again determined by the turn-taking player trying to maximize its score and so on all the way down the move tree to an end state.

A description for the algorithm, assuming X is the turn taking player:

* If the game is over, return the score from X's perspective.
* Otherwise get a list of new game states for every possible move.
* Create a scores list.
* For each of these states add the minimax result of that state to the scores list.
* If it's X's turn, return the maximum score from the scores list.
* If it's O's turn, return the minimum score from the scores list. 

Let's walk through the algorithm's execution with the full move tree, and algorithmically, how the instant winning move will be picked:

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

* It's X's turn in state 1. X generates the states 2, 3, and 4 and calls minimax on those states.
* State 2 pushes the score of +10 to state 1's score list, because the game is in an end state.
* State 3 and 4 are not in end states, so 3 generates states 5 and 6 and calls minimax on them, while state 4 generates states 7 and 8 and calls minimax on them.
* State 5 pushes a score of -10 onto state 3's score list, while the same happens for state 7 which pushes a score of -10 onto state 4's score list.
* State 6 and 8 generate the only available moves, which are end states, and so both of them add the score of +10 to the move lists of states 3 and 4.
* Because it is O's turn in both state 3 and 4, O will seek to find the minimum score, and given the choice between -10 and +10, both states 3 and 4 will yield -10.
* Finally the score list for states 2, 3, and 4 are populated with +10, -10 and -10 respectively, and state 1 seeking to maximize the score will chose the winning move with score +10, state 2.

Let's see what is happening here by looking through the possible move tree:
* Given the board state 1 where both players are playing perfectly, and O is the computer player. O choses the move in state 5 and then immediately loses when X wins in state 9.
* But if O blocks X's win as in state 3, X will obviously block O's potential win as shown in state 7.
* This puts two certain wins for X as shown in state 10 and 11, so no matter which move O picks in state 7, X will ultimately win.

Another important factor in this algorithm is depth. 

The key improvement to this algorithm, such that, no matter the board arrangement, the perfect player will play perfectly, is to take the "depth" or number of turns till the end of the game into account. Basically the perfect player should play perfectly, but prolong the game as much as possible.

So each time we invoke minimax, depth is incremented by 1 and when the end game state is ultimately calculated, the score is adjusted by depth.
 
Since this is a very complex algorithm, we have a computer to execute this algorithm.

### CODE IMPLEMENTATION

* In order to run this code, pygame library needs to be installed. To install this, open command prompt and type "import random".

* Run the complete code TicTacToe.ipynb.

* The game contains two buttons - vs Human and vs AI, so that we can choose our opponent. Once we click button, start playing game by clicking on the game board. Since we play first, we will be defined as Player X. 

* Once the game is finished, the message will be displayed on the game screen with either the winner name (X or O) or Draw game.
