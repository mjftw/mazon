import random
from typing import List, Optional
from mazon.at import At

from mazon.grid import Grid

def binary_tree(rows: int, cols: int, seed: Optional[int] = None) -> Grid:
  if seed is not None:
    random.seed(seed)

  grid = Grid(rows, cols)

  for row in grid.row_idx_ns():
    for at, _ in grid.row_we(row):
      if random.choice([True, False]):
        grid.link_north(at) or grid.link_east(at)
      else:
        grid.link_east(at) or grid.link_north(at)

  return grid

def sidewinder(rows: int, cols: int, seed: Optional[int] = None) -> Grid:
  if seed is not None:
    random.seed(seed)

  grid = Grid(rows, cols)
  run: List[At] = []

  for row in grid.row_idx_ns():
    for at, _ in grid.row_we(row):
      run.append(at)
      # If True or can't link east, link north. If that fails, link east regardless.
      if random.choice([True, False]) or not grid.link_east(at):
        grid.link_north(random.choice(run)) or grid.link_east(at)
        run = []

  return grid