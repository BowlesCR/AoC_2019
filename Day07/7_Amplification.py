import fileinput
from itertools import permutations
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        output: int = 0

        for phases in permutations(range(5)):
            a = IntCode(stack[:])
            a.inpt(phases[0])
            a.inpt(0)

            b = IntCode(stack[:])
            b.inpt(phases[1])
            b.inpt(a.run())

            c = IntCode(stack[:])
            c.inpt(phases[2])
            c.inpt(b.run())

            d = IntCode(stack[:])
            d.inpt(phases[3])
            d.inpt(c.run())

            e = IntCode(stack[:])
            e.inpt(phases[4])
            e.inpt(d.run())

            output = max(output, e.run())

        print(output)


if __name__ == '__main__':
    main()
