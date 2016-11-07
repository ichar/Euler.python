# euler.python
Title: Project Euler
https://projecteuler.net/index.php?section=problems

Python 3.4

=============
fibonacci.py:
=============

Euler Project.
--------------
Problem 2. Sum of odd/even in the limited Fibonacci sequence of the number.
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
http://euler.jakumo.org/problems/view/2.html

Format: python fibonacci.py [-d] [-oe] [-l] \<number\>

Options:

    -d:     debug flag 0/1
    -o:     sum of odd numbers
    -e:     sum of even numbers
    -l:     limited by the given number

Arguments:

    number: limit sum value (4000000)

v1.0[Python3]

> python fibonacci.py -d -oe 10

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 03:28:44.717000

1
2
3
5
8
13
21
34
55
89
231

Finished at 2016-11-04 03:28:44.717000
Spent time: 0 msec (0.0 sec)

> python fibonacci.py -d -e -l 4000000

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 03:29:56.271000

2
8
34
144
610
2584
10946
46368
196418
832040
3524578
4613732

Finished at 2016-11-04 03:29:56.272000
Spent time: 1000 msec (0.001 sec)

===========
euler_f.py:
===========

Euler Project.
--------------
Problem 3. Largest prime factor.
What is the largest prime factor of the number?
https://projecteuler.net/problem=3

Format: python euler_f.py [-d] \<number\>

Options:

    -d:     debug flag 0/1

Arguments:

    number: some number value (13195)

v1.0[Python3]

> python euler_f 13195

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 02:15:43.056000

29 [5, 7, 13, 29]

Finished at 2016-11-04 02:15:43.056000
Spent time: 0 msec (0.0 sec)

> python euler_f 600851475143

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 02:16:57.175000

6857 [71, 839, 1471, 6857]

Finished at 2016-11-04 02:16:57.186000
Spent time: 11000 msec (0.011 sec)

==============
palindrome.py:
==============

Euler Project.
--------------
Problem 4. Find the largest palindrome made from the product of two n-digit numbers.
http://euler.jakumo.org/problems/view/4.html

Format: python palindrome.py [-d] \<n\>

Options:

    -d:     debug flag 0/1

Arguments:

    n:      degree of numbers (2|3|4 ...)

v1.0[Python3]

> python palindrome.py -d 2

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 03:34:14.272000

99*98=9702
99*97=9603
99*96=9504
99*95=9405
99*94=9306
99*93=9207
99*92=9108
99*91=9009
(9009, 99, 91)

Finished at 2016-11-04 03:34:14.273000
Spent time: 1000 msec (0.001 sec)

> python palindrome.py 3

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 03:35:50.766000

(580085, 995, 583)

Finished at 2016-11-04 03:35:50.805000
Spent time: 39000 msec (0.039 sec)

==============
pythagorean.py
==============

Euler Project.
--------------
Problem 9. Special Pythagorean triplet.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
http://euler.jakumo.org/problems/view/9.html

Format: python pythagorean.py [-dD] [-all] \<number\> [\<mode\>]

Options:

    -d:     debug flag 0/1
    -D:     deepdebug flag 0/1
    -all:   find all feasible solutions

Arguments:

    number: perimeter value (a + b + c)
    mode:   number of run-function (method): 1|2|3, default: 3

v1.0[Python3]

> python pythagorean.py 12

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 02:33:15.472000

(4, 3, 5) 60

Finished at 2016-11-05 02:33:15.472000
Spent time: 0 msec (0.0 sec)

> python pythagorean.py 1000

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 02:33:46.557000

(200, 375, 425) 31875000

Finished at 2016-11-05 02:33:46.557000
Spent time: 0 msec (0.0 sec)

> python pythagorean.py -d -all 1080

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 03:12:31.836000

mode:3

1080: (432, 180, 468)
Итерация: 147
1080: (280, 351, 449)
Итерация: 177

[(432, 180, 468), (280, 351, 449)] ... Total:2

Finished at 2016-11-05 03:12:31.940000
Spent time: 104000 msec (0.104 sec)

===========
collatz.py:
===========

Euler Project.
--------------
Problem 14. Longest Collatz sequence.
Which starting number, under one million, produces the longest chain?
https://projecteuler.net/problem=14

Format: python collatz.py [-d] \<number\>

Options:

    -d:     debug flag 0/1

Arguments:

    number: limit of chain value (4000000)

v1.0[Python3]

> python collatz.py 13

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 02:26:59.947000

9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
len: 20

Finished at 2016-11-04 02:26:59.948000
Spent time: 1000 msec (0.001 sec)

> python collatz.py 1000000

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 02:27:44.514000

837799 -> 2513398 -> 1256699 -> 3770098 -> 1885049 -> 5655148 -> 2827574 -> 1413787 -> 4241362 -> 2120681 -> 6362044 ... 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
len: 525

Finished at 2016-11-04 02:30:13.447000
Spent time: 148933000 msec (148.933 sec)

=============
factorial.py:
=============

Euler Project.
--------------
Problem 20. Sum of digits in factorial of the number.
http://euler.jakumo.org/problems/view/20.html

Format: python factorial.py [-d] \<number\>

Options:

    -d:     debug flag 0/1

Arguments:

    number: source value (100)

v1.0[Python3]

> python factorial.py -d 10

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 02:41:46.558000

3628800

Factorial at 2016-11-04 02:41:46.558000
Spent time: 0 msec (0.0 sec)

27

Finished at 2016-11-04 02:41:46.558000
Spent time: 0 msec (0.0 sec)

> python factorial.py -d 100

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-04 02:42:14.641000

93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

Factorial at 2016-11-04 02:42:14.641000
Spent time: 0 msec (0.0 sec)

648

Finished at 2016-11-04 02:42:14.642000
Spent time: 1000 msec (0.001 sec)

==========
spiral.py:
==========

Euler Project.
--------------
Problem 28. Number spiral diagonals.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
http://euler.jakumo.org/problems/view/28.html

Format: python pythagorean.py [-dD] <number>

Options:

  -d    : debug flag 0/1
  -D    : deepdebug flag 0/1 (prints sequence on the screen)

Warning! Be carefull with -D.

v1.0[Python3]

> python spiral.py -dD 5

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-06 06:29:14.174000

2 R:1 (1:0)
3 R:1 (2:0)
R:1 [1, 3])
4 R:1 (1:1)
5 R:1 (2:1)
R:1 [1, 3, 5])
6 R:1 (1:2)
7 R:1 (2:2)
R:1 [1, 3, 5, 7])
8 R:1 (1:3)
9 R:1 (2:3)
R:1 [1, 3, 5, 7, 9])
10 R:2 (1:0)
11 R:2 (2:0)
12 R:2 (3:0)
13 R:2 (4:0)
R:2 [1, 3, 5, 7, 9, 13])
14 R:2 (1:1)
15 R:2 (2:1)
16 R:2 (3:1)
17 R:2 (4:1)
R:2 [1, 3, 5, 7, 9, 13, 17])
18 R:2 (1:2)
19 R:2 (2:2)
20 R:2 (3:2)
21 R:2 (4:2)
R:2 [1, 3, 5, 7, 9, 13, 17, 21])
22 R:2 (1:3)
23 R:2 (2:3)
24 R:2 (3:3)
25 R:2 (4:3)
R:2 [1, 3, 5, 7, 9, 13, 17, 21, 25])

[1, 3, 5, 7, 9, 13, 17, 21, 25]
Total selected items in the spiral: 9 Sum: 101

Finished at 2016-11-06 06:29:14.174000
Spent time: 0 msec (0.0 sec)

> python spiral.py 101

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-06 06:29:57.653000

Total selected items in the spiral: 201 Sum: 692101

Finished at 2016-11-06 06:29:57.663000
Spent time: 10000 msec (0.01 sec)

> python spiral.py 1001

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-06 06:30:15.565000

Total selected items in the spiral: 2001 Sum: 669171001

Finished at 2016-11-06 06:30:16.739000
Spent time: 1174000 msec (1.174 sec)

==============
champernown.py
==============

Euler Project.
--------------
Problem 40. Champernowne's constant.
Find the value of the following expression: d1 * d10 * d100 * d1000 ...
http://euler.jakumo.org/problems/view/40.html

Format: python champernown.py [-dD] \<n1\> \<n2\> \<n3\> ...

Options:

    -d:     debug flag 0/1
    -D:     deepdebug flag 0/1 (prints sequence on the screen)

Arguments:

    nX:     digit positions list item (1 10 100 ...)

Warning! Be carefull with -D.

v1.0[Python3]

> python champernown.py 1 10 100 1000 10000 100000 1000000

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 06:09:44.462000

[1, 1, 5, 3, 7, 2, 1] 210

Finished at 2016-11-05 06:09:44.737000
Spent time: 275000 msec (0.275 sec)

=================
triangle_words.py
=================

Euler Project.
--------------
Problem 42. Coded triangle numbers.
How many are triangle words in the given file?
http://euler.jakumo.org/problems/view/42.html

Format: python pythagorean.py [-dD] <source> [<mode>]

Options:

    -d     : debug flag 0/1
    -D     : deepdebug flag 0/1

Arguments:

    source : "word.txt" file path
    mode   : number of run-function (method): 1|2, default: 1

Method mode=1 checks the file, and mode=2 - simple words only: ABOVE,ABSOLUTELY,SOLUTION.

Note that words in the file enclosed in quotation marks!

v1.0[Python3]

> python triangle_words.py -d words.txt

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 09:37:01.544000
Words count in line [1]: 1786

"ABILITY"
"ABOVE"
"ACCOMPANY"
"ACHIEVEMENT"
"AGENCY"
"AGREE"
"AIR"
"ALREADY"
"AN"
"ANCIENT"
"APPARENT"
"APPOINT"
"APPROACH"
"ASSUME"
"AT"
"ATMOSPHERE"
"BAG"
"BAND"
"BANK"
"BAR"
"BEAT"
"BELONG"
"BENEATH"
"BONE"
"BOTH"
"BRIDGE"
"BUILDING"
"BURN"
"CALL"
"CAPACITY"
"CAREFUL"
"CASE"
"CHILD"
"CIVIL"
"CLOSELY"
"COME"
"CONFIDENCE"
"CONFIRM"
"CONSERVATIVE"
"CONSTRUCTION"
"CONTENT"
"COULD"
"CURRENTLY"
"DECISION"
"DEFINITION"
"DEMOCRATIC"
"DEPUTY"
"DESPITE"
"DISTINCTION"
"EAST"
"EDGE"
"EDUCATIONAL"
"EFFECT"
"EQUIPMENT"
"EVENT"
"FACE"
"FAIL"
"FAMILY"
"FEEL"
"FIELD"
"FIGURE"
"FLOOR"
"FREEDOM"
"FUND"
"FUTURE"
"GENTLEMAN"
"GREY"
"GROWTH"
"HAIR"
"HAPPY"
"HAVE"
"HERE"
"HIS"
"IF"
"INCIDENT"
"INCREASED"
"INCREASINGLY"
"INDIVIDUAL"
"INSTRUMENT"
"INTEND"
"INTENTION"
"IS"
"LAW"
"LEADER"
"LEAVE"
"LENGTH"
"LESS"
"LITTLE"
"LOVELY"
"MAN"
"MATCH"
"MERELY"
"MILK"
"MISTAKE"
"MOVE"
"MUCH"
"NEED"
"NOTICE"
"OBJECT"
"OBJECTIVE"
"OF"
"OIL"
"ONLY"
"OTHER"
"OURSELVES"
"PART"
"PASS"
"PATH"
"PERFORM"
"PRISON"
"PRIVATE"
"PROBABLY"
"PROCEDURE"
"QUALITY"
"QUESTION"
"RANGE"
"READ"
"REAL"
"RELIEF"
"REMOVE"
"REPRESENT"
"REQUEST"
"RESPOND"
"RIDE"
"SAMPLE"
"SAY"
"SEAT"
"SECURITY"
"SINGLE"
"SKY"
"SOIL"
"SOLICITOR"
"SONG"
"SOUTHERN"
"SPIRIT"
"START"
"SUGGESTION"
"TALL"
"TAX"
"THEORY"
"THREATEN"
"THROUGHOUT"
"TITLE"
"TOOTH"
"TOTALLY"
"TRAVEL"
"TYPE"
"UNABLE"
"UNDERSTAND"
"UPON"
"USE"
"VARIOUS"
"VARY"
"VIDEO"
"WAGE"
"WARM"
"WATCH"
"WE"
"WHILST"
"WIDELY"
"WOMAN"

Triangle words: 161
Total:161

Finished at 2016-11-05 09:37:01.573000
Spent time: 29000 msec (0.029 sec)

> python triangle_words.py -D ABOVE,ABSOLUTELY,SOLUTION 2

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 09:39:01.049000

Word [ABOVE]: 45
D [45]: 361
x1[9.0], x2[-10.0], valid: True
Word [ABSOLUTELY]: 132
D [132]: 1057
x1[15.75576820700886], x2[-16.75576820700886], valid: False
Word [SOLUTION]: 125
D [125]: 1001
x1[15.319292019556375], x2[-16.319292019556375], valid: False

Total:1

Finished at 2016-11-05 09:39:01.050000
Spent time: 1000 msec (0.001 sec)

> python triangle_words.py -D SKY 2

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-05 09:43:56.662000

Word [SKY]: 55
D [55]: 441
x1[10.0], x2[-11.0], valid: True

Total:1

Finished at 2016-11-05 09:43:56.662000
Spent time: 0 msec (0.0 sec)

==================
primes_factors.py:
==================

Euler Project.
--------------
Problem 47. Distinct primes factors.
Find the first four consecutive integers to have four distinct prime factors each.
http://euler.jakumo.org/problems/view/47.html

Format: python primes_factors.py [-dD] [-demo] <n|number> [<mode>]

Options:

    -d     : debug flag 0/1
    -D     : deepdebug flag 0/1
    -demo  : demo mode

Arguments:

    n      : primarity count (x1*x2*...*xn), mode=0
    number : value for subtasks
    mode   : number of run-function (method): 0|1|2|3, default: 0

Subtasks (extra functions):

    mode=1 : Get next prime number over the given one
    mode=2 : Check if the given number is a prime
    mode=3 : Get simple decomposition of the given number

v1.0[Python3]

> python primes_factors.py 4

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
Started at 2016-11-07 13:49:40.787000

[134043, 134044, 134045, 134046]

Finished at 2016-11-07 13:49:45.719000
Spent time: 4932000 msec (4.932 sec)

Check if the given number is a prime
------------------------------------

> python primes_factors.py -dD 134043 2

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
>>> Started at 2016-11-07 13:52:11.581000

--> mode:0 1,2
--> mode:0 2,3

False

>>> Finished at 2016-11-07 13:52:11.581000
>>> Spent time: 0 msec (0.0 sec)

Get simple decomposition of the given number
--------------------------------------------

> python primes_factors.py 134043 3

3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)]
>>> Started at 2016-11-07 13:53:12.821000

(3\*\*1)(7\*\*1)(13\*\*1)(491\*\*1)

>>> Finished at 2016-11-07 13:53:12.821000
>>> Spent time: 0 msec (0.0 sec)
