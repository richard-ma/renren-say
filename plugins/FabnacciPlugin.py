#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say
from random import randint

class FabnacciPlugin(Say):

    def __init__(self):
        self.start = randint(1, 100)
        self.length = randint(3, 6)

    def fabnacci(self, start, length):
        l = []

        if 1 in range(start, start+length):
            l.append(1)
        if 2 in range(start, start+length):
            l.append(1)

        a = 1
        b = 1
        idx = 3
        while len(l) < length:
            c = a + b
            a = b
            b = c
            if idx in range(start, start + length):
                l.append(c)
            idx = idx + 1

        return l

    def say(self):
        ret = 'Fabnacci[%d] ~ Fabnacci[%d] are ' % (self.start, self.start + self.length - 1)
        for item in self.fabnacci(self.start, self.length):
            ret = ret + ('%d ' % (item))

        return ret

if __name__ == "__main__":
    test = FabnacciPlugin()
    text = test.say()
    print text
    print len(text)
