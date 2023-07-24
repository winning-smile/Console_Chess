import numpy as np
import sys
class Figure():
    def __init__(self, value, color, id, xy):
        self.val = value
        self.color = color
        self.id = id
        self.xy = xy

def start(board):
    """ Заполнение доски по умолчанию """
    board[0][0] = Figure("R", "Black", 1, [0, 0])
    board[0][1] = Figure("K", "Black", 2, [0, 1])
    board[0][2] = Figure("B", "Black", 3, [0, 2])
    board[0][3] = Figure("S", "Black", 4, [0, 3])
    board[0][4] = Figure("Q", "Black", 5, [0, 4])
    board[0][5] = Figure("B", "Black", 6, [0, 5])
    board[0][6] = Figure("K", "Black", 7, [0, 6])
    board[0][7] = Figure("R", "Black", 8, [0, 7])

    for i in range(8):
        board[1][i] = Figure("P", "Black", 9+i, [1, i])


    for i in range(8):
        board[6][i] = Figure("P", "White", 17+i, [6, i])

    board[7][0] = Figure("R", "White", 25, [7, 0])
    board[7][1] = Figure("K", "White", 26, [7, 1])
    board[7][2] = Figure("B", "White", 27, [7, 2])
    board[7][3] = Figure("S", "White", 28, [7, 3])
    board[7][4] = Figure("Q", "White", 29, [7, 4])
    board[7][5] = Figure("B", "White", 30, [7, 5])
    board[7][6] = Figure("K", "White", 31, [7, 6])
    board[7][7] = Figure("R", "White", 32, [7, 7])

def board_output(board):
    """ Выводит актуальную позицию доски """
    print(" " * 3, end="")
    print(' '.join([f"{k+1}" for k in range(8)]), end=" ")
    print("")
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                if j == 0:
                    print(f"{i+1}| ", end="")
                    print("0 ", end="")
                elif j == 7:
                    print("0", end="")
                    print(f" |{i+1}", end="")
                else:
                    print("0 ", end="")
            else:
                if j == 0:
                    print(f"{i+1}| ", end="")
                    print(board[i][j].val, end=" ")
                elif j == 7:
                    print(board[i][j].val, end=" ")
                    print(f"|{i+1}", end="")
                else:
                    print(board[i][j].val, end=" ")
        print("")
    print(" " * 3, end="")
    print(' '.join([f"{k + 1}" for k in range(8)]), end=" ")


if __name__ == '__main__':
    board = np.zeros((8, 8), dtype=object)
    start(board)
    board_output(board)




