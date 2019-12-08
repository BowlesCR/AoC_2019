import fileinput
from typing import List


class IntCode:

    def __init__(self, stack: List[int], phase: int):
        self.stack: List[int] = stack
        self.input: List[int] = [phase]
        self.pc: int = 0
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

            param1: int
            param2: int
            param3: int

            if opcode in [1, 2, 4, 5, 6, 7, 8]:  # Takes 1+ input params
                if mode1 == 0:
                    param1: int = self.stack[self.stack[self.pc + 1]]
                elif mode1 == 1:
                    param1: int = self.stack[self.pc + 1]

            if opcode in [1, 2, 5, 6, 7, 8]:  # Takes 2+ input params
                if mode2 == 0:
                    param2: int = self.stack[self.stack[self.pc + 2]]
                elif mode2 == 1:
                    param2: int = self.stack[self.pc + 2]

            if opcode in []:  # Takes 3 input params
                if mode3 == 0:
                    param3: int = self.stack[self.stack[self.pc + 3]]
                elif mode3 == 1:
                    param3: int = self.stack[self.pc + 3]

            if opcode == 99:
                break  # halt
            elif opcode == 1:  # add
                self.stack[self.stack[self.pc + 3]] = param1 + param2
                self.pc += 4
            elif opcode == 2:  # mult
                self.stack[self.stack[self.pc + 3]] = param1 * param2
                self.pc += 4
            elif opcode == 3:  # input
                self.stack[self.stack[self.pc + 1]] = self.input.pop(0)
                self.pc += 2
            elif opcode == 4:  # output
                self.pc += 2
                self.output = param1
                return param1
            elif opcode == 5:  # Branch neq 0
                if param1 != 0:
                    self.pc = param2
                else:
                    self.pc += 3
            elif opcode == 6:  # Branch eq 0
                if param1 == 0:
                    self.pc = param2
                else:
                    self.pc += 3
            elif opcode == 7:  # Less than
                self.stack[self.stack[self.pc + 3]] = int(param1 < param2)
                self.pc += 4
            elif opcode == 8:  # Equal
                self.stack[self.stack[self.pc + 3]] = int(param1 == param2)
                self.pc += 4
            else:
                print(f"Panic! PC: {self.pc}")
                print(self.stack)
                break

    pass


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        maxOutput: int = 0

        for phaseA in range(5, 10):
            for phaseB in range(5, 10):
                if phaseB in [phaseA]:
                    continue
                for phaseC in range(5, 10):
                    if phaseC in [phaseA, phaseB]:
                        continue
                    for phaseD in range(5, 10):
                        if phaseD in [phaseA, phaseB, phaseC]:
                            continue
                        for phaseE in range(5, 10):
                            if phaseE in [phaseA, phaseB, phaseC, phaseD]:
                                continue

                            a: IntCode = IntCode(stack[:], phaseA)
                            a.inpt(0)
                            b: IntCode = IntCode(stack[:], phaseB)
                            c: IntCode = IntCode(stack[:], phaseC)
                            d: IntCode = IntCode(stack[:], phaseD)
                            e: IntCode = IntCode(stack[:], phaseE)

                            while True:
                                b.inpt(a.run())
                                c.inpt(b.run())
                                d.inpt(c.run())
                                e.inpt(d.run())
                                a.inpt(e.run())

                                if e.is_halted():
                                    maxOutput = max(maxOutput, e.out())
                                    break

        print(maxOutput)


if __name__ == '__main__':
    main()
