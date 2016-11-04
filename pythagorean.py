# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.0'

debug = 0
deepdebug = 0

## --------------------------------- ##

def D(h):
    p = 2*h
    for x in range(1,10000):
        if (x*x)%p == 0:
            return x

def A(h, e):
    return h+e

def B(h, e):
    return int(e+(e*e)/2*h)

def C(h, b):
    return int(h+b)

def get_next(num):
    for h in range(1,101):
        for k in range(1,101):
            yield (h, k)

def run(num):
    # Расчет "Тейган и Хедвин":
    # http://ananserr.narod.ru/2.sp.gen_ru.html
    # для случая a+b+c=1000 не работает!!!
    i = 0
    for h, k in get_next(num):
        d = D(h)
        if d is None:
            continue
        e = k * d
        
        a = A(h, e)
        b = B(h, e)
        c = C(h, b)

        p = a + b + c

        if debug or (deepdebug and abs(num-p) < 100):
            print('--> %s(%s,%s)[%s:%s:%s]' % (p,h,k,a,b,c))

        if p == num:
            return a, b, c
        elif i > 1000000: #p > num or 
            if debug or deepdebug:
                print('>>> Overflow: %s' % i)
            return 0

        i += 1

    if debug or deepdebug:
        print('>>> Not found, i=%s, (%s,%s)' % (i,h,k))

def test(num):
    # Простой перебор от 1 до num/2
    # очень долго!!!
    n = int(num/2)
    for a in range(1,n+1):
        for b in range(1,n+1):
            for c in range(1,n+1):
                p = a + b + c
                if p == num and a*a+b*b == c*c:
                    return a,b,c

def demo(num):
    # Формула Эвклида:
    # a = 2*m*n, b = m*m − n*n, c = m*m + n*n , m > n
    # просто и быстро (+++)
    i = 0
    for m in range(2, int(num/2)):
        for n in range(1, m):
            if 2*m*n + 2*m*m == num:
                a, b, c = 2*m*n, m*m - n*n, m*m + n*n
                if debug:
                    print('>>> %s: %s' % ((a+b+c),(a, b, c)))
                    print('>>> Кол-во итераций: %s' % i)
                return a,b,c
            
            i += 1

    if debug or deepdebug:
        print('>>> Overflow: %s' % i)


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 9. Special Pythagorean triplet.')
        print('--> There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.')
        print('--> http://euler.jakumo.org/problems/view/9.html')
        print('--> ')
        print('--> Format: python pythagorean.py [-d] <number>')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d: debug flag 0/1')
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

        r = demo(num)
        print(r, r and len(r) == 3 and r[0]*r[1]*r[2] or 0)

        finished()
