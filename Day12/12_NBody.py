import fileinput
import re
from typing import List, Tuple


def main():
    moons: List[Tuple[List[int], List[int]]] = []
    for line in fileinput.input():
        pos = re.findall(r'^<x=(.+), y=(.+), z=(.+)>$', line)
        moons.append(
            (
                [int(pos[0][0]), int(pos[0][1]), int(pos[0][2])],
                [0, 0, 0]
            )
        )

    for x in range(1000):
        # Set Velocities
        for i in range(len(moons)):
            for j in range(i + 1, len(moons)):

                for k in range(3):
                    cmp = moons[i][0][k] - moons[j][0][k]
                    if cmp < 0:
                        moons[i][1][k] += 1
                        moons[j][1][k] -= 1
                    elif cmp > 0:
                        moons[i][1][k] -= 1
                        moons[j][1][k] += 1

        for i in range(len(moons)):
            for k in range(3):
                moons[i][0][k] += moons[i][1][k]

    total: int = 0
    for moon in moons:
        print(moon)
        total += (abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])) * \
                 (abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2]))
    print(f'Energy: {total}')


if __name__ == '__main__':
    main()
