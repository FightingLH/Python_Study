#!/usr/bin/env python
# -*- coding: utf-8 -*-
#JAN = 1
#FEB = 2
#MAR = 3
#...
#DEC = 12
import Enum
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print Month.Jan
