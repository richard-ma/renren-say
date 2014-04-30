#!/usr/bin/env python
#-- coding:utf-8 --

import os
import glob

class SayFactory():
    def __init__(self):
        self.modules = []
        for module_file in glob.glob("./plugins/*-plugin.py"):
            module_name = os.path.splitext(os.path.basename(module_file))[0]
            module = __import__(module_name)
            print module

    def pick(self):
        pass

if __name__ == '__main__':
    say = SayFactory()
