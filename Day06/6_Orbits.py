import fileinput
from typing import Dict

orbits: Dict[str, str] = {}


def countOrbits(obj: str) -> int:
    if obj in orbits:
        return countOrbits(orbits[obj]) + 1
    else:
        return 0


def main():
    for line in fileinput.input():
        tokens = line.rstrip().split(')')
        orbits[tokens[1]] = tokens[0]

    total: int = 0

    for obj in orbits.keys():
        total += countOrbits(obj)

    print(total)


if __name__ == '__main__':
    main()
