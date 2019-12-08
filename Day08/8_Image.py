import fileinput
from typing import Dict


def main():
    for line in fileinput.input():

        counts: Dict[int, int] = {}

        for i in range(0, len(line), 150):
            layer = line[i: i + 150]
            counts[i] = layer.count('0')

        minZeros = min(counts.values())
        for i, count in counts.items():
            if count == minZeros:
                layer = line[i: i + 150]
                print(layer.count('1') * layer.count('2'))


if __name__ == '__main__':
    main()
