import re

from collections import defaultdict


p = re.compile(r'(\w+)\s=>\s(\w+)')

with open('clue.txt') as f:
    replacements = defaultdict(list)
    for line in f:
        if '=>' in line:
            match = p.search(line)
            replacements[match.group(1)].append(match.group(2))
        else:
            break
    # after replacements, only non blank line
    # left will be the molecule itself
    for line in f:
        if line.strip():
            molecule = line.strip()


distinct_molecules = set()

for k, v in replacements.items():
    for r in v:
        i = 0
        indices = []
        # for every replacement get
        # all indices where it occurs
        while molecule.find(k, i) != -1:
            indices.append(molecule.find(k, i))
            i = indices[-1] + 1

        # make replacement in each
        # index found earlier and
        # add it to the set
        for index in indices:
            new_molecule = molecule[:index] + r + molecule[index+len(k):]
            distinct_molecules.add(new_molecule)

print('Part 1:', len(distinct_molecules))

# reverse replacement dictionary so
# we can work backwards
replacements = {r:k for k, v in replacements.items() for r in v}
medicine = molecule
steps = 0

# stop once the medicine molecule
# becomes a single electron "e"
while medicine != 'e':
    # start working backwards from the longest
    # possible replacements
    # then pray
    for k, v in sorted(replacements.items(), key=lambda t: len(t[0]), reverse=True):
        if k in medicine:
            medicine = medicine.replace(k, v, 1)
            steps += 1
            break

print('Part 2:', steps)
