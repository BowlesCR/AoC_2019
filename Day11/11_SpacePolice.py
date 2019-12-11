import fileinput
import sys
from typing import List, Dict, Tuple


class IntCode:

    def __init__(self, stack: List[int]):
        self.stack: List[int] = stack
        self.stack += [0] * 10000
        self.input: List[int] = []
        self.pc: int = 0
        self.rb: int = 0
        self.output = None

    def is_halted(self) -> bool:
        return self.stack[self.pc] == 99

    def inpt(self, inpt: int):
        self.input.append(inpt)

    def out(self) -> int:
        return self.output

    def run(self) -> int:
        while True:

            opcode: int = self.stack[self.pc] % 100
            mode1: int = (self.stack[self.pc] // 100) % 10
            mode2: int = (self.stack[self.pc] // 1000) % 10
            mode3: int = (self.stack[self.pc] // 10000) % 10

            p1addy: int = -1  # Initializing these just to squelch the warning.
            p2addy: int = -1
            p3addy: int = -1

            if mode1 == 0:
                p1addy: int = self.stack[self.pc + 1]
            elif mode1 == 1:
                p1addy: int = self.pc + 1
            elif mode1 == 2:
                p1addy: int = self.stack[self.pc + 1] + self.rb

            if mode2 == 0:
                p2addy: int = self.stack[self.pc + 2]
            elif mode2 == 1:
                p2addy: int = self.pc + 2
            elif mode2 == 2:
                p2addy: int = self.stack[self.pc + 2] + self.rb

            if mode3 == 0:
                p3addy: int = self.stack[self.pc + 3]
            elif mode3 == 1:
                p3addy: int = self.pc + 3
            elif mode3 == 2:
                p3addy: int = self.stack[self.pc + 3] + self.rb

            if opcode == 99:
                break  # halt
            elif opcode == 1:  # add
                self.stack[p3addy] = self.stack[p1addy] + self.stack[p2addy]
                self.pc += 4
            elif opcode == 2:  # mult
                self.stack[p3addy] = self.stack[p1addy] * self.stack[p2addy]
                self.pc += 4
            elif opcode == 3:  # input
                self.stack[p1addy] = self.input.pop(0)
                self.pc += 2
            elif opcode == 4:  # output
                self.pc += 2
                self.output = self.stack[p1addy]
                return self.stack[p1addy]
            elif opcode == 5:  # Branch neq 0
                if self.stack[p1addy] != 0:
                    self.pc = self.stack[p2addy]
                else:
                    self.pc += 3
            elif opcode == 6:  # Branch eq 0
                if self.stack[p1addy] == 0:
                    self.pc = self.stack[p2addy]
                else:
                    self.pc += 3
            elif opcode == 7:  # Less than
                self.stack[p3addy] = int(self.stack[p1addy] < self.stack[p2addy])
                self.pc += 4
            elif opcode == 8:  # Equal
                self.stack[p3addy] = int(self.stack[p1addy] == self.stack[p2addy])
                self.pc += 4
            elif opcode == 9:  # RB offset
                self.rb += self.stack[p1addy]
                self.pc += 2
            else:
                print(f"Panic! PC: {self.pc}")
                print(self.stack)
                break

    pass


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        robot: IntCode = IntCode(stack)
        panels: Dict[Tuple[int, int], int] = {}
        x: int = 0
        y: int = 0

        dirs = "NESW"
        minX: int = 0
        maxX: int = 0
        minY: int = 0
        maxY: int = 0
        d: int = 0

        while not robot.is_halted():
            robot.inpt(panels.get((x, y), 0))

            color = robot.run()
            if color is not None:
                panels[(x, y)] = color

            turn = robot.run()
            if turn is not None:
                d += int((turn - .5) * 2)
                d %= 4

            if dirs[d] == 'N':
                y -= 1
                minY = min(minY, y)
            elif dirs[d] == 'E':
                x += 1
                maxX = max(maxX, x)
            elif dirs[d] == 'S':
                y += 1
                maxY = max(maxY, y)
            elif dirs[d] == 'W':
                x -= 1
                minX = min(minX, x)

        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                sys.stdout.write("#" if panels.get((x, y), 0) else " ")
            sys.stdout.write("\n")

        print(len(panels.keys()))


if __name__ == '__main__':
    main()
