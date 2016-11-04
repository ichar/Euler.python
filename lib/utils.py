# -*- coding: utf-8 -*-

import time
from datetime import datetime
import decimal

TIME_MASK = '%H:%M:%S %f'

start = None

def started():
    global start
    start = datetime.now()
    print('>>> Started at %s' % start)

def finished(point='Finished'):
    finish = datetime.now()
    t = finish - start
    print('>>> %s at %s' % (point, finish))
    print('>>> Spent time: %s msec (%s sec)' % ( \
            t.seconds*1000000+t.microseconds,
            decimal.Decimal(str((t.seconds*1000000+t.microseconds)/1000000.0))
    ))
