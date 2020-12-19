#Jogo da Velha em Python

board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '
    
def printBoard(board):
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')

def isWinner(board, letter):
    return (board[7]== letter and board[8]== letter and board[9]== letter) or (board[4]== letter and board[5]== letter and board[6]== letter) or (board[1]== letter and board[2]== letter and board[3]== letter) or (board[1]== letter and board[4]== letter and board[7]== letter) or (board[2]== letter and board[5]== letter and board[8]== letter) or (board[3]== letter and board[6]== letter and board[9]== letter) or (board[1]== letter and board[5]== letter and board[9]== letter) or (board[3]== letter and board[5]== letter and board[7]== letter)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to plave an X (1-9):')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print('sorry this space is occupaied')
            else:
                print('Please type a number within the range')
        except:
            print('please type a number')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = 1
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move

def selectRandom(li):
    import random
    ln  = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("welcome to Tic Tac Toe!")
    printBoard(board);

    while not (isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print("O won this game")
            break

        if not(isWinner(board,'X')):
            move = compMove()
            if move == 0:
                print('tie game')
            else:
                insertLetter('O',move)
                print('computer placed O in position', move, ':')
                printBoard(board)
        else:
            print("X won this game")
            break

    if isBoardFull(board):
        print("tie game")

main()