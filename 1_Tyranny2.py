'''
Created on Dec 4, 2019

@author: cbowles
'''

import fileinput

def main():
  total: int = 0
  for line in fileinput.input():
    total += fuel(int(line))
  
  print(total)

def fuel(mass: int) -> int:
  x: int = (mass // 3) - 2
  if x < 0:
    return 0
  return x + fuel(x)

if __name__ == '__main__':
    main()