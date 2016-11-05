# -*- coding: utf-8 -*-

import sys
from lib.utils import *

version = '1.01'


class euler_f:

    def __init__(self, debug):
        self._debug = debug     # флаг отладки 0/1

    def _init_state(self):
        self._nums = list()     # список всех просчитанных значений
        self._x = 1             # кандидат делителя
        self.results = list()   # результат

    def __call__(self, num):
        
        self._init_state()
        self.run(num)

        if debug:
            print('>>> nums:', self._nums)

        return sorted(self.results)

    def rep(self, a, b):
        """
            Проверить кратность двух чисел a и b
        """
        return a != b and a%b == 0 and int(a/b) or 0

    def prime(self, num):
        """
            Существует ли в списке результатов число кратное заданному num
        """
        for n in self.results:
            if num%n == 0:
                return True
        return False

    def run(self, num, m=0):
        """
            Основной цикл.

            Аргументы:
                num  -- число для просчета в проходе
                m    -- проход (уровень рекурсии)

            Переменные:
                divs -- делители, полученные в текущем проходе
                x    -- расчетное значение делителя
                q    -- частное для делителя
        """
        divs = []

        while True:
            x = len(divs) and divs.pop(0) or self._x < num-1 and self._x+1 or 0
            if x <= 1 or x <= self._x:
                break
            
            self._x = x
            
            if num%self._x != 0:
                continue

            q = int(num/self._x)

            if self._debug:
                print('--> [%s, %s] %s:%s ' % (m, num, self._x, q))
            
            if not self.prime(self._x):
                self.results.append(self._x)
                divs.append(q)

            self.run(q, m+1)

            if q == 1 or self.results and q == self.results[0] or \
                self._x in self._nums or self._x > num:
                break

        self._nums.append(num)


if __name__ == '__main__':
    argv = sys.argv
    
    if len(argv) < 2 or argv[1].lower() in ('/h', '/help', '-h', 'help', '--help'):
        print('--> Euler Project.')
        print('--> --------------')
        print('--> Problem 3. Largest prime factor.')
        print('--> What is the largest prime factor of the number?')
        print('--> https://projecteuler.net/problem=3')
        print('--> ')
        print('--> Format: python euler_f.py [d] <number>')
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

        f = euler_f(debug)
        r = f(num)

        print(max(r), r)

        finished()
