#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
   print 'try.....'
   r = 10/2

except ZeroDivisionError as e:
    print ('except:',e)
finally:
    print ('finally...')
print ('END')

