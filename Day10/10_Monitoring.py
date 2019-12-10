import fileinput
from typing import List, Set


def main():
    grid: List[str] = []
    maxAsteroids: int = 0

    for line in fileinput.input():
        grid.append(line.rstrip())

    for y1 in range(len(grid)):
        for x1 in range(len(grid[0])):
            if grid[y1][x1] == '#':
                count: int = 0
                blocked: Set[tuple[int, int]] = set()

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

                # print(f"  {len(slopes)}")
                maxAsteroids = max(maxAsteroids, count)

    print(maxAsteroids)


if __name__ == '__main__':
    main()
