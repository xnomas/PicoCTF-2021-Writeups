# Easy Peasy

Category: Cryptography </br>
AUTHOR: MADSTACKS
</br></br>

**DISCLAIMER! I do not own any of the challenge files!**


## Description
```
A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})
```

## Connecting

We were given an `nc` command to run (as well as the source code, more on that later).  
```
nc mercury.picoctf.net 58913
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57

What data would you like to encrypt?
```
Alright... so what exactly is a one-time pad? The gimmick of it is, that we have a random string (that is our key) that is at least as long as the message (in our case it's longer). But what is the most important part? This surely can't be secure! Well it is, only if the key is never reused. Hell, even the NSA used a one-time pad! On paper! (listen about that [here](https://darknetdiaries.com/episode/83/)). Now that we know this, time to look at the source code.

## Studying otp.py

At the start we have some important variables:
```py
KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"
```
Next we have two functions `encrypt` and `startup`. `startup` is called first, it reads from the `FLAG_FILE`, sets a starting and end point and then encrypts the flag using the key from `KEY_FILE`:
```py
def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location
```
So what are the `start` and `stop` variables for? These are file offsets, so the key will always be as long as the message. Now the `encrypt` function:
```py
def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location # starts at 32
	stop = key_location + len(ui) # 32 + len(input)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN: 
		stop = stop % KEY_LEN # if stop == KEY_LEN then stop = 0
		key = kf[start:] + kf[:stop] # key = [start, 0]
	else:
		key = kf[start:stop]
	key_location = stop # we want this to be 0 

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location
```
This is the really important function for us. I added some comments for myself as I was solving the challenge. So what is going on here? The function reads our input (if none is provided or its bigger than 50000 return -1), gets a starting file offset and calculates the ending offset. The start is where the end was previously, so when we give our first input it is the length of the flag ( `len(flag)/2` actually. As each letter is a hex number of atleast two letters/digits).</br>

So this gives us an offset of `32`. What next? Look here:
```py
	if stop >= KEY_LEN: 
		stop = stop % KEY_LEN # if stop == KEY_LEN then stop = 0
		key = kf[start:] + kf[:stop] # key = [start, 0]
	else:
		key = kf[start:stop]
	key_location = stop # we want this to be 0 
```
Interesting huh? If the `stop` offset is equal or larger then the `KEY_LEN` variable we set stop to `stop % KEY_LEN`. What does that mean for us? Well, if we get the stop to be exactly `KEY_LEN` then `KEY_LEN % KEY_LEN == 0` and bam! We have one-time pad reuse!! If this is not obvious to you, try playing around with it in the console. </br>

Lastly, since the "encryption" is just a xor, we can easily get the result by xoring with the key again.

## Getting padding reuse

Now we just need to construct our payload and run our script. Once we loop the pad back to zero, we need an input of length `32`. Because we know the plaintext and the ciphertext, we can xor them and get the key! Then just xor with the encrypted flag and whabbam.
```py
from pwn import *

import binascii

offset = 50000 - 32

p = remote('mercury.picoctf.net', 58913)

print(p.recvline())
print(p.recvline())
encrypted_flag = p.recvline().strip()

print(encrypted_flag)

p.recvuntil('?')
p.sendline('A'*offset)

p.recvuntil('?')

p.sendline('A'*32)

p.recvline()
```
I used `pwntools` because it allowed me to easily interact with the remote service. Like this I receive lines, send a bunch of A's (to get back to offset 0) and send exactly 32 A's. 
```py
encoded = p.recvline().strip()

print(f'encoded input: {encoded}')

encoded = binascii.unhexlify(encoded)

print(f'unhexed input: {encoded}')
```
Then unhexlify the input so we can decode it! 
```py
message = 'A'*32

key = []

for e in range(len(encoded)):
	key.append( ord(message[e])^encoded[e] )

print(f'[+] Found key: {key}')
```
Then just xor the unhexlified encrypted message with our plaintext and we have the key! 
```py
decoded_flag = []

encrypted_flag = binascii.unhexlify(encrypted_flag)

for i in range(32):
	decoded_flag.append( chr(key[i]^encrypted_flag[i]) )

flag = ''.join(decoded_flag)

print(f'flag: {flag}')
```
And finally the flag is decrypted. This is all put together in [solve.py](https://github.com/xnomas/PicoCTF-2021-Writeups/easy_peasy/solve.py). Then when we run it:
```py
python3 solve.py 
[+] Opening connection to mercury.picoctf.net on port 58913: Done
b'******************Welcome to our OTP implementation!******************\n'
b'This is the encrypted flag!\n'
b'51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57'
encoded input: b'23666b6f3a3c1a111d3971771d397122181d3927731d3925231d3924241d3924'
unhexed input: b'#fko:<\x1a\x11\x1d9qw\x1d9q"\x18\x1d9\'s\x1d9%#\x1d9$$\x1d9$'
--------------------------------------------------
Working on the decode
--------------------------------------------------
[+] Found key: [98, 39, 42, 46, 123, 125, 91, 80, 92, 120, 48, 54, 92, 120, 48, 99, 89, 92, 120, 102, 50, 92, 120, 100, 98, 92, 120, 101, 101, 92, 120, 101]
flag: 35ecb423b3b43472c35cc2f41011c6d2
```
Now just wrap the output in `picoCTF{35ecb423b3b43472c35cc2f41011c6d2}`. 