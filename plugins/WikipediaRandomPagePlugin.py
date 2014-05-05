#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say

import urllib2
import re

class WikipediaRandomPagePlugin(Say):

    def __init__(self):
        url = "http://zh.wikipedia.org/wiki/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2"
        req = urllib2.Request(url)
        u = urllib2.urlopen(req)
        html = u.read()
        title = re.findall(r"<title>(.+?) -", html)
        title = title[0]

        self.title = title
        self.url = u.geturl()

    def say(self):
        return "随机条目：%s 链接：%s" % (self.title, self.url)

if __name__ == "__main__":
# should return true
    test = WikipediaRandomPagePlugin()
    print test.say()
