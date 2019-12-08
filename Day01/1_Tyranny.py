'''
Created on Dec 4, 2019

@author: cbowles
'''

import fileinput

def main():
  fuel: int = 0
  for line in fileinput.input():
    fuel += (int(line) // 3) - 2
  
  print(fuel)

if __name__ == '__main__':
    main()