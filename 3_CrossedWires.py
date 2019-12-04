'''
Created on Dec 3, 2019

@author: cbowles
'''

import fileinput

from typing import List, Tuple

def findRange(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
  minLR: int = 0
  maxLR: int = 0
  minUD: int = 0
  maxUD: int = 0

  LR: int = 0
  UD: int = 0
    
  for token in line.split(','):
    d = token[0]
    m = int(token[1:])
    if d == 'R':
      LR += m
      maxLR = max(LR, maxLR)
    elif d == 'L':
      LR -= m
      minLR = min(LR, minLR)
    elif d == 'U':
      UD += m
      maxUD = max(UD, maxUD)
    elif d == 'D':
      UD -= m
      minUD = min(UD, minUD)
  return ((minLR, maxLR), (minUD, maxUD))

def fillGrid(line: str, grid: List[List[int]], value: int, LR: int, UD: int):
  for token in line.split(','):
    d = token[0]
    m = int(token[1:])
    if d == 'R':
      for x in range (LR+1, LR+m):
        grid[x][UD] |= value
      LR += m
    elif d == 'L':
      for x in range (LR-1, LR-m, -1):
        grid[x][UD] |= value
      LR -= m
    elif d == 'U':
      for y in range (UD+1, UD+m):
        grid[LR][y] |= value
      UD += m
    elif d == 'D':
      for y in range (UD-1, UD-m, -1):
        grid[LR][y] |= value
      UD -= m


def main():
  
  grid: List[List[int]]
  
  line1: str = None
  line2: str = None
  
  for line in fileinput.input():
    if line1 == None:
      line1 = line
    else:
      line2 = line

  tup1 = findRange(line1)
  tup2 = findRange(line2)
    

  origLR: int = min(tup1[0][0], tup2[0][0]) * -1
  origUD: int = min(tup1[1][0], tup2[1][0]) * -1
  grid = [[0]*(origUD + max(tup1[1][1], tup2[1][1]) + 1) for j in range(origLR + max(tup1[0][1], tup2[0][1]) + 1)]


  fillGrid(line1, grid, 1, origLR, origUD)
  fillGrid(line2, grid, 2, origLR, origUD)

  dist: int = float("inf")

  for LR in range(len(grid)):
    for UD in range(len(grid[LR])):
      
      if grid[LR][UD] == 3:
        dist = min(dist, md((origLR, origUD), (LR, UD)))
        print(dist)


def md(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

if __name__ == '__main__':
    main()