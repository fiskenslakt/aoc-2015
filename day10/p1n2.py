def look_and_say(seq):
    stack = []

    for n in seq:
        if stack and n == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([n, 1])

    return ''.join(f'{t[1]}{t[0]}' for t in stack)


sequence = '3113322113'

for _ in range(40):
    sequence = look_and_say(sequence)

print('Part 1:', len(sequence))

for _ in range(10):
    sequence = look_and_say(sequence)
    
print('Part 2:', len(sequence))
