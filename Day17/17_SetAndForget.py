import fileinput
import sys
from typing import List, Dict, Tuple

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        grid: Dict[Tuple[int, int], str] = {}

        intcode: IntCode = IntCode(stack)

        x: int = 0
        y: int = 0
        while not intcode.is_halted():
            output = intcode.run()
            if not intcode.is_halted():
                sys.stdout.write(chr(output))

                if output == 35:
                    grid[(x, y)] = chr(output)

                if output == 10:
                    x = 0
                    y += 1
                elif output != 10:
                    x += 1

        # grid = {
        #     (2, 0): '#',
        #     (2, 1): '#',
        #
        #     (0, 2): '#',
        #     (1, 2): '#',
        #     (2, 2): '#',
        #     (3, 2): '#',
        #     (4, 2): '#',
        #     (5, 2): '#',
        #     (6, 2): '#',
        #     (10, 2): '#',
        #     (11, 2): '#',
        #     (12, 2): '#',
        #
        #     (0, 3): '#',
        #     (2, 3): '#',
        #     (6, 3): '#',
        #     (10, 3): '#',
        #     (12, 3): '#',
        #
        #     (0, 4): '#',
        #     (1, 4): '#',
        #     (2, 4): '#',
        #     (3, 4): '#',
        #     (4, 4): '#',
        #     (5, 4): '#',
        #     (6, 4): '#',
        #     (7, 4): '#',
        #     (8, 4): '#',
        #     (9, 4): '#',
        #     (10, 4): '#',
        #     (11, 4): '#',
        #     (12, 4): '#',
        #
        #     (2, 5): '#',
        #     (6, 5): '#',
        #     (10, 5): '#',
        #
        #     (2, 6): '#',
        #     (3, 6): '#',
        #     (4, 6): '#',
        #     (5, 6): '#',
        #     (6, 6): '#',
        #     (10, 6): '#',
        #
        # }

        sum: int = 0
        for i in grid.keys():
            if grid.get(i) and grid.get((i[0] - 1, i[1])) and grid.get((i[0] + 1, i[1])) and grid.get(
                    (i[0], i[1] - 1)) and grid.get((i[0], i[1] + 1)):
                print(i)
                sum += (i[0] * i[1])

        print(sum)


if __name__ == '__main__':
    main()
