"""
Created on Dec 5, 2019

@author: cbowles
"""

import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        intcode = IntCode(stack)

        intcode.inpt(1)
        while not intcode.is_halted():
            print(intcode.run())


if __name__ == '__main__':
    main()
