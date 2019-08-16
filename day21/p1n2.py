import re

from collections import deque, namedtuple


class Equip:
    def __init__(self, weapon, armor=None, rings=None):
        self.weapon = weapon
        self.armor = armor
        self.rings = rings
        self.cost = shop['Weapons'][weapon]['cost']

        if armor is not None:
            self.armor_score = shop['Armor'][armor]['armor']
            self.cost += shop['Armor'][armor]['cost']
        else:
            self.armor_score = 0
            
        self.damage_score = shop['Weapons'][weapon]['damage']

        if rings is not None:
            for ring in rings:
                self.damage_score += shop['Rings'][ring]['damage']
                self.armor_score += shop['Rings'][ring]['armor']
                self.cost += shop['Rings'][ring]['cost']

    def __repr__(self):
        return f'Equip({self.weapon}, {self.armor}, {self.rings})'

    @staticmethod
    def battle_sim(player, boss):
        """Return True if player defeats
        boss with given stats.
        """
        boss_hp = boss.hp
        player_hp = player.hp
        
        player_attack = player.damage - boss.armor
        if player_attack < 1:
            player_attack = 1

        boss_attack = boss.damage - player.armor
        if boss_attack < 1:
            boss_attack = 1
            
        while player_hp >= 0:
            boss_hp -= player_attack
            if boss_hp <= 0:
                break
            player_hp -= boss_attack

        return player_hp > 0


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

Player = namedtuple('Player', ('hp', 'damage', 'armor'))
            
with open('clue.txt') as f:
    boss_stats = map(int, re.findall(r'\d+', f.read()))

boss = Player(*boss_stats)

winning_costs = []
losing_costs = []

queue = deque()
for weapon, stats in shop['Weapons'].items():
    queue.append(Equip(weapon))

while queue:
    equip = queue.popleft()
    player = Player(100, equip.damage_score, equip.armor_score)

    if equip.battle_sim(player, boss):
        winning_costs.append(equip.cost)
    else:
        losing_costs.append(equip.cost)

    if equip.armor is None:
        for armor in shop['Armor']:
            queue.append(Equip(equip.weapon, armor, equip.rings))

    if equip.rings is None:
        for ring in shop['Rings']:
            queue.append(Equip(equip.weapon, equip.armor, {ring}))
            
    elif len(equip.rings) < 2:
        for ring in shop['Rings']:
            if ring not in equip.rings:
                queue.append(Equip(equip.weapon, equip.armor, equip.rings | {ring}))

print('Part 1:', min(winning_costs))
print('Part 2:', max(losing_costs))
