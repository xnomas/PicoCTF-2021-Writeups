import string

alphabet = 'abcdefghijklmnop'
offset = 97


def b16_decode(encoded):
	
	for e in encoded:
		p1 = f"{alphabet.index(encoded[:1]):04b}"
		p2 = f"{alphabet.index(encoded[1:]):04b}"

		binary = p1 + p2
		char = chr(int(binary,2))
		
		return char

def shift(c, k):
	t1 = ord(c) + offset
	t2 = ord(k) + offset
	return alphabet[(t1 + t2) % len(alphabet)]

def check(text):
	for t in text:
		if t not in string.printable:
			return False

	return True

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
