'''
Created on Dec 4, 2019

@author: cbowles
'''

import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        for noun in range(100):
            for verb in range(100):
                intcode = IntCode(stack[:])

                intcode.stack[1] = noun
                intcode.stack[2] = verb

                intcode.run()

                if intcode.stack[0] == 19690720:
                    print(100 * noun + verb)
                    exit()


if __name__ == '__main__':
    main()
