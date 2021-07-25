from dataclasses import dataclass, field
from typing import Optional, Set

@dataclass(frozen=True)
class Neighbor:
  cell: 'Cell'
  is_linked: bool

@dataclass(frozen=True)
class Cell:
  north: Optional[Neighbor] = field(default_factory=lambda: None)
  east: Optional[Neighbor] = field(default_factory=lambda: None)
  south: Optional[Neighbor] = field(default_factory=lambda: None)
  west: Optional[Neighbor] = field(default_factory=lambda: None)

  @property
  def neighbors(self) -> Set[Neighbor]:
    neighbors: Set[Neighbor] = set()

    if self.north:
      neighbors.add(self.north)
    if self.east:
      neighbors.add(self.east)
    if self.south:
      neighbors.add(self.south)
    if self.west:
      neighbors.add(self.west)

    return neighbors

  def __repr__(self) -> str:
    n = "_" if not self.north else ('N' if self.north.is_linked else "n")
    s = "_" if not self.south else ('S' if self.south.is_linked else "s")
    e = "_" if not self.east else ('E' if self.east.is_linked else "e")
    w = "_" if not self.west else ('W' if self.west.is_linked else "w")
    return f"Cell[{n}{s}{e}{w}]"