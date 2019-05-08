import re


def contains_3_vowels(s):
    vowel_count = sum(c in 'aeiou' for c in s)
    return vowel_count >= 3


def has_double_letter(s):
    return re.search(r'(\w)\1', s)

        
def no_bad_string(s):
    bad_strings = ('ab','cd','pq','xy')
    return not any(bs in s for bs in bad_strings)


def pair_appears_twice(s):
    # pair can't overlap
    return re.search(r'(\w{2}).*\1', s)


def has_letter_sandwich(s):
    return re.search(r'(\w).\1', s)


def nice_string_part1(s):
    if not contains_3_vowels(s):
        return False

    if not has_double_letter(s):
        return False

    if not no_bad_string(s):
        return False

    return True

def nice_string_part2(s):
    if not pair_appears_twice(s):
        return False

    if not has_letter_sandwich(s):
        return False

    return True


with open('clue.txt') as f:
    strings = f.read().splitlines()

print('Part 1:', sum(nice_string_part1(s) for s in strings))
print('Part 2:', sum(nice_string_part2(s) for s in strings))
