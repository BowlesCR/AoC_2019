'''
Created on Dec 4, 2019

@author: cbowles
'''

import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List(int) = [int(x) for x in line.split(',')]

        stack[1] = 12
        stack[2] = 2

        intcode = IntCode(stack)

        intcode.run()
        print(intcode.stack[0])


if __name__ == '__main__':
    main()
