import fileinput
from typing import List

from IntCode import IntCode


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        intcode: IntCode = IntCode(stack)

        intcode.stack[0] = 2

        M = 'A,B,A,C,B,C,B,C,A,C'
        for char in M:
            intcode.inpt(ord(char))
        intcode.inpt(10)
        A = 'L,10,R,12,R,12'
        for char in A:
            intcode.inpt(ord(char))
        intcode.inpt(10)
        B = 'R,6,R,10,L,10'
        for char in B:
            intcode.inpt(ord(char))
        intcode.inpt(10)
        C = 'R,10,L,10,L,12,R,6'
        for char in C:
            intcode.inpt(ord(char))
        intcode.inpt(10)

        intcode.inpt(ord('n'))
        intcode.inpt(10)

        while not intcode.is_halted():
            # output = intcode.run()
            # if not intcode.is_halted():
            #     print(chr(output), end="")
            print(intcode.run())


# L,10,R,12,R,12,R,6,R,10,L,10,L,10,R,12,R,12,R,10,L,10,L,12,R,6,R,6,R,10,L,10,R,10,L,10,L,12,R,6,R,6,R,10,L,10,R,10,L,10,L,12,R,6,L,10,R,12,R,12,R,10,L,10,L,12,R,6
#
# a: R,12
# b: L,10
# c: R,6
# d: R,10
# e: L,12

#
# baa cdb baa dbec cdb dbec cdb dbec baa dbec
#
#     12345678901234567890
# M = A,B,A,C,B,C,B,C,A,C
# A = L,10,R,12,R,12
# B = R,6,R,10,L,10
# C = R,10,L,10,L,12,R,6


if __name__ == '__main__':
    main()
