import re

from collections import namedtuple


shop_category = re.compile(r'(\w+):')
item = re.compile(r'^([\w\s+]+?)(?!:)\s+(\d+)\s+(\d+)\s+(\d+)')

shop = {}

with open('shop') as f:
    for line in f:
        current_category_match = shop_category.search(line)
        if current_category_match:
            current_category = current_category_match.group(1)
            shop[current_category] = {}
            continue

        shop_item = item.search(line)
        if shop_item:
            name, cost, damage, armor = shop_item.groups()
            shop[current_category][name] = {
                'cost': int(cost),
                'damage': int(damage),
                'armor': int(armor),
            }

Boss = namedtuple('Boss', ('hp', 'damage', 'armor'))
            
with open('clue.txt') as f:
    stats = map(int, re.findall(r'\d+', f.read()))

boss = Boss(*stats)
