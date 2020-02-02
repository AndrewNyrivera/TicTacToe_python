import random 

#Set the board up With parameters board
def board_game(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])

#Little test below | CHECK!
# boardy = ['X','O','X','O','X','O','X','O','X','O']
# board_game(boardy)

#Set ask for the character symbol 
def character_symbol():
    player = input("Player 1 choose a character X or O?: ").upper()
    if player == 'X':
        return ('X','O')
    if player == 'O':
        return ('O','X')
    else:
        return character_symbol()

#Little test below | CHECK!
# player1,player2 = character_symbol()
# print(player1)
# print(player2)

#Check if the position is available 
def space_available(board,position):
    return board[position] == ' '

#Little test below | CHECK!
# boardy2 = ['X','O',' ','O','X','O',' ','O',' ','O']
# board_game(boardy2)
# print(space_available(boardy2,9))

#Set the position 
def character_position(board):
    try:
        position = int(input('Player choose a position between (1-9): '))
        while position in range(1,10) and space_available(board,position) == True:
            return position
        else:
            return character_position(board)
    except:
        return character_position(board)

#Little test below | CHECK!
# boardy4 = ['X','O','X','O','X','O',' ','O','X','O']
# board_game(boardy3)
# print(character_position(boardy3))

#Set the position_marker parameters(board,position,mark)
def position_marker(board,position,mark):
    board[position] = mark

#Little test below | CHECK!
# boardy5 = ['X','O','X','O','X','O',' ','O','X','O'] 
# position_marker(boardy3,6,'$')
# board_game(boardy3)

#Set the coin_flip to choose who goes first
def coin_flip():
    coins_flip = random.randint(0,1)
    if coins_flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Little test below | CHECK!
# print(coin_flip())

#Set win_check with the parameters(board,mark)
def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark) or #first across
    (board[4]==board[5]==board[6]==mark) or #Second across
    (board[7]==board[8]==board[9]==mark) or #Third across 
    (board[1]==board[4]==board[7]==mark) or #First down
    (board[2]==board[5]==board[8]==mark) or #Second down
    (board[3]==board[6]==board[9]==mark) or #Third down
    (board[1]==board[5]==board[9]==mark) or # First diagnol 
    (board[3]==board[5]==board[7]==mark))

#Little test below | CHECK!
# boardy6 = ['X','O','X','O','X','O',' ','O','X','O'] 
# board_game(boardy6)
# print(win_check(boardy6,'O'))

#Set full board check with parameters(board)
def full_board_check(board):
    for i in range(1,10):
        if space_available(board,i) == True:
            return False
    return True

#Little test below | CHECK!
# boardy7 = ['X','O','X','O','X','O','X','O','X',' '] 
# board_game(boardy7)
# print(full_board_check(boardy7))

#Set Replay function
def replay():
    play_again = input('Want to play again? Y or N: ').upper()
    if play_again == 'Y':
        return True
    else:
        return False

#little test below | CHECK!
# print(replay())

#Set everything up

print('Welcome to my Tic Tac Toe Game!')

choice = coin_flip()
play_game = input('Want to play a game? Y or N: ').upper()

while True:
    gamy_board = [' ']*10
    
    if play_game == 'Y':
        game_on = True
        player1,player2 = character_symbol()
    else:
        game_on = False
    
    while game_on:
        #Player 1 
        if choice == 'Player 1':

            print('\n'*100)
            print(f'Player 1: {player1}')
            board_game(gamy_board)
            position = character_position(gamy_board)
            position_marker(gamy_board,position,player1)

            if win_check(gamy_board,player1) == True:
                print(f'Player 1 has won: {player1}')
                break
            if full_board_check(gamy_board):
                print('Tie Game!')
                break
            else:
                choice = 'Player 2'
        

        #Player 2 
        if choice == 'Player 2':

            print('\n'*100)
            print(f'Player 2: {player2}')
            board_game(gamy_board)
            position = character_position(gamy_board)
            position_marker(gamy_board,position,player2)

            if win_check(gamy_board,player2) == True:
                print(f'Player 2 has won: {player2}')
                break
            if full_board_check(gamy_board):
                print('Tie Game!')
                break
            else:
                choice = 'Player 1'


    if replay() == False:
        break
    else:
        True
