import fileinput
import re
from math import gcd
from typing import List, Tuple, Set


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


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

    states: list[Set[str]] = [set()] * 3
    for i in range(3):
        concat = ",".join([str(moon[0][i]) for moon in moons] + [str(moon[1][i]) for moon in moons])
        print(i, concat)
        states[i].add(concat)

    repeats: List[int] = [0] * 3

    for x in range(4686774925):
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

        for i in range(3):
            if repeats[i] > 0:
                continue
            concat = ",".join([str(moon[0][i]) for moon in moons] + [str(moon[1][i]) for moon in moons])
            if concat in states[i]:
                repeats[i] = x + 1
            else:
                states[i].add(concat)

        if len([x for x in repeats if x == 0]) == 0:
            print(repeats)
            print(lcm(lcm(repeats[0], repeats[1]), repeats[2]))
            break

        print(x)


if __name__ == '__main__':
    main()
