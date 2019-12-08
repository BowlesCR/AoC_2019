'''
Created on Dec 4, 2019

@author: cbowles
'''


def main():
  count: int = 0
  for x in range(146810, 612564):
    if adj(x) and nodec(x):
      count += 1
  print(count)

def adj(x: int) -> bool:
  x = str(x)
  return (
    (x[0] == x[1] and x[1] != x[2]) or
    (x[1] == x[2] and x[0] != x[1] and x[2] != x[3]) or
    (x[2] == x[3] and x[1] != x[2] and x[3] != x[4]) or
    (x[3] == x[4] and x[2] != x[3] and x[4] != x[5]) or
    (x[4] == x[5] and x[3] != x[4]) 
    )

def nodec(x: int) -> bool:
  x = str(x)
  return int(x[0]) <= int(x[1]) and int(x[1]) <= int(x[2]) and int(x[2]) <= int(x[3]) and int(x[3]) <= int(x[4]) and int(x[4]) <= int(x[5]) 
  

if __name__ == '__main__':
    main()