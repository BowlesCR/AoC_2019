import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        sum: int = 0

        for y in range(50):
            for x in range(50):
                intcode: IntCode = IntCode(stack[:])
                intcode.inpt(x)
                intcode.inpt(y)
                sum += intcode.run()
        print(sum)

    pass


if __name__ == '__main__':
    main()
