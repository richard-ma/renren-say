#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import cookielib
import re

class Renren():

    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:16.0) Gecko/20100101 Firefox/16.0'}

    def __init__(self):
        # set cookie
        cj = cookielib.CookieJar()
        # set opener
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

    def login(self, username, password):
        # make login url
        logpage = "http://www.renren.com/Login.do"
        data = {'email':username,'password':password}
        login_data = urllib.urlencode(data)
        res = urllib2.Request(logpage,login_data)
        self.file=urllib2.urlopen(res).read()

        # get uid, tok and rtk
        idPos = self.file.index("'id':'")
        self.uid=self.file[idPos+6:idPos+15]
        tokPos=self.file.index("get_check:'")
        self.tok=self.file[tokPos+11:tokPos+21]
        rtkPos=self.file.index("get_check_x:'")
        self.rtk=self.file[rtkPos+13:rtkPos+21]

        # get homepage and test login successfully or failed
        res = urllib2.urlopen("http://www.renren.com/home")
        html = res.read()
        uid = re.search("'ruid':'(\d+)'",html).group(1)
        return uid

    def postmessage(self,content):
        # make post data
        url = "http://shell.renren.com/"+self.uid+"/status"
        postdata = {'content':content,
                    'hostid':self.uid,
                    'requetToken':self.tok,
                    '_rtk':self.rtk,
                    'channel':'renren',
                   }
        log_data = urllib.urlencode(postdata)
        req2 = urllib2.Request(url,log_data)

        # send data
        self.hax = urllib2.urlopen(req2).read()

if __name__ == '__main__':
    testuser = Renren()
    print testuser.login('test-user', 'test-password')
    testuser.postmessage('renren-say testing.')
