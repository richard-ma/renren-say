#!/usr/bin/env python
#-- coding:utf-8 --

import sys

import ConfigParser

from lib.Renren import Renren
from SayFactory import SayFactory

class RenrenSay():
    def __init__(self):
        # config file
        config_file = "config.ini"

        # load configration
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_file)

    def start(self):
        sayer = SayFactory()
        content = sayer.create('Simple').say()
        print content
        user = Renren()
        user.login(
                self.config.get('renren', 'email'),
                self.config.get('renren', 'password'))
        user.postmessage(content)

if __name__ == "__main__":
    renren_say = RenrenSay()
    renren_say.start()
