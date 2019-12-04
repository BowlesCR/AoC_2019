'''
Created on Dec 4, 2019

@author: cbowles
'''

import fileinput
from typing import List

def main():
  for line in fileinput.input():

    for noun in range(100):
      for verb in range(100):

        stack: List(int) = [int(x) for x in line.split(',')]

        stack[1] = noun
        stack[2] = verb
    
        pos: int = 0
        
        try:
          while(True):
            #print(stack)
            #print(stack[pos:pos+4])
            if stack[pos] == 99:
              print(stack[0])
              break;
            elif stack[pos] == 1:
              stack[stack[pos+3]] = stack[stack[pos+1]] + stack[stack[pos+2]]
            elif stack[pos] == 2:
              stack[stack[pos+3]] = stack[stack[pos+1]] * stack[stack[pos+2]]
            else:
              #print(f'Panic! Pos: {pos}')
              #print(stack)
              break;
            pos += 4
  
        except:
          pass
          
        if stack[0] == 19690720:
          print(100*noun+verb)
          exit()

if __name__ == '__main__':
    main()