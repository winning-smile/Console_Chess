import sys
sys.path.append(r"C:\Users\coolm\PycharmProjects\Chess\venv\Lib\site-packages")
import numpy as np
from logic import *
import os
from termcolor import colored

os.system('color')


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


def board_output(board_):
    """ Выводит актуальную позицию доски """
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


def board_input(board_, old, new):
    """Передвигает фигуру по координатам old на координаты new"""
    xo = int(old[0]) - 1
    yo = int(old[2]) - 1
    xn = int(new[0]) - 1
    yn = int(new[2]) - 1
    figure = board_[xo][yo].val

    """Переделать на словарь"""
    if figure == "P":
        if pawn_logic(board_, xo, yo, xn, yn):
            tmp = board_[xo][yo]
            board_[xo][yo] = 0
            board_[xn][yn] = tmp
            return board_
        else:
            print("Неправильный ход")
            return board_
    elif figure == "K":
        if knight_logic(board_, xo, yo, xn, yn):
            tmp = board_[xo][yo]
            board_[xo][yo] = 0
            board_[xn][yn] = tmp
            return board_
        else:
            print("Неправильный ход")
            return board_
    elif figure == "B":
        if bishop_logic(board_, xo, yo, xn, yn):
            tmp = board_[xo][yo]
            board_[xo][yo] = 0
            board_[xn][yn] = tmp
            return board_
        else:
            print("Неправильный ход")
            return board_
    elif figure == "R":
        if rook_logic(board_, xo, yo, xn, yn):
            tmp = board_[xo][yo]
            board_[xo][yo] = 0
            board_[xn][yn] = tmp
            return board_
        else:
            print("Неправильный ход")
            return board_
    elif figure == "Q":
        if queen_logic(board_, xo, yo, xn, yn):
            tmp = board_[xo][yo]
            board_[xo][yo] = 0
            board_[xn][yn] = tmp
            return board_
        else:
            print("Неправильный ход")
            return board_
    elif figure == "S":
        if king_logic(board_, xo, yo, xn, yn):
            tmp = board_[xo][yo]
            board_[xo][yo] = 0
            board_[xn][yn] = tmp
            return board_
        else:
            print("Неправильный ход")
            return board_
    else:
        print("Ты даун.")
        return board_


if __name__ == '__main__':
    board = np.zeros((8, 8), dtype=object)
    start(board)
    while True:
        clear_console()
        board_output(board)
        board = board_input(board, list(input("\nКоординаты фигуры: ")), list(input("Куда передвинуть: ")))
