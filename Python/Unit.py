#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
class Student():
    def __init__(self,score,name):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 90:
           return 'A'
        else:
           return 'C'

class TestStudent(unittest.TestCase):
    def test_90_to100(self):
        s1 = Student('lihuan',100)
        s2 = Student('Lisa', 50)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'B')


    def test_60_to90(self):
        s1 = Student('lisan',60)
        s2 = Student('zhangsa', 50)
        self.assertEqual(s1.get_grade(),'C')
        self.assertEqual(s2.get_grade(),'B')

class  OpenFile():
    
    def __init__(self,path,content):
        self.path = path
        self.content = content
    
    def openWithFilePath(self):
        f = open(self.path,'rb')
        print (f.read())
        
    def writeWithFilePath(self):
        w = open(self.path,'w')
        w.write(self.content)
        w.close()
import json

class  ModelTest():
    def __init__(self, name, age, score):
        self.name = name
        self.age  = age
        self.score = score
    def dict(self):
        return {'name':self.name,'age':self.age,'score':self.score}
d = ModelTest('lihuan',28,100)
a = d.dict()
print json.dumps(a)

#if __name__ == '__main__':
#   unittest.main()
#f = OpenFile('/Users/feeyo/Desktop/iOS知识点整理.php','测试内容')
#f.openWithFilePath()
#f.writeWithFilePath()
#f.openWithFilePath()


