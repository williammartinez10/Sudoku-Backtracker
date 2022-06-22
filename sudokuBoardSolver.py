
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def solve(board):
    foundEmptySlot = findEmptySlot(board)
    if not foundEmptySlot:
        return True
    else:
        row, col = foundEmptySlot

    for i in range(1,10):
        if isValid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = '_'
    return False


def findEmptySlot(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                # (row, column)
                return i, j
    return None


def isValid(board, number, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check grid
    xCoord = position[1] // 3
    yCoord = position[0] // 3

    for i in range(yCoord * 3, yCoord * 3 + 3):
        for j in range(xCoord * 3, xCoord * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def main():
    board = [
            ['_', '_', '_',  7 ,  9 , '_', '_',  5 , '_'],
            [ 3 ,  5 ,  2 , '_', '_',  8 , '_',  4 , '_'],
            ['_', '_', '_', '_', '_', '_', '_',  8 , '_'],
            ['_',  1 , '_', '_',  7 , '_', '_', '_',  4 ],
            [ 6 , '_', '_',  3 , '_',  1 , '_', '_',  8 ],
            [ 9 , '_', '_', '_', '_', '_', '_',  1 , '_'],
            ['_',  2 , '_', '_', '_', '_', '_', '_', '_'],
            ['_',  4 , '_',  5 , '_', '_',  8 ,  9 ,  1 ],
            ['_',  8 , '_', '_',  3 ,  7 , '_', '_', '_'],
            ]

    print("\nHere is your Sudoku Board! - UNSOLVED\n")
    printBoard(board)
    solve(board)
    print("\n____________________________________________________\n")
    print("Here is your Sudoku Board! - SOLVED\n")
    printBoard(board)

main()
