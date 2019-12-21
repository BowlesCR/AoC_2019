import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        intcode = IntCode(stack)

        program: List[str] = [
            'NOT H J',
            'OR C J',
            'AND B J',
            'AND A J',
            'NOT J J',
            'AND D J',
            'RUN'
        ]

        for char in '\n'.join(program) + '\n':
            intcode.inpt(ord(char))

        while not intcode.is_halted():
            out = intcode.run()
            if not intcode.is_halted():
                print(chr(out), end='')
            else:
                print()
                print(out)

    pass


if __name__ == '__main__':
    main()
