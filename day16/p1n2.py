import re


TICKER_TAPE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

CERTAIN_ITEMS = {
    'cars': 2,
    'akitas': 0,
    'samoyeds': 2,
    'perfumes': 1,
    'children': 3,
    'vizslas': 0,
}

with open('clue.txt') as f:
    aunts_raw = f.read().splitlines()

p = re.compile(r'(\d+):\s((?:\w+:\s\d+(?:,\s)?)+)')
aunts = {}

for aunt in aunts_raw:
    aunt_id, stats = p.search(aunt).groups()
    items = re.findall(r'[a-z]+', stats)
    amounts = map(int, re.findall(r'\d+', stats))
    aunts[aunt_id] = dict(zip(items, amounts))

for aunt_id, stats in aunts.items():
    # if all items from aunt are identical
    # to corresponding items in ticker tape
    if len(stats.items() - TICKER_TAPE.items()) == 0:
        gifter = aunt_id

    # remove all certain items from aunt that
    # are identical  to corresponding items
    # in ticker tape, leaving only items
    # that describe a range
    range_items = stats.items() - CERTAIN_ITEMS.items()
    # make sure there's no certain items left
    # that weren't the same amount as the aunt's
    if not any(t[0] in CERTAIN_ITEMS.keys() for t in range_items):
        # if item exists, check it's within range
        # if not, make it True because it isn't relevant
        if 'goldfish' in stats:
            goldfish = stats['goldfish'] < TICKER_TAPE['goldfish']
        else:
            goldfish = True

        if 'pomeranians' in stats:
            pomeranians = stats['pomeranians'] < TICKER_TAPE['pomeranians']
        else:
            pomeranians = True

        if 'trees' in stats:
            trees = stats['trees'] > TICKER_TAPE['trees']
        else:
            trees = True

        if 'cats' in stats:
            cats = stats['cats'] > TICKER_TAPE['cats']
        else:
            cats = True

        if all((goldfish, pomeranians, trees, cats)):
            actual_gifter = aunt_id

print('Part 1:', gifter)
print('Part 2:', actual_gifter)
