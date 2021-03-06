import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        boost: IntCode = IntCode(stack)
        boost.inpt(2)

        while not boost.is_halted():
            print(boost.run())


if __name__ == '__main__':
    main()
