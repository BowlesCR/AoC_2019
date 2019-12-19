import fileinput
from typing import List, Tuple, Set

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        grid: Set[Tuple[int, int]] = set()

        out = 0

        tgtSize = 100 - 1
        gridSize = 10000

        minX = 0
        maxX = 0

        for y in range(0, gridSize):
            row: Set[Tuple[int, int]] = set()

            foundMax = False
            for x in range(maxX, -1, -1):
                intcode: IntCode = IntCode(stack[:])
                intcode.inpt(x)
                intcode.inpt(y)

                if intcode.run() == 1:
                    grid.add((x, y))
                    row.add((x, y))
                    if (x - tgtSize, y) in grid and (x, y - tgtSize) in grid:
                        out = ((x - tgtSize) * 10000) + (y - tgtSize)
                    foundMax = True
                elif foundMax:
                    break

            foundMin = False
            for x in range(minX, gridSize):
                intcode: IntCode = IntCode(stack[:])
                intcode.inpt(x)
                intcode.inpt(y)

                if intcode.run() == 1:
                    grid.add((x, y))
                    row.add((x, y))
                    if (x - tgtSize, y) in grid and (x, y - tgtSize) in grid:
                        out = ((x - tgtSize) * 10000) + (y - tgtSize)
                    foundMin = True
                elif foundMin:
                    break

            if out > 0:
                break

            rowX = [i[0] for i in row]
            if rowX:
                minX = min(rowX)
                maxX = max(rowX)

            print(f'y: {y}')

        print(f'len: {len(grid)}')
        print(f'output: {out}')
    pass


if __name__ == '__main__':
    main()
