from dataclasses import dataclass

@dataclass(frozen=True)
class At:
  row: int
  col: int

  def __repr__(self) -> str:
    return f"[{self.row},{self.col}]"