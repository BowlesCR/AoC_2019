'''
Created on Dec 4, 2019

@author: cbowles
'''

import fileinput
from typing import List

def main():
  for line in fileinput.input():
    stack: List(int) = [int(x) for x in line.split(',')]

    stack[1] = 12
    stack[2] = 2

    pos: int = 0
    
    
    while(True):
      print(stack)
      print(stack[pos:pos+4])
      if stack[pos] == 99:
        print(stack[0])
        break;
      elif stack[pos] == 1:
        stack[stack[pos+3]] = stack[stack[pos+1]] + stack[stack[pos+2]]
      elif stack[pos] == 2:
        stack[stack[pos+3]] = stack[stack[pos+1]] * stack[stack[pos+2]]
      else:
        print(f'Panic! Pos: {pos}')
        print(stack)
      pos += 4
        
    

if __name__ == '__main__':
    main()