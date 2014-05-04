#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say
from math import sqrt
from random import randint

class PrimePlugin(Say):

    def __init__(self):
        self.s = 1
        self.e = 100000
        self.number = randint(self.s, self.e)

    def prime(self, n):
        isPrime = True
        for i in range(2, n):
            if n % i == 0:
                isPrime = False
                break
        return isPrime

    def say(self):
        ret = '%d是一个' % (self.number)
        if self.prime(self.number):
            ret = ret + '质数'
        else:
            ret = ret + '合数'
        return ret

if __name__ == "__main__":
    test = PrimePlugin()
    print test.say()
