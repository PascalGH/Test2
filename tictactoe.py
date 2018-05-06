import random


def reset(size):
    # Creates a bi-dimensional table filled with zeroes for which size is provided as parameter
    global table
    for i in range(0,size):
        raw = []
        for j in range(0,size):
            raw.append(0)
        table.append(raw)
    return table


def is_empty(line, raw):
    # Returns true if a cell in the table is empty
    global table
    return table[line - 1][raw - 1]== 0


def is_full():
    # Returns True is at least one cell in the table is empty (i.e. contains a '0')
    global table
    for i in range(0, len(table)):
        for j in range(0, len(table)):
            if table[i][j] == 0:
                return False
    return True


def mark(player, raw, column):
    # Marks a cell with the value corresponding to a player
    global table
    # The value of the mark is corresponding to the second position of the list corresponding to the player
    table[raw - 1][column -1] = player[1]
    return table


def show():
    # Displays the table
    global table
    # Clearing the screen
    print('\n' * 100)
    # Print lines in reverse order, so that the last one appears at the top of the display
    for i in range(len(table) - 1, -1, -1):
        print(i + 1, end='  {} '.format(chr(124)))
        # Maps values to characters and decorates with vertical lines
        # The id of each line is also printed to help the players provide coordinates
        for j in range(0,len(table[0])):
            if table[j][i] == 1:
                print('X', end=' {} '.format(chr(124)))
            elif table[j][i] == -1:
                print('O', end=' {} '.format(chr(124)))
            else:
                print(' ', end=' {} '.format(chr(124)))
        print('\n')
        # Prints the name of columns to help the players to provide coordinates
    print('     1   2   3   4\n')


def line_h(player, raw):
    # Determines if the table contains a vertical line for the player given as input
    global table
    # The check is made on the sum of 1 or -1 compared with the length of the table multiplied by the same number
    return sum(table[raw]) == len(table) * player[1]


def line_v(player, column):
    # Determines if the table contains an horizontal line for the player given as input
    global table
    result = 0
    # Looping through all lines associated to that column
    for line in range(0,len(table)):
        result += table[line][column]
    return result == len(table) * player[1]


def line_x(player):
    # Determines if the table contains a crossing line for the player given as input
    global table
    result1, result2 = 0, 0
    # Checking the two cross-lines
    for i in range(0,len(table)):
        # From bottom left to top right
        result1 += table[i][len(table) - i -1]
        # From bottom right to top left
        result2 += table[len(table) - i -1][i]
    return result1 == len(table) * player[1] or result2 == len(table) * player[1]


def win(player):
    # Checks is one line has been built in the table for the player
    global table
    for i in range(0, len(table)):
        if line_h(player, i) or line_v(player, i):
            return True
    if line_x(player):
        return True
    return False


def setup():
    # Gathers the name of the players, and returns one list for each
    # The fist item in the list is the name of the layer, the second is the sign associated to the player in the table
    # The thrid is the visual associated to the sign in the representation ('X' or 'O'
    player1 = input('Name of player 1: ')
    player2 = input('name of player 2: ')
    return([player1, 1, 'X'], [player2, -1, 'O'])


def play (player):
    # Allow a player to play by providing the coordinated in the table of the cell he wants to mark
    global table
    # Capturing the input from the user - Returns false will help to exit the main loop
    i = input('{} enter x, y: '.format(player[0]))
    if i == '':
        return False
    # Gathering the coordinates of the cell by spitting around the ',' sign
    (x,y) = i.split(',')
    x = int(x)
    y = int(y)
    # Checking that line and raw are in the limit of the table's size
    if x in range(0, len(table) + 1) and y in range(0, len(table) + 1):
        # Check that the cell is empty before marking it
        if is_empty(x, y):
            mark(player, x, y)
            show()
        else:
            print('The cell is already filled, you loose your turn')
    else:
        print('The pick is out of range, you loose your turn')
    return(True)


# Creating and dimensioning the table
table = []
table = reset(4)
# Initializing the players
(player1, player2) =setup()
players = [player1, player2]
i = True
# Randomly determining which user should start
j = random.randint(0, 1)
show()
while(i):
    # Playing the first player randomly chosen
    i = play(players[j])
    if win(players[j]):
        print('{} wins!'.format(players[j][0]))
        break
    elif is_full():
        print('Duce...')
        break
    # Alternating between 0 and 1 for j in order to allow for each player to play at his turn
    j = 1 - j



