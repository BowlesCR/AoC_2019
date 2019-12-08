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

def fillGrid(line: str, grid: List[List[int]], LR: int, UD: int):
  count: int = 0

  for token in line.split(','):
    d = token[0]
    m = int(token[1:])
    if d == 'R':
      for x in range (LR+1, LR+m+1):
        count += 1
        if grid[x][UD] == 0:
          grid[x][UD] = count
      LR += m
    elif d == 'L':
      for x in range (LR-1, LR-m-1, -1):
        count += 1
        if grid[x][UD] == 0:
          grid[x][UD] = count
      LR -= m
    elif d == 'U':
      for y in range (UD+1, UD+m+1):
        count += 1
        if grid[LR][y] == 0:
          grid[LR][y] = count
      UD += m
    elif d == 'D':
      for y in range (UD-1, UD-m-1, -1):
        count += 1
        if grid[LR][y] == 0:
          grid[LR][y] = count
      UD -= m

def main():
  
  grid1: List[List[int]]
  grid2: List[List[int]]
  
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
  
  print('Building Grid 1')
  grid1 = [[0]*(origUD + max(tup1[1][1], tup2[1][1]) + 1) for j in range(origLR + max(tup1[0][1], tup2[0][1]) + 1)]

  print('Building Grid 2')
  grid2 = [[0]*(origUD + max(tup1[1][1], tup2[1][1]) + 1) for j in range(origLR + max(tup1[0][1], tup2[0][1]) + 1)]
  
  print('Filling Grid 1') 
  fillGrid(line1, grid1, origLR, origUD)

  print('Filling Grid 2')
  fillGrid(line2, grid2, origLR, origUD)

  dist: int = float("inf")

  print('Searching')

  for LR in range(len(grid1)):
    for UD in range(len(grid1[LR])):
      
      if grid1[LR][UD] != 0 and grid2[LR][UD] != 0:
        dist = min(dist, grid1[LR][UD]+grid2[LR][UD])
        print(dist)

if __name__ == '__main__':
    main()