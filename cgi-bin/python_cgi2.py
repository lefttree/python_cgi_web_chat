#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Web Chat Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print '</body>'
print '</html>'


import math
import random

def eeuclid(a, n, debug=False):
    a1, a2, a3 = 1, 0, n
    b1, b2, b3 = 0, 1, a
    while b3 > 1:
        q = math.floor(a3/b3)
        t1, t2, t3 = (a1 - (q * b1), a2 - (q * b2), a3 - (q * b3))
        a1, a2, a3 = b1, b2, b3
        b1, b2, b3 = t1, t2, t3
    if b3 == 1:
        if debug:
            print 'return inverse'
        return (b2, True)
    if b3 == 0:
        if debug:
            print 'return gcd'
        return (a3, False)

def totient(p, q):


    return (p - 1) * (q - 1)

def coprime(t):
    nums = eratosthenes(t)
    return random.choice(nums)

def eratosthenes(n):
    nums = range(2, n)
    p = t = 2
    while p**2 <= n:
        while t <= n:
            s = t * p
            if s in nums:
                del nums[nums.index(s)]
            t += 1
        p = t = nums[nums.index(p) + 1]
    return nums

def keygen(p, q, e=None):
    n = p * q
    t = totient(p, q)
    if e is None:
        e = coprime(t)
    d = int(eeuclid(e, t)[0] % t) 
    return (n, e, d, str((n, e, d)))

def rsa(message, public, private, decrypt=False):
    if decrypt is False:
        return int(message**public[1] % public[0])
    else:
        return int(message**private[1] % private[0])


