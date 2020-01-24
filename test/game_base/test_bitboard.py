#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], 'source'))

import unittest
from game_base.bitboard import BitBoard


class TestBoard(unittest.TestCase):

    def test_init(self):
        board = BitBoard()
        bb = board._bitboard
        self.assertEqual(bb[0], 0)
        self.assertEqual(bb[1], 0)

    def test_makeMove(self):
        board = BitBoard()
        bb = board._bitboard

        board.makeMove(0)
        x = 1
        o = 0
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(1)
        o |= 1 << 7
        board.makeMove(1)
        x |= 1 << 8
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(2)
        o |= 1 << 14
        board.makeMove(2)
        x |= 1 << 15
        board.makeMove(2)
        o |= 1 << 16
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

    def test_col_6(self):
        board = BitBoard()
        bb = board._bitboard

        board.makeMove(6)
        board.makeMove(6)
        x = 1 << 42
        o = 1 << 43
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(5)
        board.makeMove(5)
        x |= 1 << 35
        o |= 1 << 36
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)

        board.makeMove(4)
        board.makeMove(4)
        x |= 1 << 28
        o |= 1 << 29
        self.assertEqual(bb[0], x)
        self.assertEqual(bb[1], o)


#     def test_undoMove(self):
#         bb = BitBoard()
#         bb.makeMove(0)
#         bb.makeMove(1)
#         bb.undoMove()
#         print(bb)

    def test_isWin(self):
        bb = BitBoard()
        self.assertFalse(bb.isWin(0))
        self.assertFalse(bb.isWin(1))

    def test_seqA(self):
        board = BitBoard()
        moves = [6, 6, 5, 5, 4, 4, 3]
        for m in moves:
            board.makeMove(m)

        print(board)
        self.assertTrue(board.isWin(0))