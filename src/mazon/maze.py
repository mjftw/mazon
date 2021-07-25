import random
from typing import Optional

from mazon.at import At
from mazon.grid import Grid

def binaryTree(rows: int, cols: int, seed: Optional[int] = None) -> Grid:
  if seed is not None:
    random.seed(seed)

  grid = Grid(rows, cols)

  for row in range(grid.rows):
    for col in range(grid.cols):
      rand = random.randint(1, 100)
      at = At(row, col)
      if rand > 50:
        grid.link_north(at) or grid.link_east(at)
      else:
        grid.link_east(at) or grid.link_north(at)

  return grid
