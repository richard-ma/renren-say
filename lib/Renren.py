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
        idPos = self.file.index("id : \"")
        self.uid=self.file[idPos+6:idPos+15]
        tokPos=self.file.index("requestToken : '")
        self.tok=self.file[tokPos+16:tokPos+27]
        rtkPos=self.file.index("_rtk : '")
        self.rtk=self.file[rtkPos+8:rtkPos+16]

        # get homepage and test login successfully or failed
        res = urllib2.urlopen("http://www.renren.com/home")
        html = res.read()
        uid = re.search("ruid:'(\d+)'",html)
        return uid

    def postmessage(self,content):
        post_path='http://shell.renren.com/'+self.uid+'/status';
        post_data=urllib.urlencode({
            'content':content,
            'privacyParams':"{'sourceControl': 99}",
            'requestToken':self.tok,
            '_rtk':self.rtk,
            'channel':'renren',
            });
        req=urllib2.Request(post_path,post_data);
        self.hax = urllib2.urlopen(req).read();

if __name__ == '__main__':
    testuser = Renren()
    print testuser.login('test-user', 'test-password')
    testuser.postmessage('renren-say testing.')
