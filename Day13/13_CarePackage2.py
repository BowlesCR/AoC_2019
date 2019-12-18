import fileinput
import sys
from typing import List, Dict, Tuple

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        stack[0] = 2

        arcade: IntCode = IntCode(stack)
        grid: Dict[Tuple[int, int], int] = {}
        x: int = 0
        y: int = 0

        minX: int = 0
        maxX: int = 0
        minY: int = 0
        maxY: int = 0

        score: int = 0

        while not arcade.is_halted():

            paddlePos = (0, 0)
            ballPos = (0, 0)
            paddleDir = 0

            for tile in [tile for tile in grid if grid[tile] in [3, 4]]:
                if grid[tile] == 3:
                    paddlePos = tile
                if grid[tile] == 4:
                    ballPos = tile

            if ballPos[0] < paddlePos[0]:
                paddleDir = -1
            elif ballPos[0] == paddlePos[0]:
                paddleDir = 0
            elif ballPos[0] > paddlePos[0]:
                paddleDir = 1

            arcade.input = [paddleDir]

            x = arcade.run()
            if not arcade.is_halted():
                y = arcade.run()
                tileID = arcade.run()

                if x == -1 and y == 0:
                    score = tileID

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

        # print(len([tile for tile in grid.values() if tile == 2]))
        print(score)


if __name__ == '__main__':
    main()
