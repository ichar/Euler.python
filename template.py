# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.0'

debug = 0
deepdebug = 0

## --------------------------------- ##

def get_next(num):
    pass

def run(num):
    i = 0
    for h, k in get_next(num):
        pass

        i += 1

    if debug or deepdebug:
        print('>>> Not found, i=%s, (%s,%s)' % (i,h,k))


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 9. Special Pythagorean triplet.')
        print('--> There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.')
        print('--> http://euler.jakumo.org/problems/view/9.html')
        print('--> ')
        print('--> Format: python pythagorean.py [-d] [-all] <number> [<mode>]')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d    : debug flag 0/1')
        print('-->   -D    : deepdebug flag 0/1')
        print('-->   -all  : find all feasible solutions')
        print('-->   -mode : number of run-function (method): 1|2|3, default: 3')
        print('--> ')
        print('--> v%s[Python3]' % version)
        
    else:
        num = None

        print(sys.version)
        
        for x in argv[1:]:
            if x.startswith('-'):
                if 'd' in x[1:]:
                    debug = 1
                if 'D' in x[1:]:
                    deepdebug = 1
                if 'all' in x[1:]:
                    all = True
            else:
                num = x.isdigit() and int(x) or None

        assert num, "Number is not present!"
        
        started()

        r = run(num)
        print(r, r and not all and r[0]*r[1]*r[2] or '...', all and 'Total:%s' % len(r))

        finished()
