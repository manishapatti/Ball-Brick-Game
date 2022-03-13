import math

def printb(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print('')


def makeboard(n):
    board = [[' ' for i in range(n)] for j in range(n)]
    for i in range(n):
        board[0][i] = 'W'
        board[i][n - 1] = 'w'
        board[i][0] = 'W'
    for i in range(1, n - 1):
        board[n - 1][i] = 'G'
    board[n - 1][int(n / 2)] = 'o'
    return board


def ass_bricks(board):
    while True:
        i, j, val = [int(i) for i in input("Enter the brick's position and Brick's type: ").split()]
        board[i][j] = val
        answer = input("Enter yes or no: ")
        if answer == "Y":
            continue
        elif answer == "N":
            break
        else:
            print("Please enter yes or no.")


def st(board, b_in_pos):
    i, j = b_in_pos[0], b_in_pos[1]
    while i - 1 > 1:
        if board[i - 1][j] == "W":
            break
        elif board[i - 1][j] != " ":
            board[i - 1][j] -= 1
            if board[i - 1][j] == 0:
                board[i - 1][j] = " "
            break
        else:
            i -= 1


def ld(board, b_in_pos):
    i, j = b_in_pos[0], b_in_pos[1]
    j = j - 1
    while i - 1 > 1:
        if board[i - 1][j] == "W":
            break
        elif board[i - 1][j] != " ":
            board[i - 1][j] -= 1
            if board[i - 1][j] == 0:
                board[i - 1][j] = " "
            break
        else:
            i -= 1


def rd(board, b_in_pos):
    i, j = b_in_pos[0], b_in_pos[1]
    j = j + 1
    while i - 1 > 1:
        if board[i - 1][j] == "W":
            break
        elif board[i - 1][j] != " ":
            board[i - 1][j] -= 1
            if board[i - 1][j] == 0:
                board[i - 1][j] = " "
            break
        else:
            i -= 1




board_size = int(input("Enter the size of NxN matrix: "))
board = makeboard(board_size)
ass_bricks(board)
printb(board)
ballcnt = int(input("Enter ball count: "))
b_in_pos = [board_size - 1, math.floor(board_size / 2)]
print(b_in_pos)

while True:
    if ballcnt:
        travs = input("Enter the direction in which the ball need to traverse: ")
        if travs == "ST":
            st(board, b_in_pos)
            printb(board)
        elif travs == "LD":
            ld(board, b_in_pos)
            ballcnt = ballcnt - 1
            if (board[b_in_pos[1] - 1][6] == "W"):
                print(board[b_in_pos[1] - 1])
                ballcnt = ballcnt - 1
            else:
                board[b_in_pos[1]][6], board[b_in_pos[1] - 1][6] = board[b_in_pos[1] - 1][6], board[b_in_pos[1]][6]
                b_in_pos[1] = b_in_pos[0] - 1

            printb(board)
            print("Ball count: ", ballcnt)
        elif travs == "RD":
            rd(board, b_in_pos)
            if (board[b_in_pos[1] + 1][6] == "W"):
                ballcnt = ballcnt - 1
            else:
                b_in_pos[0] = b_in_pos[1] + 1
            ballcnt = ballcnt - 1
            printb(board)
            print("Ball count: ", ballcnt)
    else:
        print("YOU LOST")
        break
