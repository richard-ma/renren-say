#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say
from random import randint

class PiPlugin(Say):

    def __init__(self):
        self.times = randint(100000, 200000)
        self.r = 10000

    def pi(self, r):
        cnt = 0

        for i in range(0, self.times):
            x = randint(0, r)
            y = randint(0, r)

            if x ** 2 + y ** 2 <= r ** 2:
                cnt = cnt + 1

        return [str(cnt * 4 / float(self.times)), str(cnt)]

    def say(self):
        pi, cnt = self.pi(self.r)
        return "本次测试了%d次，命中%s次，PI为%s" % (self.times, cnt, pi)

if __name__ == "__main__":
    test = PiPlugin()
    print test.say()
