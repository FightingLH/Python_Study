#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
        
    def print_score(s):
        print('%s: %s' % (s.name,s.score))

    def get_grade(self):
        if self.score >= 90:
           return 'A'
        elif self.score >= 60:
           return 'B'
        else:
           return 'C'

bart = Student('lihuan',100)
bart.print_score()
print bart.get_grade()
