from dataclasses import dataclass

@dataclass(frozen=True)
class At:
  row: int
  col: int

  def __repr__(self) -> str:
    return f"[{self.row},{self.col}]"

  def north(self) -> 'At':
    return At(self.row - 1, self.col)

  def south(self) -> 'At':
    return At(self.row + 1, self.col)

  def east(self) -> 'At':
    return At(self.row, self.col + 1)

  def west(self) -> 'At':
    return At(self.row, self.col - 1)
