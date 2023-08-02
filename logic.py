"""В данном модуле описывается логика перемещения фигур"""
import recursion_detect

def figure_list(board, fcolor):
    """Возвращает список активных фигур и координаты короля противоположного цвета"""
    figures = []
    king_xy = []

    for elem in board.ravel():
        if elem:
            if elem.color == fcolor:
                figures.append(elem)
            elif elem.color != fcolor and elem.val == "S":
                king_xy = [elem.x, elem.y]

    return king_xy, figures


def king_check(board, xo, yo, xn, yn):
    depth = recursion_detect.depth()
    if depth >= 1:
        return True
    """Проверяет наличие шаха при ходе"""
    tboard = board.copy()

    # Получаем список фигур оппонента и координаты своего короля
    if board[xo][yo].color == "White":
        king_xy, figures = figure_list(board, "Black")
    else:
        king_xy, figures = figure_list(board, "White")

    # Делаем фиктивный ход, который собирались
    tmp = tboard[xo][yo]
    tboard[xo][yo] = 0
    tboard[xn][yn] = tmp

    # Перебираем все ходы фигур, отправляя их на короля
    for figure in figures:
        value = figure.val
        flaj = logic_dict[value](tboard, figure.x, figure.y, king_xy[0], king_xy[1])
        if flaj:
            return False

    return True


def refresh_position(board, xo, yo, xn, yn):
    board[xo][yo].x = xn
    board[xo][yo].y = yn


def pawn_logic(board, xo, yo, xn, yn):
    """Логика пешки"""
    if board[xo][yo].first_move:
        if board[xo][yo].color == "White":
            if (xo-xn == 1 or xo-xn == 2) and yo == yn and not board[xn][yn]:
                if not king_check(board, xo, yo, xn, yn):
                    return False
                board[xo][yo].first_move = False
                return True

            elif xo-xn == 1 and abs(yo-yn) == 1:
                if board[xn][yn] and board[xn][yn].color == "Black":
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    board[xo][yo].first_move = False
                    return True

        elif board[xo][yo].color == "Black":
            if (xn - xo == 1 or xn - xo == 2) and yo == yn and not board[xn][yn]:
                if not king_check(board, xo, yo, xn, yn):
                    return False
                board[xo][yo].first_move = False
                return True

            elif xn - xo == 1 and abs(yo-yn) == 1:
                if board[xn][yn] and board[xn][yn].color == "White":
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    board[xo][yo].first_move = False
                    return True

    else:
        if board[xo][yo].color == "White":
            if xo-xn == 1 and yo == yn and not board[xn][yn]:
                if xn == 0:
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return "WPQ"
                else:
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

            elif xo-xn == 1 and abs(yo-yn) == 1:
                if board[xn][yn] and board[xn][yn].color == "Black":
                    if xn == 0:
                        if not king_check(board, xo, yo, xn, yn):
                            return False
                        return "WPQ"
                    else:
                        if not king_check(board, xo, yo, xn, yn):
                            return False
                        return True

        elif board[xo][yo].color == "Black":
            if xn-xo == 1 and yo == yn and not board[xn][yn]:
                if xn == 7:
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return "BPQ"
                else:
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

            elif xn-xo == 1 and abs(yo-yn) == 1:
                if board[xn][yn] and board[xn][yn].color == "White":
                    if xn == 7:
                        if not king_check(board, xo, yo, xn, yn):
                            return False
                        return "BPQ"
                    else:
                        if not king_check(board, xo, yo, xn, yn):
                            return False
                        return True

    return False


def knight_logic(board, xo, yo, xn, yn):
    """Логика коня """
    if board[xo][yo].color == "White":
        if abs(xo-xn) == 1 and abs(yo-yn) == 2:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                if not king_check(board, xo, yo, xn, yn):
                    return False
                return True

        if abs(xo-xn) == 2 and abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                if not king_check(board, xo, yo, xn, yn):
                    return False
                return True

    elif board[xo][yo].color == "Black":
        if abs(xo - xn) == 1 and abs(yo - yn) == 2:
            if not board[xn][yn] or board[xn][yn].color == "White":
                if not king_check(board, xo, yo, xn, yn):
                    return False
                return True

        if abs(xo - xn) == 2 and abs(yo - yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "White":
                if not king_check(board, xo, yo, xn, yn):
                    return False
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
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

                elif xo > xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, -1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

                elif xo < xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

                elif xo < xn and yo < yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, 1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    if not king_check(board, xo, yo, xn, yn):
                        return False
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
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

                elif xo > xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, -1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

                elif xo < xn and yo > yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, -1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    if not king_check(board, xo, yo, xn, yn):
                        return False
                    return True

                elif xo < xn and yo < yn:
                    for i, j in zip(range(xo + 1, xn, 1), range(yo + 1, yn, 1)):
                        if i == xo + 1 or j == yo + 1:
                            pass
                        elif board[i - 1][j - 1] and i - 1 != xn and j - 1 != yn:
                            return False
                        else:
                            pass
                    if not king_check(board, xo, yo, xn, yn):
                        return False
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

                if not king_check(board, xo, yo, xn, yn):
                    return False

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

                if not king_check(board, xo, yo, xn, yn):
                    return False

                board[xo][yo].first_move = False
                return True

    return False


def king_logic(board, xo, yo, xn, yn):
    """Логика короля """
    if board[xo][yo].color == "White":
        if abs(xo-xn) == 1 or abs(yo-yn) == 1:
            if not board[xn][yn] or board[xn][yn].color == "Black":
                if not king_check(board, xo, yo, xn, yn):
                    return False

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
                if not king_check(board, xo, yo, xn, yn):
                    return False

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

logic_dict = {"P": pawn_logic, "K": knight_logic, "B": bishop_logic,
              "R": rook_logic, "S": king_logic, "Q": queen_logic}
