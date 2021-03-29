# Play Nice

Category: Cryptography </br>
AUTHOR: MADSTACKS

## Description
```
Not all ancient ciphers were so bad... The flag is not in standard format.
```

## What is the playfair cipher?

We were given souce code called `playfair.py`, from this we can tell that the cipher used will be a playfair cipher! But what is that? A detailed explenation can be found [here](https://en.wikipedia.org/wiki/Playfair_cipher). I know about this cipher from NetOnCTF 2021, I have writeups on challenges from it [here](https://github.com/xnomas/NetOn-Writeups-2021). But lets get into the nitty gritty.</br>
Tha basics that we need is an alphabet, size of our matrix and some ciphertext:
```
+---------+
|A|B|C|D|E|
+---------+
|F|G|H|I|J|
+---------+
|K|L|M|N|O|
+---------+
|P|Q|R|S|T|
+---------+
|U|W|X|Y|Z|
+---------+
```
This could be an example matrix. And this matrix is our key! (also notice one typical thing, we left out one letter `V`. Most often you will see `I` or `J` left out) We use it to decrypt and encrypt text. Now, instead of taking you through all of the ins and outs of encryption and decryption, here are the basic concepts if decrypting text:</br>

If we want to decrypt the text `QKDUKFHS` here is how we do it:
1. Split into pairs = `QK, DU, KF, HS`
2. Go through the pairs
3. If the letters are on the same line, shift left
4. If the letters are in the same column, shift up
5. Else form a rectangle, with the letters being one of the top or bottom edges. Get the first letter under the left top and first letter above right bottom (example to follow)
</br></br>

So here we go:
```
QK = Form a rectangle:

K L
P Q

So Q turns into P and K into L; QK = PL
---------------------------------------
DU = Form a rectangle:

ABCD<
FGHI
KLMN
PQRS
UWXY
^

D turns into A, U turns into Y; DU = AY
---------------------------------------

KF = In the same column, shift up!
---
|A|
|F|
|K|
---
K turns into F, F turns into A; KF = FA
----------------------------------------
HS  = Form a rectangle:

HI
MN
RS

H turns into I, S turns into R; HS = IR
---------------------------------------

QKDUKFHS
PLAYFAIR
```
Great, now onto solving the challenge.

## Takeaways from playfair.py

There are just a few important parts to note:
```py
SQUARE_SIZE = 6
```
This is the size of our matrix.
```py
def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix
```
And the function that generates our matrix, which looks like this:
```py
[['n', '5', 'v', 'g', 'r', 'u'],
 ['7', 'e', 'h', 'z', '1', 'k'],
 ['l', 'j', 'a', '8', 's', '9'],
 ['3', '4', '0', 'm', '2', 'w'],
 ['c', 'x', 'b', 'd', '6', 'p'],
 ['q', 'f', 'i', 't', 'o', 'y']]
```
And then when we connect to the remote service, we get this ciphertext:
```
hnjm2e4t51v16gsg104i4oi9wmrqli
```

## Decoding

You can use an online decoder, like [this one](https://www.dcode.fr/playfair-cipher). But I decided to practice and code it.
```py
alphabet = 'n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy'
matrix = generate_square(alphabet)

index = {}
for i in range(6):
	for x in range(6):
		index[matrix[i][x]] = [matrix[x].index(matrix[x][i]),x]
```
Here we generate the matrix, from that I made a dictionary containing all the characters of the alphabet, with their corresponding index.
```py
def split_by_two(text):
	splits = []
	for i in range(0,len(text),2):
		splits.append(text[i]+text[i+1])

	return splits

ciphertext = 'hnjm2e4t51v16gsg104i4oi9wmrqli'
splits = split_by_two(ciphertext)
plaintext = ''
```
Then I just simply split the cipher text into pairs.
```py
for s in splits:
	plaintext += get_rectangle(s,index,matrix)

print(f'Decrypted: {plaintext}')
```
And finally for each pair I find either the rectangle, or the column/row (those are in the get_rectangle function). I don't think I need to go too into detail of the `rectangle` code, since we went over how decryption works. Run and get this:
```
Decrypted: 7v8441mfrerhdr8rh20f2fya20noaq
```
Now just connect with netcat and here we go:
```
nc mercury.picoctf.net 19354
Here is the alphabet: n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy
Here is the encrypted message: hnjm2e4t51v16gsg104i4oi9wmrqli
What is the plaintext message? 7v8441mfrerhdr8rh20f2fya20noaq
Congratulations! Here's the flag: dbc8bf9bae7152d35d3c200c46a0fa30
```
The flag is just the flag, no `picoCTF{}`. 