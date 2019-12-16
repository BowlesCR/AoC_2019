import fileinput
from typing import List


def generatePattern(pos: int) -> List[int]:
    basePattern: List[int] = [0, 1, 0, -1]
    skipped = False
    count: int = -1  # start at -1 because of skipping the first element
    while True:
        for x in basePattern:
            for y in range(pos + 1):
                if skipped:
                    yield x
                else:
                    skipped = True


def main():
    for line in fileinput.input():
        inputList: List[int] = [int(line[i]) for i in range(len(line))]

        for phase in range(100):
            # pprint(inputList, width=4000)
            # pprint(basePattern)
            sum = 0
            for i in range(len(inputList)):
                inpt: int = inputList[i]
                sum = 0
                for tup in zip(inputList, generatePattern(i)):
                    sum += tup[0] * tup[1]

                # print(f'Sum: {sum}, {abs(sum) % 10}')
                inputList[i] = abs(sum) % 10
        print(f'After {phase + 1} phases: {"".join([str(x) for x in inputList][:8])}')


if __name__ == '__main__':
    main()
