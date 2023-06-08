import typing

from dataclasses import dataclass

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

Color = bool
COLORS = [WHITE, BLACK] = [True, False]
COLOR_NAMES = ["black", "white"]


def color_name(piece_color: Color) -> str:
    return typing.cast(str, COLOR_NAMES[piece_color])


PieceType = int
PIECE_TYPES = [STONE, DAME] = range(1, 3)
PIECE_SYMBOLS = [None, "s", "d"]
PIECE_NAMES = [None, "stone", "dame"]

UNICODE_PIECE_SYMBOLS = {
    "s": "⛀", "S": "⛂",
    "d": "⛁", "D": "⛃",
}


def piece_symbol(piece_type: PieceType) -> str:
    return typing.cast(str, PIECE_SYMBOLS[piece_type])


def piece_name(piece_type: PieceType) -> str:
    return typing.cast(str, PIECE_NAMES[piece_type])


@dataclass
class Piece:
    piece_type: PieceType
    color: Color

    def get_symbol(self) -> str:
        symbol = piece_symbol(self.piece_type)
        return symbol if self.color else symbol.upper()

    def get_unicode_symbol(self) -> str:
        symbol = self.get_symbol()
        return UNICODE_PIECE_SYMBOLS[symbol]

    def change_color(self) -> None:
        self.color = not self.color

    def __hash__(self) -> int:
        return self.piece_type + (-1 if self.color else 1)

    def __repr__(self) -> str:
        piece_type = piece_name(self.piece_type)
        piece_color = color_name(self.color)
        return f"Piece.from_symbol({piece_type!r}, {piece_color!r})"

    def __str__(self) -> str:
        return self.get_symbol()

    def __eq__(self, obj: Self) -> bool:
        return hash(obj) == hash(self)

    @classmethod
    def from_symbol(cls, symbol: str) -> Self:
        return cls(PIECE_SYMBOLS.index(symbol.lower()), not symbol.isupper())

    @classmethod
    def from_piece(cls, piece: Self) -> Self:
        return cls(piece.piece_type, piece.color)
