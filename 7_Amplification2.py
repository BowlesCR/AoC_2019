import fileinput
from typing import List, Dict, Any


def intCode(state: Dict[str, Any]) -> int:
    while True:

        opcode: int = state['stack'][state['pc']] % 100
        mode1: int = (state['stack'][state['pc']] // 100) % 10
        mode2: int = (state['stack'][state['pc']] // 1000) % 10
        mode3: int = (state['stack'][state['pc']] // 10000) % 10

        param1: int
        param2: int
        param3: int

        if opcode in [1, 2, 4, 5, 6, 7, 8]:  # Takes 1+ input params
            if mode1 == 0:
                param1: int = state['stack'][state['stack'][state['pc'] + 1]]
            elif mode1 == 1:
                param1: int = state['stack'][state['pc'] + 1]

        if opcode in [1, 2, 5, 6, 7, 8]:  # Takes 2+ input params
            if mode2 == 0:
                param2: int = state['stack'][state['stack'][state['pc'] + 2]]
            elif mode2 == 1:
                param2: int = state['stack'][state['pc'] + 2]

        if opcode in []:  # Takes 3 input params
            if mode3 == 0:
                param3: int = state['stack'][state['stack'][state['pc'] + 3]]
            elif mode3 == 1:
                param3: int = state['stack'][state['pc'] + 3]

        if opcode == 99:
            state['halted'] = True
            break  # halt
        elif opcode == 1:  # add
            state['stack'][state['stack'][state['pc'] + 3]] = param1 + param2
            state['pc'] += 4
        elif opcode == 2:  # mult
            state['stack'][state['stack'][state['pc'] + 3]] = param1 * param2
            state['pc'] += 4
        elif opcode == 3:  # input
            state['stack'][state['stack'][state['pc'] + 1]] = state['input'].pop(0)
            state['pc'] += 2
        elif opcode == 4:  # output
            state['pc'] += 2
            return param1
        elif opcode == 5:  # Branch neq 0
            if param1 != 0:
                state['pc'] = param2
            else:
                state['pc'] += 3
        elif opcode == 6:  # Branch eq 0
            if param1 == 0:
                state['pc'] = param2
            else:
                state['pc'] += 3
        elif opcode == 7:  # Less than
            state['stack'][state['stack'][state['pc'] + 3]] = int(param1 < param2)
            state['pc'] += 4
        elif opcode == 8:  # Equal
            state['stack'][state['stack'][state['pc'] + 3]] = int(param1 == param2)
            state['pc'] += 4
        else:
            print(f"Panic! PC: {state['pc']}")
            print(state['stack'])
            break


def main():
    for line in fileinput.input():
        stack: List[int] = [int(x) for x in line.split(',')]

        output: int = 0

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

                            state: Dict[str, Dict[str, Any]] = {
                                'a': {},
                                'b': {},
                                'c': {},
                                'd': {},
                                'e': {},
                            }
                            for s in state:
                                state[s].update({
                                    'stack': stack[:],
                                    'pc': 0
                                })

                            state['a']['input'] = [phaseA, 0]
                            state['b']['input'] = [phaseB]
                            state['c']['input'] = [phaseC]
                            state['d']['input'] = [phaseD]
                            state['e']['input'] = [phaseE]

                            while True:
                                a = intCode(state['a'])
                                state['b']['input'].append(a)
                                b = intCode(state['b'])
                                state['c']['input'].append(b)
                                c = intCode(state['c'])
                                state['d']['input'].append(c)
                                d = intCode(state['d'])
                                state['e']['input'].append(d)
                                e = intCode(state['e'])
                                if state['e'].get('halted'):
                                    output = max(output, state['a']['input'].pop(0))
                                    break
                                else:
                                    state['a']['input'].append(e)

        print(output)


if __name__ == '__main__':
    main()
