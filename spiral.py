# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.0'

debug = 0
deepdebug = 0

LIMIT = 4

## --------------------------------- ##

def run(num):
    # num - размерность спирали (3*3,5*5,7*7,9*9,11*11, ... 1001*1001 -> num*num), N(odd)
    # LIMIT – кол-во чисел в спирали (Const) = 4
    # R – номер витка = радиус (N): 1,2,3 …
    # n – номер числа в витке спирали 
    # p - кол-во отобранных чисел в витке
    # i - числовая последовательность i,i+1, ...
    res, total, value = [1], 1, 1
    R = 1
    n, p, i = 0, 0, 1
    while True:
        if p == LIMIT:
            R += 1
            n, p = 0, 0
    
        if R > int(num/2):
            break

        i += 1
        n += 1

        if debug:
            print('--> %s R:%s (%s:%s)' % (i,R,n,p))

        if n == 2*R:
            total += 1
            value += i

            if deepdebug:
                res.append(i)
                print('>>> R:%s %s)' % (R,res))

            n, p = 0, p+1

    return res, total, value


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 28. Number spiral diagonals.')
        print('--> What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?')
        print('--> http://euler.jakumo.org/problems/view/28.html')
        print('--> ')
        print('--> Format: python pythagorean.py [-dD] <number>')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d    : debug flag 0/1')
        print('-->   -D    : deepdebug flag 0/1 (prints sequence on the screen)')
        print('--> ')
        print('--> Warning! Be carefull with -D.')
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
            else:
                num = x.isdigit() and int(x) or None

        assert num, "Number is not present!"
        
        started()

        r = run(num)
        if deepdebug:
            print(r[0])
        print('Total selected items in the spiral:%s' % r[1], r and 'Sum:%s' % r[2])

        finished()
