import fileinput
import math
from typing import List, Set, Tuple


def findBestLoc(grid: List[str]) -> Tuple[int, Tuple[int, int]]:
    maxAsteroids: int = 0
    maxCoords: Tuple[int, int]

    for y1 in range(len(grid)):
        for x1 in range(len(grid[0])):
            if grid[y1][x1] == '#':
                count: int = 0
                blocked: Set[Tuple[int, int]] = set()

                for rise in sorted(range(0 - y1, len(grid) - y1), key=abs):
                    for run in sorted(range(0 - x1, len(grid) - x1), key=abs):
                        if rise == 0 and run == 0:
                            continue
                        counted: bool = False
                        y2 = y1 + rise
                        x2 = x1 + run
                        while 0 <= y2 < len(grid) and 0 <= x2 < len(grid):
                            if grid[y2][x2] == '#':
                                tup = (y2, x2)
                                if not counted and tup not in blocked:
                                    count += 1
                                    counted = True
                                blocked.add(tup)
                            y2 += rise
                            x2 += run

                if count > maxAsteroids:
                    maxAsteroids = count
                    maxCoords = (x1, y1)

    return maxAsteroids, maxCoords


def calcHeadings(grid: List[str], best: Tuple[int, Tuple[int, int]]) -> List[Tuple[Tuple[int, int], float, float]]:
    asteroids: List[Tuple[Tuple[int, int], float, float]] = []
    x1 = best[1][0]
    y1 = best[1][1]
    for y2 in range(len(grid)):
        for x2 in range(len(grid[0])):
            if grid[y2][x2] == '#' and (x2 != x1 or y2 != y1):
                dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                heading = math.pi / 2 + math.atan2(y2 - y1, x1 - x2)
                heading = 360 - math.degrees(heading)
                if heading >= 360:
                    heading -= 360
                asteroids.append(((x2, y2), heading, dist))
    return asteroids


def main():
    grid: List[str] = []
    for line in fileinput.input():
        grid.append(line.rstrip())

    best = findBestLoc(grid)

    asteroids: List[Tuple[Tuple[int, int], float, float]] = calcHeadings(grid, best)

    asteroids.sort(key=lambda asteroid: asteroid[2])
    asteroids.sort(key=lambda asteroid: asteroid[1])
    count = 0
    angle = -1
    while asteroids:
        candidates = [asteroid for asteroid in asteroids if asteroid[1] > angle]
        if candidates:
            asteroids.remove(candidates[0])
            angle = candidates[0][1]
            count += 1
            if count == 200:
                print(candidates[0][0][0] * 100 + candidates[0][0][1])
                break
        else:
            angle = -1


if __name__ == '__main__':
    main()
