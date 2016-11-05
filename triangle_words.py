# -*- coding: utf-8 -*-

import sys
import math
from lib.utils import *

version = '1.0'

debug = 0
deepdebug = 0

ABC_LEN = 96
COMMAS = '"'

## --------------------------------- ##

def valid(num):
    return num and num > 0 and int(num) == num and True or False

def D(a,b,c):
    return b*b - 4*a*c

def exists(num):
    # Корни квадратного уравнения: A*x*x + B*x + C = 0, где
    #   A = 1
    #   B = 1
    #   C = -2*<код числа>
    # Расчет значения D (дескриминанта) и значений корней. 
    # Должен существовать хотя бы один натуральный корень: x > 0, x in (N)
    #
    a, b, c = 1, 1, -2*num
    d = D(a,b,c)
    
    if deepdebug:
        print('>>> D [%s]: %s' % (num, d))

    if d > 0:
        q = math.sqrt(d)
        x1 = (-b + q)/2*a
        x2 = (-b - q)/2*a
    elif d == 0:
        x1 = x2 = (-b + q)/2*a
    else:
        x1 = x2 = None
    
    v = (valid(x1) or valid(x2)) and True or False
    
    if deepdebug:
        print('>>> x1[%s], x2[%s], valid: %s' % (x1, x2, v))

    return v

def is_triangle(word):
    w = word.strip()
    if word.startswith(COMMAS) and word.endswith(COMMAS):
        w = word[1:-1]
    code = sum(ord(s) - ABC_LEN for s in w.lower())
    if deepdebug:
        print('>>> Word [%s]: %s' % (w, code))
    return exists(code)

def calculate(words):
    res = []
    for w in words:
        if is_triangle(w):
            res.append(w)
    return res

def go(line, i=1):
    words = line.split(',')

    if debug:
        print('>>> Words count in line [%s]: %s' % (i, len(words)))

    res = calculate(words)

    if debug:
        for x in res:
            print('--> %s' % x)
    if debug:
        print('>>> Triangle words: %s' % len(res))

    return res

def run1(source):
    # Run for given file: source
    # --------------------------
    total = 0
    i = 0
    with open(source, 'rb') as fin:
        for line in fin:
            i += 1
            total += len(go(str(line), i))

    return total

def run2(line):
    # Check simple words only splitted by ',': line
    # ---------------------------------------------
    return len(go(line))


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 9. Coded triangle numbers.')
        print('--> How many are triangle words in the given file?')
        print('--> http://euler.jakumo.org/problems/view/42.html')
        print('--> ')
        print('--> Format: python pythagorean.py [-dD] <source> [<mode>]')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d     : debug flag 0/1')
        print('-->   -D     : deepdebug flag 0/1')
        print('--> ')
        print('--> Arguments:')
        print('--> ')
        print('-->   source : "word.txt" file path')
        print('-->   mode   : number of run-function (method): 1|2, default: 1')
        print('--> ')
        print('--> v%s[Python3]' % version)
        
    else:
        source = None
        mode = 1

        print(sys.version)
        
        for x in argv[1:]:
            if x.startswith('-'):
                if 'd' in x[1:]:
                    debug = 1
                if 'D' in x[1:]:
                    deepdebug = 1
                if 'all' in x[1:]:
                    all = True
            elif not source:
                source = not x.isdigit() and x or None
            else:
                mode = x.isdigit() and int(x)

        assert source, "Source file path is not present!"
        
        started()

        run = mode == 2 and run2 or run1

        print('Total:%s' % run(source))

        finished()
