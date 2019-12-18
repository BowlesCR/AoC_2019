import fileinput
import sys
from typing import List, Dict, Tuple

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        robot: IntCode = IntCode(stack)
        panels: Dict[Tuple[int, int], int] = {}
        x: int = 0
        y: int = 0

        dirs = "NESW"
        minX: int = 0
        maxX: int = 0
        minY: int = 0
        maxY: int = 0
        d: int = 0

        while not robot.is_halted():
            robot.inpt(panels.get((x, y), 0))

            color = robot.run()
            if color is not None:
                panels[(x, y)] = color

            turn = robot.run()
            if turn is not None:
                d += int((turn - .5) * 2)
                d %= 4

            if dirs[d] == 'N':
                y -= 1
                minY = min(minY, y)
            elif dirs[d] == 'E':
                x += 1
                maxX = max(maxX, x)
            elif dirs[d] == 'S':
                y += 1
                maxY = max(maxY, y)
            elif dirs[d] == 'W':
                x -= 1
                minX = min(minX, x)

        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                sys.stdout.write("#" if panels.get((x, y), 0) else " ")
            sys.stdout.write("\n")

        print(len(panels.keys()))


if __name__ == '__main__':
    main()
