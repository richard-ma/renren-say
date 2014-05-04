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
        say_factory = SayFactory()
        sayer = say_factory.create(self.config.get('runtime', 'mode'))
        content = '[' + sayer.__class__.__name__ + ']' + sayer.say()
        user = Renren()
        user.login(
                self.config.get('renren', 'email'),
                self.config.get('renren', 'password'))
        if self.config.getboolean('runtime', 'debug') == False:
            user.postmessage(content)
        return content

if __name__ == "__main__":
    renren_say = RenrenSay()
    print renren_say.start()
