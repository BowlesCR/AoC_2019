import fileinput
from itertools import permutations
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        maxOutput: int = 0

        for phases in permutations(range(5, 10)):

            a: IntCode = IntCode(stack[:])
            a.inpt(phases[0])
            a.inpt(0)
            b: IntCode = IntCode(stack[:])
            b.inpt(phases[1])
            c: IntCode = IntCode(stack[:])
            c.inpt(phases[2])
            d: IntCode = IntCode(stack[:])
            d.inpt(phases[3])
            e: IntCode = IntCode(stack[:])
            e.inpt(phases[4])

            while True:
                b.inpt(a.run())
                c.inpt(b.run())
                d.inpt(c.run())
                e.inpt(d.run())
                a.inpt(e.run())

                if e.is_halted():
                    maxOutput = max(maxOutput, e.out())
                    break

        print(maxOutput)


if __name__ == '__main__':
    main()
