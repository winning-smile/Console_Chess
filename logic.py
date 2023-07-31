"""В данном модуле описывается логика перемещения фигур"""


def pawn_logic(board, xo, yo, xn, yn):
    """Логика пешки"""
    if board[xo][yo].first_move:
        if board[xo][yo].color == "White":
            if (xo-xn == 1 or xo-xn == 2) and yo == yn and not board[xn][yn]:
                if xo-xn == 2:
                    board[xo][yo].first_move = False
                return True

            elif xo-xn == 1 and yo-yn == 1:
                if board[xn][yn] and board[xn][yn].color == "Black":
                    return True

            elif xo-xn == 1 and yo-yn == -1:
                if board[xn][yn] and board[xn][yn].color == "Black":
                    return True

        elif board[xo][yo].color == "Black":
            if (xn - xo == 1 or xn - xo == 2) and yo == yn and not board[xn][yn]:
                if xo-xn == 2:
                    board[xo][yo].first_move = False
                return True

            elif xn - xo == 1 and yo - yn == 1:
                if board[xn][yn] and board[xn][yn].color == "White":
                    return True

            elif xn - xo == 1 and yo - yn == -1:
                if board[xn][yn] and board[xn][yn].color == "White":
                    return True
    else:
        if board[xo][yo].color == "White":
            if xo-xn == 1 and yo == yn and not board[xn][yn]:
                return True

            elif xo-xn == 1 and yo-yn == 1:
                if board[xn][yn] and board[xn][yn].color == "Black":
                    return True

            elif xo-xn == 1 and yo-yn == -1:
                if board[xn][yn] and board[xn][yn].color == "Black":
                    return True

        elif board[xo][yo].color == "Black":
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

    elif board[xo][yo].color == "Black":
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
                if xo > xn and yo < yn:
                    for i, j in zip(range(xo + 1, xn, -1), range(yo + 1, yn, 1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

                elif xo > xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, -1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

                elif xo < xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

                elif xo < xn and yo < yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, 1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

    elif board[xo][yo].color == "Black":
        if abs(xo-xn) == abs(yo-yn) and xo-xn != 0:
            if not board[xn][yn] or board[xn][yn].color == "White":
                if xo > xn and yo < yn:
                    for i, j in zip(range(xo + 1, xn, -1), range(yo + 1, yn, 1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

                elif xo > xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, -1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

                elif xo < xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

                elif xo < xn and yo < yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, 1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    return True

    return False


def rook_logic(board, xo, yo, xn, yn):
    """Логика ладьи"""
    if board[xo][yo].color == "White":
        if (xo == xn and yo != yn) or (xo != xn and yo == yn):
            if not board[xn][yn] or board[xn][yn].color == "Black":
                t1, t2 = (xo, xn) if yo == yn else (yo, yn)
                t1, t2 = (t2, t1) if t1 > t2 else (t1, t2)
                if yo == yn:
                    for i in range(t1+1, t2, 1):
                        if board[i][yn]:
                            return False
                        else:
                            pass
                else:
                    for i in range(t1+1, t2, 1):
                        if board[xn][i]:
                            return False
                        else:
                            pass

                board[xo][yo].first_move = False
                return True

    elif board[xo][yo].color == "Black":
        if (xo == xn and yo != yn) or (xo != xn and yo == yn):
            if not board[xn][yn] or board[xn][yn].color == "White":
                t1, t2 = (xo, xn) if yo == yn else (yo, yn)
                t1, t2 = (t2, t1) if t1 > t2 else (t1, t2)
                if yo == yn:
                    for i in range(t1+1, t2, 1):
                        if board[i][yn]:
                            return False
                        else:
                            pass
                else:
                    for i in range(t1+1, t2, 1):
                        if board[xn][i]:
                            return False
                        else:
                            pass

                board[xo][yo].first_move = False
                return True

    return False


def king_logic(board, xo, yo, xn, yn):
    """Логика короля """
    if board[xo][yo].color == "White":
        if abs(xo-xn) == 1 or abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                board[xo][yo].first_move = False
                return True

        # Рокировка белых
        elif board[xo][yo].first_move and board[xn][yn].first_move and board[xn][yn].val == "R" and board[xn][yn].color == "White":
            # короткая
            if yn == 7:
                for i in range(yo+1, yn, 1):
                    if i == yo+1:
                        pass
                    elif board[7][i]:
                        return False
                    else:
                        return "WSC"
            # длинная
            if yn == 0:
                for i in range(yo, yn, -1):
                    if i == yo:
                        pass
                    elif board[7][i]:
                        return False
                    else:
                        return "WLC"

    elif board[xo][yo].color == "Black":
        if abs(xo-xn) == 1 or abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "White":
                board[xo][yo].first_move = True
                return True

        # Рокировка черных
        elif board[xo][yo].first_move and board[xn][yn].first_move and board[xn][yn].val == "R" and board[xn][yn].color == "Black":
            # короткая
            if yn == 7:
                for i in range(yo+1, yn, 1):
                    if i == yo+1:
                        pass
                    elif board[0][i]:
                        return False
                    else:
                        return "BSC"
            # длинная
            if yn == 0:
                for i in range(yo, yn, -1):
                    if i == yo:
                        pass
                    elif board[0][i]:
                        return False
                    else:
                        return "BLC"


    return False


def queen_logic(board, xo, yo, xn, yn):
    """Логика ферзя"""
    if board[xo][yo].color == "White":
        if (abs(xo - xn) == abs(yo - yn) and xo - xn != 0):
            if bishop_logic(board, xo, yo, xn, yn):
                return True
        elif ((xo == xn and yo != yn) or (xo != xn and yo == yn)):
            if rook_logic(board, xo, yo, xn, yn):
                return True

    elif board[xo][yo].color == "Black":
        if (abs(xo - xn) == abs(yo - yn) and xo - xn != 0):
            if bishop_logic(board, xo, yo, xn, yn):
                return True
        elif ((xo == xn and yo != yn) or (xo != xn and yo == yn)):
            if rook_logic(board, xo, yo, xn, yn):
                return True

    return False