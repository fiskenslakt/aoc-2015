import json
import re


def get_non_reds(data):
    if isinstance(data, dict):
        if 'red' in data.values():
            return 0
        yield from get_non_reds(list(data.values()))
    elif isinstance(data, list):
        for el in data:
            if isinstance(el, int):
                yield el
            elif isinstance(el, (dict, list)):
                yield from get_non_reds(el)


# use regex to simply find all numbers
# and get their sum
with open('clue.txt') as f:
    document = [int(n) for n in re.findall(r'-?\d+', f.read())]

print('Part 1:', sum(document))

# use recursion to identify any and all
# objects containing the value 'red'
# and ignore all its numbers, including
# all of its children.
# yield all the other numbers
# and get their sum
with open('clue.txt') as f:
    document = json.load(f)

print('Part 2:', sum(get_non_reds(document)))
