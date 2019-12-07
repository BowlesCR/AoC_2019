import fileinput
from typing import List


def intCode(stack: List[int], usrInput: List[int]) -> int:
    pos: int = 0

    while True:

        opcode: int = stack[pos] % 100
        mode1: int = (stack[pos] // 100) % 10
        mode2: int = (stack[pos] // 1000) % 10
        mode3: int = (stack[pos] // 10000) % 10

        param1: int
        param2: int
        param3: int

        if opcode in [1, 2, 4, 5, 6, 7, 8]:  # Takes 1+ input params
            if mode1 == 0:
                param1: int = stack[stack[pos + 1]]
            elif mode1 == 1:
                param1: int = stack[pos + 1]

        if opcode in [1, 2, 5, 6, 7, 8]:  # Takes 2+ input params
            if mode2 == 0:
                param2: int = stack[stack[pos + 2]]
            elif mode2 == 1:
                param2: int = stack[pos + 2]

        if opcode in []:  # Takes 3 input params
            if mode3 == 0:
                param3: int = stack[stack[pos + 3]]
            elif mode3 == 1:
                param3: int = stack[pos + 3]

        if opcode == 99:
            break  # halt
        elif opcode == 1:  # add
            stack[stack[pos + 3]] = param1 + param2
            pos += 4
        elif opcode == 2:  # mult
            stack[stack[pos + 3]] = param1 * param2
            pos += 4
        elif opcode == 3:  # input
            stack[stack[pos + 1]] = usrInput.pop(0)
            pos += 2
        elif opcode == 4:  # output
            return param1
            pos += 2
        elif opcode == 5:  # Branch neq 0
            if param1 != 0:
                pos = param2
            else:
                pos += 3
        elif opcode == 6:  # Branch eq 0
            if param1 == 0:
                pos = param2
            else:
                pos += 3
        elif opcode == 7:  # Less than
            stack[stack[pos + 3]] = int(param1 < param2)
            pos += 4
        elif opcode == 8:  # Equal
            stack[stack[pos + 3]] = int(param1 == param2)
            pos += 4
        else:
            print(f'Panic! Pos: {pos}')
            print(stack)
            break


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        output: int = 0

        for phaseA in range(5):
            for phaseB in range(5):
                if phaseB in [phaseA]:
                    continue
                for phaseC in range(5):
                    if phaseC in [phaseA, phaseB]:
                        continue
                    for phaseD in range(5):
                        if phaseD in [phaseA, phaseB, phaseC]:
                            continue
                        for phaseE in range(5):
                            if phaseE in [phaseA, phaseB, phaseC, phaseD]:
                                continue
                            a = intCode(stack[:], [phaseA, 0])
                            b = intCode(stack[:], [phaseB, a])
                            c = intCode(stack[:], [phaseC, b])
                            d = intCode(stack[:], [phaseD, c])
                            e = intCode(stack[:], [phaseE, d])

                            output = max(output, e)

        print(output)


if __name__ == '__main__':
    main()
