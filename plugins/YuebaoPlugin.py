#!/usr/bin/env python
#-- coding:utf-8 --

from Say import Say

import urllib2
import re

class YuebaoPlugin(Say):

    def __init__(self):
        url = "https://financeprod.alipay.com/fund/index.htm"
        req = urllib2.Request(url)
        html = urllib2.urlopen(req).read()
        shouyilv = re.findall(r"nianhuashouyilv\">(.+?)<", html)
        if shouyilv == []:
            self.shouyilv = False
        else:
            self.shouyilv = shouyilv[1]

    def say(self):
        if self.shouyilv == False:
            return '余额宝收益获取出错了喵'
        else:
            return '今日余额宝七天年化收益率为: ' + self.shouyilv + '%'

if __name__ == "__main__":
# should return true
    test = YuebaoPlugin()
    print test.say()
# should error
    test.shouyilv = False
    print test.say()
