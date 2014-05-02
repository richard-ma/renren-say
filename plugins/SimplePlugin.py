#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say

class SimplePlugin(Say):

    def __init__(self):
        pass

    def say(self):
        return '[Sending by Renren-say] Fork me: https://github.com/richard-ma/renren-say'

if __name__ == "__main__":
    test = SimplePlugin()
    print test.say()
