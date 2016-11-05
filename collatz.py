# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.01'

## --------------------------------- ##

def odd(x):
    return x%2 == 1 and True or False

def even(x):
    return x%2 == 0 and True or False

def put_next(num):
    x = num
    while x > 1:
        x = even(x) and int(x/2) or 3*x + 1
        yield x

def get_next(num):
    for x in range(num, 0, -1):
        yield x

def run(num, debug=0):
    res = []
    for a in get_next(num):
        #r = [x for x in put_next(a)]
        r = list(put_next(a))
        r.insert(0, a)
        if debug:
            print('--> %s:%s len:%s' % (a, r, len(r)))
        if len(r) > len(res):
            res = r

    return res


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 14. Longest Collatz sequence.')
        print('--> Which starting number, under one million, produces the longest chain?')
        print('--> https://projecteuler.net/problem=14')
        print('--> ')
        print('--> Format: python collatz.py [-d] <number>')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d: debug flag 0/1')
        print('--> ')
        print('--> v%s[Python3]' % version)
        
    else:
        debug = 0
        num = None

        print(sys.version)
        
        for x in argv[1:]:
            if x.startswith('-'):
                if 'd' in x[1:]:
                    debug = 1
            else:
                num = x.isdigit() and int(x) or None

        assert num, "Number is not present!"

        started()

        r = run(num, debug)
        print(' -> '.join([str(x) for x in r]))
        """
        for x in r:
            print(x)
        """
        print('len:', len(r))

        finished()
