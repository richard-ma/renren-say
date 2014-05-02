#!/usr/bin/env python
#-- coding:utf-8 --

import os
import glob
from new import classobj
from random import choice

import sys
sys.path.append('./plugins')

from Say import Say

class SayFactory():
    def __init__(self):
        self.modules = {}

        # Get all plugins
        for module_file in glob.glob(r'./plugins/*Plugin.py'):
            module_name, module_ext = os.path.splitext(os.path.basename(module_file))
            module = __import__(module_name)
            self.modules[module_name] = module

    def create(self, name):
        if name == 'random':
            name = choice(self.modules.keys())
        else:
            name = name + 'Plugin'

        if name in self.modules.keys():
            c = getattr(self.modules[name], name)
            return c()
        else:
            return None

if __name__ == '__main__':
    say = SayFactory()
    print say.create('Yuebao').say()
    print say.create('random').say()
