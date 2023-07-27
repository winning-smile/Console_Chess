import sys
sys.path.append(r"C:\Users\coolm\PycharmProjects\Chess\venv\Lib\site-packages")
import numpy as np
from logic import *
import os
from termcolor import colored

os.system('color')

logic_dict = {"P" : pawn_logic, "K" : knight_logic, "B" : bishop_logic,
              "R" : rook_logic, "S" : king_logic, "Q" : queen_logic}


class Figure:
    def __init__(self, value, color, fid, xy):
        self.val = value
        self.color = color
        self.id = fid
        self.xy = xy


def clear_console():
    clear = lambda: os.system('cls')
    clear()


def start(board_):
    """ Заполнение доски по умолчанию """
    board_[0][0] = Figure("R", "Black", 1, [0, 0])
    board_[0][1] = Figure("K", "Black", 2, [0, 1])
    board_[0][2] = Figure("B", "Black", 3, [0, 2])
    board_[0][3] = Figure("S", "Black", 4, [0, 3])
    board_[0][4] = Figure("Q", "Black", 5, [0, 4])
    board_[0][5] = Figure("B", "Black", 6, [0, 5])
    board_[0][6] = Figure("K", "Black", 7, [0, 6])
    board_[0][7] = Figure("R", "Black", 8, [0, 7])

    for i in range(8):
        board_[1][i] = Figure("P", "Black", 9+i, [1, i])

    for i in range(8):
        board_[6][i] = Figure("P", "White", 17+i, [6, i])

    board_[7][0] = Figure("R", "White", 25, [7, 0])
    board_[7][1] = Figure("K", "White", 26, [7, 1])
    board_[7][2] = Figure("B", "White", 27, [7, 2])
    board_[7][3] = Figure("S", "White", 28, [7, 3])
    board_[7][4] = Figure("Q", "White", 29, [7, 4])
    board_[7][5] = Figure("B", "White", 30, [7, 5])
    board_[7][6] = Figure("K", "White", 31, [7, 6])
    board_[7][7] = Figure("R", "White", 32, [7, 7])


def board_output(board_, i):
    """ Выводит актуальную позицию доски """
    print("       " + f"Turn {i}")
    if (i) % 2 != 0:
        print("   " + "Turn for " + colored("WHITE", "blue"))
    else:
        print("   " + "Turn for " + colored("BLACK", "red"))
    print(" " * 3, end="")
    print(' '.join([f"{k+1}" for k in range(8)]), end=" ")
    print("")
    for i in range(len(board_)):
        for j in range(len(board_)):
            if not board_[i][j]:
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
                    if board_[i][j].color == "White":
                        print(colored(board_[i][j].val, 'blue'), end=" ")
                    else:
                        print(colored(board_[i][j].val, 'red'), end=" ")
                elif j == 7:
                    if board_[i][j].color == "White":
                        print(colored(board_[i][j].val, 'blue'), end=" ")
                    else:
                        print(colored(board_[i][j].val, 'red'), end=" ")
                    print(f"|{i+1}", end="")
                else:
                    if board_[i][j].color == "White":
                        print(colored(board_[i][j].val, 'blue'), end=" ")
                    else:
                        print(colored(board_[i][j].val, 'red'), end=" ")
        print("")
    print(" " * 3, end="")
    print(' '.join([f"{k + 1}" for k in range(8)]), end=" ")


def board_input(board_, old, new, i):
    """Передвигает фигуру по координатам old на координаты new"""
    xo = int(old[0]) - 1
    yo = int(old[2]) - 1
    xn = int(new[0]) - 1
    yn = int(new[2]) - 1
    color_flag = ""
    """Переделать на тернарник"""

    if i % 2 != 0:
        color_flag = "White"
    else:
        color_flag = "Black"

    if board_[xo][yo] and color_flag == board_[xo][yo]:
        figure = board_[xo][yo].val
        logic_dict[figure](board_, xo, yo, xn, yn)
        tmp = board_[xo][yo]
        board_[xo][yo] = 0
        board_[xn][yn] = tmp
        return board_, True

    else:
        return board_, False

if __name__ == '__main__':
    i = 1   # Turn counter
    board = np.zeros((8, 8), dtype=object)
    start(board)
    while True:
        clear_console()
        board_output(board, i)
        board, flag = board_input(board, list(input("\nКоординаты фигуры: ")), list(input("Куда передвинуть: ")), i)
        if flag:
            i += 1  # Turn counter

