import string
import re


class Password:
    def __init__(self, pwd):
        self.pwd = list(pwd)

    @property
    def pwd_string(self):
        return ''.join(self.pwd)
        
    def good_password(self):
        if any(c in self.pwd for c in 'iol'):
            return False
        
        # potential increasing straights
        straights = [''.join(self.pwd[i:i+3]) for i in range(len(self.pwd)-2)]
        if not any(straight in string.ascii_lowercase for straight in straights):
            return False

        # has at least two unique pairs
        pair1_match = re.search(r'(.)\1', self.pwd_string)
        pair1 = pair1_match.group(1) if pair1_match else None
        pair2_match = re.search(rf'([^{pair1}])\1', self.pwd_string)
        if pair1_match is None or pair2_match is None:
            return False

        return True

    def cycle(self):
        for i, c in enumerate(reversed(self.pwd),1):
            if c == 'z':
                self.pwd[-i] = 'a'
            else:
                self.pwd[-i] = chr(ord(c)+1)
                break


password = Password('hxbxwxba')

while not password.good_password():
    password.cycle()

print('Part 1:', password.pwd_string)

# cycle once to not look at
# prevous password again
password.cycle()

while not password.good_password():
    password.cycle()

print('Part 2:', password.pwd_string)
