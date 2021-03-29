# New caesar

Category: Cryptography </br>
AUTHOR: MADSTACKS

**DISCLAIMER! I do not own any of the challenge files!**

## Description

```
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{})
lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil
```

## What is the caesar cipher? 

A monoalphabetic substition cipher with a right shift of 3. Now that the fancing words are out of the way, what does it actually do? Well the classic caesar cipher just takes each letter and shifts it 3 positions to the right in the alphabet. If the shift would go over the length of the alphabet, then just loop back around. We have been given cipher text and the source code used to encrypt it.

## new_caesar.py

Lets look at the variables first:
```py
import string

LOWERCASE_OFFSET = ord("a") 

ALPHABET = string.ascii_lowercase[:16]
```
So the offset (our shift value) is the ascii value of `a` (97), and our special alphabet is a slice of all lowercase letters: `abcdefghijklmnop`. Great! On to the functions.
```py
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc
```
Alright, this might look confusing, but if we break it down. Iterate over the plaintext string, and convert the ascii value of each letter into binary format, keep it at a length of 8 (so a byte) and padded by 0's if needed. Try this:
```py
python
>>> f'{ord("a"):08b}'
'01100001'
>>> int(f'{ord("a"):08b}',2)
97
```
This is the except, that I used a python 3 format string (they are just so pretty!). Right, so what happens next? Well the binary string is split into two halves: `0110` and `0001` in our case, these are converted back into decimal, and used as an index in the alphabet. Again, try it in the terminal! 
```python
>>> alphabet = string.ascii_lowercase[:16]
>>> a = f'{ord("a"):08b}'
>>> int(a[:4],2)
6
>>> int(a[4:],2)
1
>>> alphabet[6]+alphabet[1]
'gb'
```
So `a` turns into `gb`. Great! Now on to the `shift`:
```py
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
```
For the two variables we get two characters, and substract `97` from their ascii values. Then just add those together (modulo length of the alphabet so we stay in bounds) and use that value as an index for the alphabet list.
```py
flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
``` 
This is all put together here. The initial assertions are really telling. The assert makes sure that a condition is met and if not it raises an assertion error. So we can tell that the key is made up of letters from the alphabet only! Next we know that the length of this key is 1. The flag is then put into `b16_encode`, so it doubles in length! And here is the `enumerate` method:
```python
>>> c = 'lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil'
>>> for i,c in enumerate(c):
...     print(f'{i} {c}')
...
0 l
1 k
2 m
3 j
4 k
5 e
6 m
7 j
8 m
9 k
...
...
```
It just indexes each letter from the b16 encoded string. Each letter (c) is shifted using the key! "But what about the modulus?" Who cares? The length of the key is 1, so we are just going to use the single letter anyway.

## solve.py

Now we just have to reverse it all:
```py
def shift(c, k):
	t1 = ord(c) + offset
	t2 = ord(k) + offset
	return alphabet[(t1 + t2) % len(alphabet)]
``` 
This should be obvious. Next.
```py
def b16_decode(encoded):
	
	for e in encoded:
		p1 = f"{alphabet.index(encoded[:1]):04b}"
		p2 = f"{alphabet.index(encoded[1:]):04b}"

		binary = p1 + p2
		char = chr(int(binary,2))
		
		return char
```
Here the input are two letters, we split them, get their index in the alphabet and turn into a binay string of length 4. Put those together and convert to ascii. Then I just added a `check` function to only see if the decoded string contains printable letters:
```py
def check(text):
	for t in text:
		if t not in string.printable:
			return False

	return True
```
And here is the rest:
```py
ciphertext = 'lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil'

for a in alphabet:
	plain = ''
	key = a
	decode = '' 

	for i,c in enumerate(ciphertext):
		decode += shift(c, key)

	for i in range(0,len(decode),2):
		temp = (decode[i] + decode[i+1])

		plain += b16_decode(temp)

	if check(plain):
		print(f'key = {a} : {plain} ')
		print() 
```
Run it and this is the output:
```
key = g : TcNcd.N#" SQ%!R$% 'RS&$U S/Q'"'"!Q%&Q#% 

key = h : et_tu?_431db62c5618cd75f1d0b83832b67b46 
```
Try and guess which is the flag ;)