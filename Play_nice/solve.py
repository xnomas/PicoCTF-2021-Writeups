from pprint import pprint

SQUARE_SIZE = 6

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

def split_by_two(text):
	splits = []
	for i in range(0,len(text),2):
		splits.append(text[i]+text[i+1])

	return splits

def on_same_line(text,index):
	x1 = index[text[0]][0]
	x2 = index[text[1]][0]

	if x1 == x2:
		return True 

def in_same_column(text,index):
	y1 = index[text[0]][1]
	y2 = index[text[1]][1]

	if y1 == y2:
		return True 
	
def get_rectangle(text,index,matrix):

	uno = text[0]
	due = text[1]

	uno_index = index[uno]
	due_index = index[due]

	if on_same_line(text,index):
		return f'{ matrix[uno_index[0]][uno_index[1]-1] + matrix[due_index[0]][due_index[1]-1] }'

	left_side = matrix[ uno_index[0] ][ due_index[1] ]
	right_side = matrix[ due_index[0] ][ uno_index[1] ]

	return f'{left_side+right_side}'



alphabet = 'n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy'
matrix = generate_square(alphabet)
"""
[['n', '5', 'v', 'g', 'r', 'u'],
 ['7', 'e', 'h', 'z', '1', 'k'],
 ['l', 'j', 'a', '8', 's', '9'],
 ['3', '4', '0', 'm', '2', 'w'],
 ['c', 'x', 'b', 'd', '6', 'p'],
 ['q', 'f', 'i', 't', 'o', 'y']]
"""
index = {}
for i in range(6):
	for x in range(6):
		index[matrix[i][x]] = [matrix[x].index(matrix[x][i]),x]

ciphertext = 'hnjm2e4t51v16gsg104i4oi9wmrqli'
splits = split_by_two(ciphertext)
plaintext = ''

for s in splits:
	plaintext += get_rectangle(s,index,matrix)

print(f'Decrypted: {plaintext}')

"""
nc64.exe mercury.picoctf.net 19354
Here is the alphabet: n5vgru7ehz1klja8s9340m2wcxbd6pqfitoy
Here is the encrypted message: hnjm2e4t51v16gsg104i4oi9wmrqli
What is the plaintext message? 7v8441mfrerhdr8rh20f2fya20noaq
Congratulations! Here's the flag: dbc8bf9bae7152d35d3c200c46a0fa30
"""