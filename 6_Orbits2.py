import fileinput
from typing import List, Dict

orbits: Dict[str, str] = {}


def listOrbits(obj: str) -> List[str]:
    if obj in orbits:
        chain: List[str] = listOrbits(orbits[obj])
        chain.append(obj)
        return chain
    else:
        return []


def main():
    for line in fileinput.input():
        tokens = line.rstrip().split(')')
        orbits[tokens[1]] = tokens[0]

    you: List[str] = listOrbits('YOU')
    san: List[str] = listOrbits('SAN')

    you.reverse()

    for obj in you[1:]:
        if obj in san:
            transfers: int = you.index(obj) + len(san) - san.index(obj)
            transfers -= 3  # Account for YOU, SAN, and double-counting the common root object
            print(transfers)
            break


if __name__ == '__main__':
    main()
