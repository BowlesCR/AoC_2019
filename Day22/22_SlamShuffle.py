import fileinput
import re
from typing import List


def main():
    deck: List[int] = [x for x in range(10007)]

    for line in fileinput.input():
        line = line.rstrip()

        if line == "deal into new stack":
            deck.reverse()
        else:
            result = re.match(r'^(.*) (-?\d+)', line)
            inst: str = result.group(1)
            num: int = int(result.group(2))

            if inst == "cut":
                newdeck: List[int] = deck[num:] + deck[:num]
                deck = newdeck
            elif inst == "deal with increment":
                newdeck: List[int] = [-1] * len(deck)
                pos: int = 0
                while len(deck):
                    newdeck[pos] = deck.pop(0)
                    pos += num
                    pos %= len(newdeck)
                deck = newdeck

    print(deck.index(2019))


if __name__ == '__main__':
    main()
