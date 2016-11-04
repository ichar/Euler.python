# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.0'

## --------------------------------- ##

def palindrom(x):
    x1 = str(x)
    x2 = ''.join(str(x1[i]) for i in range(len(x1)-1,-1,-1))
    return x1 == x2 and True or False

def get_next(num):
    p = num-1
    z = p and str.zfill('0', p) or ''
    min = int('1%s' % z)
    max = int('1%s0' % z)
    x1 = max
    while True:
        x1 = x1 - 1
        if x1 < min:
            break
        x2 = x1
        while True:
            x2 = x2 - 1
            if x2 < min:
                break
            yield (x1, x2)

def run(num, debug=0):
    for x1, x2 in get_next(num):
        x = x1 * x2
        if debug:
            print('--> %s*%s=%s' % (x1, x2, x))
        if palindrom(x):
            return x, x1, x2

    return 0


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 4. Find the largest palindrome made from the product of two n-digit numbers.')
        print('--> http://euler.jakumo.org/problems/view/4.html')
        print('--> ')
        print('--> Format: python palindrome.py [-d] <n>')
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

        print(run(num, debug))

        finished()
