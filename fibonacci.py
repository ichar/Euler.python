# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '2.01'

isOdd = isEven = isLimit = False

## --------------------------------- ##

def get_next(num):
    p = [0, 1]
    i = 1
    while True:
        x = sum(p)
        if isLimit:
            if x > num:
                break
        elif i > num:
            break
        yield x
        p = [p[1], x]
        i += 1

def run(num, debug=0):
    r = 0
    for x in get_next(num):
        p = x%2
        if isOdd and p == 1 or isEven and p == 0:
            if debug:
                print('--> %s' % x)
            r += x

    return r


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 2. Sum of odd/even in the limited Fibonacci sequence of the number.')
        print('--> By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.')
        print('--> http://euler.jakumo.org/problems/view/2.html')
        print('--> ')
        print('--> Format: python fibonacci.py [-d] [-oe] [-l] <number>')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d: debug flag 0/1')
        print('-->   -o: sum of odd numbers')
        print('-->   -e: sum of even numbers')
        print('-->   -l: limited by the given number')
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
                if 'o' in x[1:]:
                    isOdd = True
                if 'e' in x[1:]:
                    isEven = True
                if 'l' in x[1:]:
                    isLimit = True
            else:
                num = x.isdigit() and int(x) or None

        assert num, "Number is not present!"
        
        started()

        print(run(num, debug))

        finished()
