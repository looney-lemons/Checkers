from dataclasses import dataclass
import typing

Color = bool
COLORS = [WHITE, BLACK] = [True, False]
COLOR_NAMES = ["black", "white"]

PieceType = int
PIECE_TYPES = [STONE, DAME] = range(1, 3)
PIECE_SYMBOLS = [None, "s", "d"]
PIECE_NAMES = [None, "stone", "dame"]


def piece_symbol(piece_type: PieceType) -> str:
    return typing.cast(str, PIECE_SYMBOLS[piece_type])


def piece_name(piece_type: PieceType) -> str:
    return typing.cast(str, PIECE_NAMES[piece_type])


@dataclass
class Piece:
    piece_type: PieceType
    color: Color

    def change_color(self):
        self.color = not self.color

    def __hash__(self) -> int:
        return self.piece_type + (-1 if self.color else 1)

    def __repr__(self) -> str:
        return f"Piece.from_symbol({str(self)!r})"

    def __str__(self) -> str:
        symbol = piece_symbol(self.piece_type)
        return symbol if self.color else symbol.upper()

    def __eq__(self, obj: Piece) -> bool:
        return hash(obj) == hash(self)

    @classmethod
    def from_symbol(cls, symbol: str) -> Piece:
        return cls(PIECE_SYMBOLS.index(symbol.lower()), symbol.isupper())

    @classmethod
    def from_piece(cls, piece: Piece) -> Piece:
        return cls(piece.piece_type, piece.color)
