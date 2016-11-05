# -*- coding: utf-8 -*-

import sys
from lib.utils import *
from functools import reduce

version = '1.0'

debug = 0
deepdebug = 0

## --------------------------------- ##

def run(source):
    # Номера цифр для отбора могут быть заданы в любой последовательности без сортировки.
    # Результирующий список соблюдает заданную последовательность, например:
    #
    #   > python champernown.py 1 32 16 180 76 10 1029
    #
    # Результат:
    #
    #   [1, 2, 1, 9, 4, 1, 7] 504
    #
    digits = sorted(source)
    length = 0
    res = {}
    s = ''
    p = None
    i = 1
    while True:
        while not p and digits:
            p = int(digits.pop(0))

        if not (p or digits):
            break

        n = str(i)
        l = len(n)
        s += n
        length += l

        if debug or deepdebug:
            print('>>> %s[%s]:%s %s' % (p,i,length,s))

        if p <= length:
            index = deepdebug and p-1 or length-l-p+1
            res[p] = int(s[index])
            p = None
        elif not deepdebug:
            s = ''

        i += 1

    return list(res[x] for x in source)


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 40. Champernowne\'s constant.')
        print('--> Find the value of the following expression: d1*d10*d100*d1000 ...')
        print('--> http://euler.jakumo.org/problems/view/40.html')
        print('--> ')
        print('--> Format: python champernown.py [-d] <n1> <n2> <n3> ...')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d: debug flag 0/1')
        print('-->   -D: deepdebug flag 0/1')
        print('--> ')
        print('--> v%s[Python3]' % version)
        
    else:
        digits = []

        print(sys.version)
        
        for x in argv[1:]:
            if x.startswith('-'):
                if 'd' in x[1:]:
                    debug = 1
                if 'D' in x[1:]:
                    deepdebug = 1
            else:
                num = x.isdigit() and int(x) or None
                digits.append(num)

        assert digits, "Number is not present!"
        
        started()

        print('>>> debug:%s' % debug)
        print('>>> deepdebug:%s' % deepdebug)

        r = run(digits)
        print(r, r and reduce(lambda a,b: a*b, r) or 0)

        finished()
