import re

from functools import lru_cache


def bitwise_op(wire_a, gate, wire_b):
    """Returns an integer from the result
    of one of the 5 valid bitwise operations.
    """
    if gate == 'AND':
        return wire_a & wire_b
    elif gate == 'OR':
        return wire_a | wire_b
    elif gate == 'LSHIFT':
        return wire_a << wire_b
    elif gate == 'RSHIFT':
        return wire_a >> wire_b
    elif gate == 'NOT':
        return ~wire_b

@lru_cache(maxsize=None)
def execute_circuit(wire):
    """Returns signal of wire as an integer.
    If signal is unknown, recurse deeper
    into the circuit to find it.
    """
    signal = circuit[wire]
    wire_a, gate, wire_b, wire_c = signal.groups()

    # if no gate, wire_c is being set to either
    # a wire or some arbitrary signal
    if gate is None:
        # return signal
        if wire_b.isdigit():
            return int(wire_b)
        # recurse to find signal
        else:
            return execute_circuit(wire_b)

    # if no wire_a, gate is NOT
    # so wire_c is set to
    # compliment of wire_b
    elif wire_a is None:
        if not wire_b.isdigit():
            wire_b = execute_circuit(wire_b)
        return bitwise_op(None, gate, wire_b)   # gate should be NOT

    # if wire_a exists, then perform bitwise
    # operation on both wires to get signal
    # if either wire is unknown, recurse
    # to find its signal
    else:
        if not wire_a.isdigit():
            wire_a = execute_circuit(wire_a)
        if not wire_b.isdigit():
            wire_b = execute_circuit(wire_b)

        return bitwise_op(int(wire_a), gate, int(wire_b))


# parses instruction such that regardless
# of the instruction format:
# wire 'a' will always be group 1
# gate will always be group 2
# wire 'b' will always be group 3
# wire 'c' will always be group 4
p = re.compile(r'(?:([a-z]{1,2}|\d+)?\s)?(NOT|OR|AND|[LR]SHIFT)?\s?([a-z]{1,2}|\d+)\s->\s([a-z]{1,2})')

with open('clue.txt') as f:
    instructions = f.read().splitlines()

circuit = {}

# build circuit by mapping
# each wire to its signal
for instruction in instructions:
    match = p.search(instruction)
    circuit[match.group(4)] = match

# find what signal is ultimately
# provided to wire 'a'
signal = execute_circuit('a')
print('Part 1:', signal)

# override wire 'b' to wire 'a' signal
# and clear cache so wire 'b' doesn't
# return its old signal
execute_circuit.cache_clear()
match = p.search(f'{signal} -> b')
circuit[match.group(4)] = match

signal = execute_circuit('a')
print('Part 2:', signal)
