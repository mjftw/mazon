

from mazon.at import At
from mazon.cell import Cell, Neighbor
from typing import Dict, Generator, Iterable

class Grid:
  def __init__(self, rows: int, cols: int):
    self.rows: int = rows
    self.cols: int = cols
    self.cells = self._setup_cells(rows, cols)

  def col_ns(self, col: int) -> Iterable[Cell]:
    if 0 <= col < self.cols:
      for row in range(self.rows):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  def col_sn(self, col: int) -> Iterable[Cell]:
    if 0 <= col < self.cols:
      for row in range(self.rows - 1, -1, -1):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  def row_we(self, row: int) -> Iterable[Cell]:
    if 0 <= row < self.rows:
      for col in range(self.cols):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  def row_ew(self, row: int) -> Iterable[Cell]:
    if 0 <= row < self.rows:
      for col in range(self.cols - 1, -1, -1):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  def _setup_cells(self, rows: int, cols: int) -> Dict[At, Cell]:
    cells = {At(row, col): Cell()
      for col in range(self.cols)
      for row in range(self.rows)
    }

    for at in cells:
      north_cell = cells.get(At(at.row - 1, at.col))
      north_neighbor = north_cell and Neighbor(north_cell, False)

      south_cell = cells.get(At(at.row + 1, at.col))
      south_neighbor = south_cell and Neighbor(south_cell, False)

      east_cell = cells.get(At(at.row, at.col + 1))
      east_neighbor = east_cell and Neighbor(east_cell, False)

      west_cell = cells.get(At(at.row, at.col - 1))
      west_neighbor = west_cell and Neighbor(west_cell, False)

      cells[at] = Cell(
        north=north_neighbor,
        south=south_neighbor,
        east=east_neighbor,
        west=west_neighbor
      )

    return cells

