

from dataclasses import replace
from mazon.at import At
from mazon.cell import Cell, Neighbor
from typing import Dict, Iterable

class Grid:
  def __init__(self, rows: int, cols: int):
    self.rows: int = rows
    self.cols: int = cols
    self.cells = self._setup_cells(rows, cols)

  '''Link the cell at @at to its northern neighbor'''
  def link_north(self, at: At) -> 'Grid':
    self._validate_at(at)
    cell = self.cells[at]
    if cell.north:
      north = self.cells[at.north()]
      self.cells[at] = replace(cell, north=replace(cell.north, is_linked=True))
      self.cells[at.north()] = replace(north, south=replace(north.south, is_linked=True))
    return self

  '''Link the cell at @at to its southern neighbor'''
  def link_south(self, at: At) -> 'Grid':
    self._validate_at(at)
    cell = self.cells[at]
    if cell.south:
      south = self.cells[at.south()]
      self.cells[at] = replace(cell, south=replace(cell.south, is_linked=True))
      self.cells[at.south()] = replace(south, north=replace(south.north, is_linked=True))
    return self

  '''Link the cell at @at to its eastern neighbor'''
  def link_east(self, at: At) -> 'Grid':
    self._validate_at(at)
    cell = self.cells[at]
    if cell.east:
      east = self.cells[at.east()]
      self.cells[at] = replace(cell, east=replace(cell.east, is_linked=True))
      self.cells[at.east()] = replace(east, west=replace(east.west, is_linked=True))
    return self

  '''Link the cell at @at to its western neighbor'''
  def link_west(self, at: At) -> 'Grid':
    self._validate_at(at)
    cell = self.cells[at]
    if cell.west:
      west = self.cells[at.west()]
      self.cells[at] = replace(cell, west=replace(cell.west, is_linked=True))
      self.cells[at.west()] = replace(west, east=replace(west.east, is_linked=True))
    return self

  '''Iterate cells in @col north to south'''
  def col_ns(self, col: int) -> Iterable[Cell]:
    if 0 <= col < self.cols:
      for row in range(self.rows):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  '''Iterate cells in @col south to north'''
  def col_sn(self, col: int) -> Iterable[Cell]:
    if 0 <= col < self.cols:
      for row in range(self.rows - 1, -1, -1):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  '''Iterate cells in @row west to east'''
  def row_we(self, row: int) -> Iterable[Cell]:
    if 0 <= row < self.rows:
      for col in range(self.cols):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  '''Iterate cells in @row east to west'''
  def row_ew(self, row: int) -> Iterable[Cell]:
    if 0 <= row < self.rows:
      for col in range(self.cols - 1, -1, -1):
        yield self.cells[At(row, col)]
    else:
      yield from ()

  def __repr__(self) -> str:
    print(self.rows)
    output: str = "+" + ("---+" * self.cols) + "\n"

    for row in range(self.rows):
      middle_str = "|"
      bottom_str = "+"

      for cell in self.row_we(row):
        middle_str += "   " + (" " if cell.east and cell.east.is_linked else "|")
        bottom_str += ("   " if cell.south and cell.south.is_linked else "---") + "+"

      output += middle_str + "\n" + bottom_str + "\n"

    return output

  def _setup_cells(self, rows: int, cols: int) -> Dict[At, Cell]:
    cells = {At(row, col): Cell()
      for col in range(self.cols)
      for row in range(self.rows)
    }

    for at in cells:
      north_cell = cells.get(at.north())
      north_neighbor = north_cell and Neighbor(north_cell, False)

      south_cell = cells.get(at.south())
      south_neighbor = south_cell and Neighbor(south_cell, False)

      east_cell = cells.get(at.east())
      east_neighbor = east_cell and Neighbor(east_cell, False)

      west_cell = cells.get(at.west())
      west_neighbor = west_cell and Neighbor(west_cell, False)

      cells[at] = Cell(
        north=north_neighbor,
        south=south_neighbor,
        east=east_neighbor,
        west=west_neighbor
      )

    return cells

  def _validate_at(self, at: At):
    if at not in self.cells:
      raise IndexError(f'No cell at {at}')