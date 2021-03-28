# Tic Tac Toe game using python
board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' '
}

player = 1  #to initialise first player
total_moves = 0  #to count the moves
end_check = 0


def check():
    #checking the moves of player one
    #for horrizontal
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print('Player one won')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Player one won')
        return 1
    if board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X':
        print('Player one won')
        return 1

    #for vertical

    if board['T1'] == 'X' and board['M1'] == 'X' and board['B1'] == 'X':
        print('Player one won')
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['B2'] == 'X':
        print('Player one won')
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['B3'] == 'X':
        print('Player one won')
        return 1

    #for diagonal
    if board['T1'] == 'X' and board['M2'] == 'X' and board['B3'] == 'X':
        print('Player one won')
        return 1
    if board['T3'] == 'X' and board['M2'] == 'X' and board['B1'] == 'X':
        print('Player one won')
        return 1

    # checking the moves of player two
    # for horrizontal

    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
            print('Player one won')
            return 1
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
            print('Player one won')
            return 1
    if board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O':
            print('Player one won')
            return 1

    # for vertical

    if board['T1'] == 'O' and board['M1'] == 'O' and board['B1'] == 'O':
            print('Player one won')
            return 1
    if board['T2'] == 'O' and board['M2'] == 'O' and board['B2'] == 'O':
            print('Player one won')
            return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['B3'] == 'O':
            print('Player one won')
            return 1

    # for diagonal
    if board['T1'] == 'O' and board['M2'] == 'O' and board['B3'] == 'O':
            print('Player one won')
            return 1
    if board['T3'] == 'O' and board['M2'] == 'O' and board['B1'] == 'O':
            print('Player one won')
            return 1

    return 0





print('T1 |T2 |T3')
print('---+---+--')
print('M1 |M2 |M3')
print('---+---+--')
print('B1 |B2 |B3')
print('---+---+--')
print('****************************')
print()


while True:
    print(board['T1'] + '  | ' + board['T2'] + ' | ' + board['T3'])
    print('---+---+--')
    print(board['M1'] + '  | ' + board['M2'] + ' | ' + board['M3'])
    print('---+---+--')
    print(board['B1'] + '  | ' + board['B2'] + ' | ' + board['B3'])

    end_check = check()

    if total_moves == 9 or end_check == 1:
        break
    while True:  #input from the player
        if player == 1:  #to choose the player
            p1_input = input('player one: ')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            #on wrong input
            else:
                print('Invalid input, please try again!')
                continue
        else:
            p2_input = input('player two: ')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            # on wrong input
            else:
                print('Invalid input, please try again!')
                continue

    total_moves += 1
    print('****************************')
    print()

