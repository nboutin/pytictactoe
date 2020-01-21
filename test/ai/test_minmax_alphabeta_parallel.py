#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import copy
import sys
import os
import time
sys.path.insert(0, os.path.join(sys.path[0], 'source'))
# sys.path.insert(0, os.path.join(sys.path[0], '..', '..', 'source'))


from game_base.board import (Point, Board, Token)
from game_base.player import Player
from ai.minmax_alphabeta_thread import Minmax_AlphaBeta_Thread
from game.tictactoe import TicTacToe
from game.connect_four import ConnectFour
from game.gomoku import Gomoku


class TestMinmaxAlphaBeta(unittest.TestCase):

    def test_pos(self):
        p1 = Player("AI_1", Token.A, True)
        p2 = Player("AI_2", Token.B, True)
        game = ConnectFour(p1=p1, p2=p2)

        moves = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2, 1, 2]
        for m in moves:
            game.play(m)

        #Todo: check board configuration
        #Todo: go to p2 turn, and call ai.compute

        depth = 1
        ai = Minmax_AlphaBeta_Thread(p1, depth)

        self.assertEqual(ai.compute(game), 3)

    def test_deepcopy(self):
        depth = 4
        p1 = Player("AI_1", Token.A, True)
        ai = Minmax_AlphaBeta_Thread(p1, depth)

        cai = copy.deepcopy(ai)

        self.assertFalse(ai is cai)
        self.assertFalse(ai._player is cai._player)
        ai._depth = 5
        self.assertFalse(ai._depth is cai._depth)
        self.assertNotEqual(ai._depth, cai._depth)

    @unittest.skip("")
    def test_tictactoe(self):
        ai_player = Player("AI_1", Token.A, True)
        game = TicTacToe(p1=ai_player)
        depth = 9
        minmax = Minmax_AlphaBeta_Thread(ai_player, depth)

        minmax.compute(game)

    @unittest.skip("")
    def test_connect_four(self):
        ai_player = Player("AI_1", Token.A, True)
        game = ConnectFour(p1=ai_player)
        depth = 10
        minmax = Minmax_AlphaBeta_Thread(ai_player, depth)

        minmax.compute(game)

    @unittest.skip("")
    def test_gomoku(self):
        ai_player = Player("AI_1", Token.A, True)
        game = Gomoku(p1=ai_player)
        depth = 5
        minmax = Minmax_AlphaBeta_Thread(ai_player, depth)

        minmax.compute(game)


if __name__ == "__main__":
    unittest.main()
