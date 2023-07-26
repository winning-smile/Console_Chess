"""В данном модуле описывается логика перемещения фигур"""


def pawn_logic(board, xo, yo, xn, yn):
    """Логика пешки"""
    if board[xo][yo].color == "White":
        if xo-xn == 1 and yo == yn and not board[xn][yn]:
                return True

        elif xo-xn == 1 and yo-yn == 1:
            if board[xn][yn] and board[xn][yn].color == "Black":
                return True

        elif xo-xn == 1 and yo-yn == -1:
            if board[xn][yn] and board[xn][yn].color == "Black":
                return True

    else:
        if xn - xo == 1 and yo == yn and not board[xn][yn]:
            return True

        elif xn - xo == 1 and yo - yn == 1:
            if board[xn][yn] and board[xn][yn].color == "White":
                return True

        elif xn - xo == 1 and yo - yn == -1:
            if board[xn][yn] and board[xn][yn].color == "White":
                return True

    return False


def knight_logic(board, xo, yo, xn, yn):
    """Логика коня """
    if board[xo][yo].color == "White":
        if abs(xo-xn) == 1 and abs(yo-yn) == 2:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                return True

        if abs(xo-xn) == 2 and abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                return True

    if board[xo][yo].color == "Black":
        if abs(xo - xn) == 1 and abs(yo - yn) == 2:
            if not board[xn][yn] or board[xn][yn].color == "White":
                return True

        if abs(xo - xn) == 2 and abs(yo - yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "White":
                return True

    return False


def bishop_logic(board, xo, yo, xn, yn):
    """Логика слона """
    if board[xo][yo].color == "White":
        if abs(xo-xn) == abs(yo-yn) and xo-xn != 0:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                return True

    if board[xo][yo].color == "Black":
        if abs(xo-xn) == abs(yo-yn) and xo-xn != 0:
            if not board[xn][yn] or board[xn][yn].color == "White":
                return True

    return False


def rook_logic(board, xo, yo, xn, yn):
    """Логика ладьи"""
    if board[xo][yo].color == "White":
        if (xo == xn and yo != yn) or (xo != xn and yo == yn):
            if not board[xn][yn] or board[xn][yn].color == "Black":
                return True

    if board[xo][yo].color == "Black":
        if (xo == xn and yo != yn) or (xo != xn and yo == yn):
            if not board[xn][yn] or board[xn][yn].color == "White":
                return True

    return False


def king_logic(board, xo, yo, xn, yn):
    """Логика короля """
    if board[xo][yo].color == "White":
        if abs(xo-xn) == 1 or abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                return True

    if board[xo][yo].color == "Black":
        if abs(xo-xn) == 1 or abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "White":
                return True

    return False


def queen_logic(board, xo, yo, xn, yn):
    """Логика ферзя"""
    if board[xo][yo].color == "White":
        if (abs(xo - xn) == abs(yo - yn) and xo - xn != 0) or ((xo == xn and yo != yn) or (xo != xn and yo == yn)):
            if not board[xn][yn] or board[xn][yn].color == "Black":
                return True

    if board[xo][yo].color == "Black":
        if (abs(xo - xn) == abs(yo - yn) and xo - xn != 0) or ((xo == xn and yo != yn) or (xo != xn and yo == yn)):
            if not board[xn][yn] or board[xn][yn].color == "White":
                return True

    return False