import sys
import os
sys.path.append(r"C:\Users\coolm\PycharmProjects\Chess\venv\Lib\site-packages")
import unittest
import numpy as np
import main
import logic


class TestChess(unittest.TestCase):
    def test_castling(self):
        # Короткая рокировка белых
        WSC = [[[7," ", 7], [6, " ", 7]], [[2, " ", 1], [3, " ", 1]], [[8, " ", 7], [6, " ", 6]],
                   [[3, " ", 1], [4, " ", 1]], [[8, " ", 6], [7, " ", 7]], [[4, " ", 1], [5, " ", 1]]]
        # Длинная рокировка белых
        WLC = [[[7," ", 4], [6, " ", 4]], [[2, " ", 8], [3, " ", 8]], [[8, " ", 3], [6, " ", 5]],
                   [[3, " ", 8], [4, " ", 8]], [[8, " ", 4], [7, " ", 4]], [[4, " ", 8], [5, " ", 8]], [[8, " ", 2], [6, " ", 1]],
                   [[5, " ", 8], [6, " ", 8]]]
        # Короткая рокировка черных
        BSC = [[[7," ", 1], [6, " ", 1]], [[2, " ", 7], [3, " ", 7]], [[6, " ", 1], [5, " ", 1]],
                   [[1, " ", 6], [2, " ", 7]], [[5, " ", 1], [4, " ", 1]], [[1, " ", 7], [3, " ", 8]], [[4, " ", 1], [3, " ", 1]]]
        # Длинная рокировка черных
        BLC = [[[7," ", 8], [6, " ", 8]], [[2, " ", 4], [3, " ", 4]], [[6, " ", 8], [5, " ", 8]],
                   [[1, " ", 3], [3, " ", 5]], [[5, " ", 8], [4, " ", 8]], [[1, " ", 4], [2, " ", 4]], [[4, " ", 8], [3, " ", 8]],
                   [[1, " ", 2], [3, " ", 1]], [[7, " ", 1], [6, " ", 1]]]

        lt = [[7, 4, 7, 7], [7, 4, 7, 0], [0, 4, 0, 7], [0, 4, 0, 0]]
        castling_tests = [WSC, WLC, BSC, BLC]
        castling_out = ["WSC", "WLC", "BSC", "BLC"]

        for id, scenario in enumerate(castling_tests):
            counter = id
            i = 1
            tboard = np.zeros((8, 8), dtype=object)
            tboard = main.start(tboard)

            for turn in scenario:
                tboard, tflag = main.board_input(tboard, i, turn[0], turn[1])
                i += 1

            # castling
            self.assertEqual(logic.king_logic(tboard, lt[counter][0], lt[counter][1], lt[counter][2], lt[counter][3]), f'{castling_out[counter]}')
            tboard, tflag = main.board_input(tboard, i, [lt[counter][0]+1, " ", lt[counter][1]+1], [lt[counter][2]+1," ", lt[counter][3]+1])
            i += 1
            print(f"\ntest to {castling_out[counter]}")
            main.board_output(tboard, i)

    def test_pawn_to_queen(self):
        # Белая и черная пешки становятся ферзями
        WBQ = [[[7, " ", 5], [6, " ", 5]], [[2, " ", 4], [3, " ", 4]], [[7, " ", 8], [6, " ", 8]],
               [[2, " ", 1], [3, " ", 1]], [[8, " ", 6], [3, " ", 1]], [[1, " ", 3], [6, " ", 8]],
               [[7, " ", 7], [6, " ", 8]], [[2, " ", 2], [3, " ", 1]], [[7, " ", 2], [5, " ", 2]],
               [[2, " ", 7], [4, " ", 7]], [[5, " ", 2], [4, " ", 2]], [[4, " ", 7], [5, " ", 7]],
               [[4, " ", 2], [3, " ", 2]], [[5, " ", 7], [6, " ", 7]], [[3, " ", 2], [2, " ", 2]],
               [[6, " ", 7], [7, " ", 7]], [[8, " ", 7], [6, " ", 6]], [[1, " ", 2], [3, " ", 3]],
               [[2, " ", 2], [1, " ", 2]], [[7, " ", 7], [8, " ", 7]]]

        lt = [[0, 1], [7, 6]]
        i = 1
        tboard = np.zeros((8, 8), dtype=object)
        tboard = main.start(tboard)

        for turn in WBQ:
            tboard, tflag = main.board_input(tboard, i, turn[0], turn[1])
            i += 1
        print(f"\ntest to pawn to queen")
        main.board_output(tboard, i)
        # castling
        self.assertEqual(tboard[lt[0][0]][lt[0][1]].val, "Q")
        self.assertEqual(tboard[lt[1][0]][lt[1][1]].val, "Q")


if __name__ == '__main__':
    main.clear_console()
    unittest.main()