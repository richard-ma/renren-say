#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say
from random import choice

class MorseAlphabetPlugin(Say):

    def __init__(self):
        self.p = {'0': '.', '1': '-'}

        self.d = {
                'A': '01', 'B': '1000', 'C': '1010',
                'D': '100', 'E': '0', 'F': '0010',
                'G': '110', 'H': '0000', 'I': '00',
                'J': '0111', 'K': '101', 'L': '0100',
                'M': '11', 'N': '10', 'O': '111',
                'P': '0110', 'Q': '1101', 'R': '010',
                'S': '000', 'T': '1', 'U': '001',
                'V': '0001', 'W': '011', 'X': '1001',
                'Y': '1011', 'Z': '1100',
                }

        self.word = choice([
            'superbia', 'invidia', 'ira', 'acedia',
            'avaritia', 'gula', 'luxuria'])

    def encode(self, s):
        s = s.upper()
        ret = ''
        for c in s:
            ret = ret + self.renderChar(self.d[c]) + ' '
        return ret

    def renderChar(self, code):
        ret = ''
        for c in code:
            ret = ret + self.p[c]
        return ret

    def say(self):
        return self.encode(self.word)

if __name__ == "__main__":
    test = MorseAlphabetPlugin()
    print test.word
    print test.say()
