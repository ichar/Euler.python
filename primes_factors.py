# -*- coding: utf-8 -*-

import sys
import sympy
from lib.utils import *

version = '1.0'

debug = 0
deepdebug = 0

seq = [2,3,5,7,11,13,17,19]

## --------------------------------- ##

def get_next(num):
    n = num
    for _ in range(1,100):
        n += 1

        if deepdebug:
            print('--> get_next[%s]: %s' % (num, n))

        if prime(n, mode=1):
            seq.append(n)
            return n

    return None

def getNextPrime(num, mode=0):
    n = seq[-1]
    while True:
        if n > num or n is None:
            break
        n = get_next(n+1)

    if n is None:
        print('>>> Next not found: %s' % num)

    if debug and not mode:
        print('>>> seq:%s' % seq)

    return n

def prime(num, mode=0):
    # Это простое число?
    #   num - предельное значение для расчета
    #   mode - режим расчета: 0 (default) - генерация, 1 - проверка
    #   seq - список простых чисел
    #   p - порядковый номер простого числа из списка seq
    #   n - последовательность n,n+1 ...
    p = 0
    n = 0
    while True:
        if num in seq:
            return True

        if n >= num:
            break
        else:
            if n == 0 and p < len(seq):
                n = seq[p]
                p += 1
            elif mode == 0:
                n = get_next(seq[-1])
                if n is None:
                    if debug or deepdebug:
                        print('>>> Not found the next, n=%s, (%s,%s)' % (n,p,seq))
                    break
                else:
                    pass
            else:
                break

        if deepdebug:
            print('--> mode:%s %s,%s' % (mode,p,n))

        if num % n == 0:
            return num == n and True or False
        else:
            n = 0

    return True

def decompose(num, mode=0, mnemonic=False, list_only=False):
    # Разложение числа на простые сомножители
    # Любое натуральное число, большее единицы, можно представить в виде произведения простых сомножителей, 
    # причем единственным способом.
    divs = {}
    if not mode and getNextPrime(num-1, mode=mode):
        n = num
        p = 0
        while n > 1:
            x = seq[p]
            if n % x == 0:
                divs[x] = x in divs and divs[x]+1 or 1
                n = int(n/x)
                p = 0
            elif p < len(seq)-1:
                p += 1
            else:
               return None 

        if debug:
            print('>>> dividers:%s' % divs)
    
    elif mode == 1:
        divs = sympy.factorint(num)

    if divs and mnemonic:
        # Запись вида: (x1**n1)*(x2**n2)...
        s = ''
        for x in sorted(divs.keys()):
            s += '(%s**%s)' % (x, divs[x])

        return s

    if list_only:
        return divs and sorted(divs.keys()) or 0

    return divs

def run1(num):
    # Get next prime number over the given one
    # ----------------------------------------
    return getNextPrime(num)

def run2(num):
    # Check if the given number is a prime
    # ------------------------------------
    return prime(num)

def run3(num):
    # Get simple decomposition of the given number
    # --------------------------------------------
    return decompose(num, mode=1, mnemonic=True)

def run(n):
    # Find the first four consecutive integers to have four distinct prime factors each. 
    # What is the first of these numbers?
    # ----------------------------------------------------------------------------------
    res = []
    i = int('1%s' % str.zfill('0', n-1))
    while len(res) < n and i < 10**6:
        i += 1
        divs = decompose(i, mode=1, list_only=True)
        if len(divs) == n:
            if debug:
                print('>>> %s, divs:%s, %s' % (i, divs, len(res)))

            if not res or i == res[-1] + 1:
                res.append(i)
                continue
        
        res = []

    return res

def run_demo(n):
    counter = 0
    res = []
    for n in range(1000, 1000000):
        if counter == 4:
            print("Answer=", n - 4)
            break
        else:
            x = sympy.factorint(n)
            if len(x) == 4:
                counter += 1
                res.append((n, x))
            else:
                counter = 0
                res = []

    if debug:
        for n, x in res:
            print('>>> %s, divs:%s' % (n, x))

    return res


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 47. Distinct primes factors.')
        print('--> Find the first four consecutive integers to have four distinct prime factors each.')
        print('--> http://euler.jakumo.org/problems/view/47.html')
        print('--> ')
        print('--> Format: python primes_factors.py [-dD] [-demo] <n|number> [<mode>]')
        print('--> ')
        print('--> Options:')
        print('--> ')
        print('-->   -d     : debug flag 0/1')
        print('-->   -D     : deepdebug flag 0/1')
        print('-->   -demo  : demo mode')
        print('--> ')
        print('--> Arguments:')
        print('--> ')
        print('-->   n      : primarity count (x1*x2*...*xn), mode=0')
        print('-->   number : value for subtasks')
        print('-->   mode   : number of run-function (method): 0|1|2|3, default: 0')
        print('--> ')
        print('--> Subtasks (extra functions):')
        print('--> ')
        print('-->   mode=1 : Get next prime number over the given one')
        print('-->   mode=2 : Check if the given number is a prime')
        print('-->   mode=3 : Get simple decomposition of the given number')
        print('--> ')
        print('--> v%s[Python3]' % version)
        
    else:
        num = None
        mode = 0
        demo = False

        print(sys.version)
        
        for x in argv[1:]:
            if x.startswith('-'):
                if 'demo' in x[1:]:
                    demo = True
                else:
                    if 'd' in x[1:]:
                        debug = 1
                    if 'D' in x[1:]:
                        deepdebug = 1
            elif not num:
                num = x.isdigit() and int(x) or None
            else:
                mode = x.isdigit() and int(x)

        assert num, "Number is not present!"
        
        started()

        if demo:
            run = run_demo
        elif mode:
            run = mode == 3 and run3 or mode == 2 and run2 or mode == 2 and run2 or run1
        
        print(run(num))

        finished()
