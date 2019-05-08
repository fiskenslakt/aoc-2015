with open('clue.txt') as f:
    strings = f.read().splitlines()

literals_raw = 0
literals = 0
in_memory = 0

for string in strings:
    # literal length plus a backslash to
    # escape each double quote, and a backslash
    # to escape each backslash, plus 2 to represent
    # the imaginary outermost double quotes to contain it
    raw = len(string)
    raw += string.count('"')
    raw += string.count('\\')
    raw += 2
    literals_raw += raw

    literals += len(string)
    # removes just outermost double quotes
    # from string, as strip('"') will remove too much
    literal = string[1:-1]

    escaped = bytes(literal.encode()).decode('unicode_escape')
    in_memory += len(escaped)

print('Part 1:', literals - in_memory)
print('Part 2:', literals_raw - literals)
