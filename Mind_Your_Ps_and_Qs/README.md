# Mind your Ps and Qs

Category: Cryptography </br>
AUTHOR: SARA

## Description
```
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?
```

## Values

We have been given the following values:
```
Decrypt my super sick RSA:
c: 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n: 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e: 65537
```
C is the ciphertext we wish to decode. N is the result of multiplying two prime numbers p and q, ie. `n = p * q`. E is the multiplicative inverse of a private exponent `d` modulo `phi`. Phi is equal to `(p-1)*(q-1)`. Here in a more ordered fashion:
```
C = ciphertext
p and q = prime numbers
n = p * q
phi = (p-1) * (q-1)
e = some number that 1 < e < phi and gcd(e,phi) == 1 
d = e^(-1) mod phi
```
Great! Now we just need to find p and q...

## Factor db

[Factordb](http://factordb.com/) is a database of factorised numbers. We could try out n:
```
n = 2159947535959146091116171018558446546179 * 658558036833541874645521278345168572231473 
```
Awesome! Now we can just calculate.

## Solving

```py
from Crypto.Util.number import inverse, long_to_bytes

c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e = 65537
p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,n)

print(long_to_bytes(m))
```
```bash
python3 solve.py 
b'picoCTF{sma11_N_n0_g0od_00264570}'
```
There we go! 