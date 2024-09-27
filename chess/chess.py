

board_state = [
    ['r', 'n' , 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p']*8,
    ['.']*8,
    ['.']*8,
    ['.']*8,
    ['.']*8,
    ['P']*8,
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
] # this is from white's side


def print_board():
    global board_state

    print()
    print()

    print('\t', end='')
    for ls in board_state:
        for item in ls:
            print(item + ' ', end='')
        
        print()
        print('\t', end='')



##################

move_num = 0
turn = 0 # 0 for white, 1 for black
game = True # is the game running? True --> Not checkmate/stalemate/3-fold



### game loop ####

# start game
# take input move


