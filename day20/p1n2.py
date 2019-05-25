def get_presents(n, multiplier=10):
    factors = set()

    if multiplier == 10:
        for i in range(1, int(n**.5)+1):
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
    else:
        for i in range(1, int(n**.5)+1):
            if n % i == 0:
                if n // i <= HOUSES:
                    factors.add(i)
                if i <= HOUSES:
                    factors.add(n//i)

    return sum(factors)*multiplier


PRESENTS = 33_100_000
HOUSES = 50

house = 1

while get_presents(house) < PRESENTS:
    house += 1

print('Part 1:', house)

house = 1

while get_presents(house, 11) < PRESENTS:
    house += 1

print('Part 2:', house)
