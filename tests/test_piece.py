import unittest
from lib.piece import *


class PieceColor(unittest.TestCase):
    def test_color_name(self):
        piece_color = [color_name(WHITE), color_name(BLACK)]
        excepted_color = ["white", "black"]

        self.assertEqual(piece_color, excepted_color)


class PieceTypeFunction(unittest.TestCase):

    def test_pieces_symbol(self):
        stone, dame = PIECE_TYPES[0], PIECE_TYPES[1]
        symbols = (piece_symbol(stone), piece_symbol(dame))

        expected_symbols = ('s', 'd')
        self.assertEqual(expected_symbols, symbols)

    def test_pieces_name(self):
        stone, dame = PIECE_TYPES[0], PIECE_TYPES[1]
        name = (piece_name(stone), piece_name(dame))

        expected_name = ('stone', 'dame')
        self.assertEqual(expected_name, name)


class PieceClass(unittest.TestCase):
    pieces = [
        Piece(STONE, WHITE),
        Piece(DAME, WHITE),
        Piece(STONE, BLACK),
        Piece(DAME, BLACK),
    ]

    def test_change_color(self):
        colors = []
        for piece in self.pieces:
            piece.change_color()
            colors.append(piece.color)
            piece.change_color()

        expected_colors = [BLACK, BLACK, WHITE, WHITE]
        self.assertEqual(expected_colors, colors)

    def test_hash(self):
        hashes = []
        for piece in self.pieces:
            hashes.append(hash(piece))

        expected_hashes = [0, 1, 2, 3]
        self.assertEqual(expected_hashes, hashes)

    def test_get_symbol(self):
        strings = []
        for piece in self.pieces:
            strings.append(piece.get_symbol())

        excepted_strings = ['s', 'd', 'S', 'D']
        self.assertEqual(excepted_strings, strings)

    def test_from_symbol(self):
        pieces = []
        for piece in self.pieces:
            symbol = piece.get_symbol()
            pieces.append(Piece.from_symbol(symbol))

        expected_pieces = []
        for piece in self.pieces:
            expected_pieces.append(piece)

        self.assertEqual(expected_pieces, pieces)

    def test_from_piece(self):
        pieces = []
        for piece in self.pieces:
            pieces.append(Piece.from_piece(piece))

        expected_pieces = []
        for piece in self.pieces:
            expected_pieces.append(piece)

        self.assertEqual(expected_pieces, pieces)

    def test_get_unicode_symbol(self):
        strings = []
        for piece in self.pieces:
            strings.append(piece.get_unicode_symbol())

        excepted_strings = ['⛀', '⛁', '⛂', '⛃']
        self.assertEqual(excepted_strings, strings)


if __name__ == '__main__':
    unittest.main()
