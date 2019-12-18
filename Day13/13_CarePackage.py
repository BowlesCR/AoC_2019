import fileinput
import sys
from typing import List, Dict, Tuple

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        arcade: IntCode = IntCode(stack)
        grid: Dict[Tuple[int, int], int] = {}
        x: int = 0
        y: int = 0

        minX: int = 0
        maxX: int = 0
        minY: int = 0
        maxY: int = 0

        while not arcade.is_halted():

            x = arcade.run()
            if not arcade.is_halted():
                y = arcade.run()
                tileID = arcade.run()

                minX = min(minX, x)
                maxX = max(maxX, x)
                minY = min(minY, y)
                maxY = max(minY, y)

                grid[(x, y)] = tileID

        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                tileID = grid.get((x, y), 0)
                if tileID == 0:
                    sys.stdout.write(' ')
                elif tileID == 1:
                    sys.stdout.write('X')
                elif tileID == 2:
                    sys.stdout.write('#')
                elif tileID == 3:
                    sys.stdout.write('=')
                elif tileID == 4:
                    sys.stdout.write('*')

            sys.stdout.write("\n")

        print(len([tile for tile in grid.values() if tile == 2]))


if __name__ == '__main__':
    main()
