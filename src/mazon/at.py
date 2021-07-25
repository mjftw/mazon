from dataclasses import dataclass

@dataclass(frozen=True)
class At:
  row: int
  col: int

  def __repr__(self) -> str:
    return f"[{self.row},{self.col}]"

  '''Get coordinate to the north'''
  def north(self) -> 'At':
    return At(self.row - 1, self.col)

  '''Get coordinate to the south'''
  def south(self) -> 'At':
    return At(self.row + 1, self.col)

  '''Get coordinate to the east'''
  def east(self) -> 'At':
    return At(self.row, self.col + 1)

  '''Get coordinate to the west'''
  def west(self) -> 'At':
    return At(self.row, self.col - 1)
