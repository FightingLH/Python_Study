#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Animals(object):
    def __init__(self,name = 'wang san'):
        self.name = name
    
    def run(self):
        print ('%s is runing...'%(self.name))

class Dog(Animals):
      pass

class Cat(Animals):
      pass

dog = Dog('lili')
dog.run()
