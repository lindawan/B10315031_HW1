# Encrypt and Decrypt cipher method

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Caesar cipher
def Caesar_Encrypt(plaintext, key):
	cipher = ''
	for i in plaintext:
		cipher += alphabet[(alphabet.index(i)+key) % 26]
	print('Cipher: ' + cipher)
	return cipher

def Caesar_Decrypt(cipher, key):
	plaintext = ''
	for i in cipher:
		plaintext += alphabet[(alphabet.index(i)-key+26) % 26]
	print('Plaintext: ' + plaintext)

# Monoalphabetic cipher
def Mono_Encrypt(plaintext, monoalphabet):
	cipher = ''
	for i in plaintext:
		cipher += monoalphabet[alphabet.index(i)]
	print('Cipher: ' + cipher)
	return cipher

def Mono_Decrypt(cipher, monoalphabet):
	plaintext = ''
	for i in cipher:
		plaintext += alphabet[monoalphabet.index(i)]
	print('Plaintext: ' + plaintext)

# Playfair cipher
def Playfair_Encrypt(plaintext, key):
	row = []
	for i in key:
		if i not in row:
			row.append(i)

	for i in alphabet.upper():
		if (i not in row) and (i != 'J'):
			row.append(i)

	matrix = []
	for i in range(5):
		matrix.append(row[i*5:(i+1)*5])
	del row

	for i in range(len(plaintext)):
		if plaintext[i] == plaintext[i+1]:
			plaintext = plaintext[:i+1] + 'x' + plaintext[i+1:]
			i+=1

	if len(plaintext)%2 == 1:
		plaintext += 'x'		

	cipher = ''
	for i in range(0, len(plaintext), 2):
		x1, y1 = find_pos(matrix, plaintext[i].upper())
		x2, y2 = find_pos(matrix, plaintext[i+1].upper())
		
		# in the same row
		if y1 == y2 :
			cipher += matrix[(x1+1)%5][y1]
			cipher += matrix[(x2+1)%5][y1]
		# in the same column
		elif x1 == x2 :
			cipher += matrix[x1][(y1+1)%5]
			cipher += matrix[x1][(y2+1)%5]
		else:
			cipher += matrix[x1][y2]
			cipher += matrix[x2][y1]

		cipher += ' '

	print('Cipher: ' + cipher)
	return cipher

# find the letter position in key matrix
def find_pos(matrix, letter):
	for x in range(5):
		for y in range(5):
			if letter == matrix[x][y]:
				return x,y

def Playfair_Decrypt(cipher, key):
	row = []
	for i in key:
		if i not in row:
			row.append(i)

	for i in alphabet.upper():
		if (i not in row) and (i != 'J'):
			row.append(i)

	matrix = []
	for i in range(5):
		matrix.append(row[i*5:(i+1)*5])
	del row

	plaintext = ''
	cipher = cipher.replace(' ', '')

	for i in range(0, len(cipher), 2):
		x1, y1 = find_pos(matrix, cipher[i])
		x2, y2 = find_pos(matrix, cipher[i+1])

		# in the same row
		if y1 == y2 :
			plaintext += matrix[(x1+4)%5][y1]
			plaintext += matrix[(x2+4)%5][y1]
		# in the same column
		elif x1 == x2 :
			plaintext += matrix[x1][(y1+4)%5]
			plaintext += matrix[x1][(y2+4)%5]
		else:
			plaintext += matrix[x1][y2]
			plaintext += matrix[x2][y1]

	for i in range(len(plaintext)):
		if i+2 == len(plaintext):
			break
		elif plaintext[i] == plaintext[i+2] and plaintext[i+1] == 'X':
			plaintext = plaintext.replace('X', '')

	if len(plaintext)%2 == 1:
		plaintext = plaintext[:len(plaintext)-1]

	print('Plaintext: ' + plaintext.lower())

# Vernam proposed the autokey system
def Autokey_Encrypt(plaintext, word):
	p_len = len(plaintext)
	w_len = len(word)
	key = word.lower() + plaintext[0:p_len-w_len]
	cipher = ''
	for i in range(p_len):
		cipher += alphabet[(alphabet.index(plaintext[i]) + alphabet.index(key[i])) % 26]
	cipher = cipher.upper()
	print('Cipher: ' + cipher)
	return cipher

def Autokey_Decrypt(cipher, word):
	plaintext = ''
	key = word
	w_len = len(word)
	for i in range(w_len):
		plaintext += alphabet[(alphabet.index(cipher[i].lower()) - alphabet.index(key[i].lower()) + 26) % 26]

	for i in range(w_len, len(cipher)):
		key += plaintext[i-w_len]
		plaintext += alphabet[(alphabet.index(cipher[i].lower()) - alphabet.index(key[i].lower()) + 26) % 26]

	print('Plaintext: ' + plaintext)

# Row transposition
def Rowtrans_Encrypt(plaintext, key):
	k_len = len(key)
	p_len = len(plaintext)
	matrix = []

	for col in range(k_len):
		row = []
		row.append(list(key)[col])
		for i in range(p_len/k_len):
			row.append(plaintext[i*k_len+col])
		matrix.append(row)

	matrix = sorted(matrix, key = lambda x:x[0])
	cipher = ''
	for col in matrix:
		for i in range(1, len(col)):
			cipher += col[i]
	print('Cipher: ' + cipher)
	return cipher

def Rowtrans_Decrypt(cipher, key):
	k_len = len(key)
	c_len = len(cipher)
	order = list(key)
	matrix = [sorted(order)]
	for col in range(c_len/k_len):
		row = []
		for i in range(k_len):
			row.append(cipher[col+i*(c_len/k_len)])
		matrix.append(row)
	
	plaintext = ''
	for i in range(1, c_len/k_len+1):
		for col in order:
			j = matrix[0].index(col)
			plaintext += matrix[i][j]

	print('Plaintext: ' + plaintext)

# Product cipher
def Product_Encrypt(plaintext, key):
	cipher = ''
	for i in range(len(plaintext)):
		cipher += plaintext[key.index(i+1)]
	print('Cipher: ' + cipher)
	return cipher

def Product_Decrypt(cipher, key):
	plaintext = ''
	for i in key:
		plaintext += cipher[i-1]
	print('Plaintext: ' + plaintext)