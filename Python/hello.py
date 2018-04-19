#!/usr/bin/env python
# -*- coding: utf-8 -*-
#name = input('please input your name  ')
#s = 'hello+ {0},{1}' .format('x','y')
#y = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
#print (s)
#classmates = ['lihuan','huangsan','zhangsi']
##print classmates
#for x in classmates:
#    print x

#L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
#     ]
#for x in L:
#    for y in x:
#        print y

#age = input('please input age: ')
#birth = int(age)
#if birth > 18:
#   print 'adult'
#else:
#   print  'child'


#sum = 0
#for i in range(100):
#    sum += i
#print sum

#def fact(n):
#    if n == 1 :
#       return 1
#    return n *fact(n - 1)
#print fact(5)


#list = ['li','zhang','wang','ma']
##op = []
##n = len(list)
##for x in range(n):
##    op.append(list[x])
##print op
##print list[0:3]
##print list[-1:3]
##print list[0:len(list)]
#print list[-len(list):0]
#dic = {'key1':'hello','key2':'wang'}
##for x in dic:
##    print dic[x]
#
#for vallue in dic.itervalues() :
#    print vallue
#
#for x,y in [(1,3),(2,4)]:
#    print x , y
#list = []
#for i in range(11):
#    if i % 2  == 0:
#       list.append(i * i)
#    else :
#        print ('hello.py %d!',i)
#
#print list
#x = 'abc'
#y = 123
#z = 123.00
#print isinstance(x,str)
#print isinstance(y,int)
#print isinstance(z,float)

#L = [x *x for x in range(10)]
#print L
#g = (x * x for x in range(10))
#for n in g:
#    if n == 4:
#       print n
#def add(x):
#    return x+x
#list = range(1,10)
#print map(add,list)

#def add(x, y):
#    return x+y
#list = range(1,4)
##print reduce(add,list)
#print sum(list)
#def is_odd(n):
#    if n % 2 == 1:
#       return True
#
#print filter(is_odd,[1,2,3,4,5,6])

#def reversed_cmp(x,y):
#    if x < y :
#       return 1
#    if x > y :
#        return  -1;
#    return 0
#print sorted([1,2,3,4,2,0],reversed_cmp)
#def lazy_sum(*args):
#    def sum():
#        ax = 0
#        for n in args:
#            ax += n
#        return ax
#    return sum
#f1 = lazy_sum(1,2,3)
#f2 = lazy_sum(1,2,3)
#print f1,f2

#print list(map(lambda x:x*x,[1,2,3,4]))
#print(filter(lambda x: x %2 == 1,range(1,20)))
' a test module '

__author__ = 'Michael Liao'
import sys
import add

def testAdd(x,y):
    return add.add_cms(x,y)

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
   print test()

