

from typing import Callable, List, TypeVar,  Union
A = TypeVar('A')
B = TypeVar('B')

def map2d(f: Callable[[A], B], items: List[List[A]]) -> List[List[B]]:
  return [[f(item) for item in rows] for rows in items]

def get_or_else(l: List[List[A]], row: int, col: int, otherwise: B) -> Union[A, B]:
  try:
    return l[row][col]
  except IndexError:
    return otherwise