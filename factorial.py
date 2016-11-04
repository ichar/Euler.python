# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.0'

## --------------------------------- ##

def run(num, debug=0):
    r = 1
    for x in range(1, num+1):
        r *= x

    if debug:
        print('--> %s' % r)

    return r


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 20. Sum of digits in factorial of the number.')
        print('--> http://euler.jakumo.org/problems/view/20.html')
        print('--> ')
        print('--> Format: python factorial.py [d] <number>')
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
                debug = x[1:] == 'd' and 1 or 0
            else:
                num = x.isdigit() and int(x) or None

        assert num, "Number is not present!"
        
        started()

        r = run(num, debug)

        finished('Factorial')
        start = datetime.now()
    
        #print(sum([int(x) for x in str(r)]))
        print(sum([int(chr(x)) for x in bytes(str(r), 'cp1251')]))

        finished()