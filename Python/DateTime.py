#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
#获取当前datetime
now = datetime.now()
print (now)
#获取指定日期和时间
dt = datetime(2015,4,19,12,20)
print (dt)
#datetime 转换timestamp
dt.timestamp()
