import hashlib


key = 'yzbqklnj'
n = 1
part1 = None

while True:
    md5hash = hashlib.md5(f'{key}{n}'.encode()).hexdigest()
    
    if part1 is None and md5hash[:5] == '0'*5:
        part1 = n

    if md5hash[:6] == '0'*6:
        part2 = n
        break
    
    n += 1

print('Part 1:', part1)
print('Part 2:', part2)
