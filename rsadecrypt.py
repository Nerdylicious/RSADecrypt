import math
import re

alpha = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}

def Decode(z, plaintext):

	#determine 1st letter
	letter_1 = z - (z % math.pow(26, 2))	
	letter_1 = int(letter_1 / math.pow(26, 2))
	plaintext = plaintext + alpha[letter_1]

	#determine 2nd letter
	letter_2 = z % math.pow(26, 2)
	letter_2 = letter_2 - (z % 26)
	letter_2 = int(letter_2 / 26)
	plaintext = plaintext + alpha[letter_2]

	#determine the 3rd letter
	letter_3 = z % 26
	plaintext = plaintext + alpha[letter_3]
	
	return plaintext

def SquareAndMultiply(x, c, n):
	c = '{0:b}'.format(c)
	z = 1
	l = len(c)

	for i in range(0, l):
		z = (math.pow(z, 2)) % n
		if (c[i] == "1"):
			z = (z*x) % n
	return z
	
n = 18923
a = 5797
	
pattern = re.compile(r"\s+")
f = open("table5-1.txt", "r")

ciphertext = ""
plaintext = ""

for line in f:
	line = line.split("\t")
	for i in range(0, len(line)):
		line[i] = re.sub(pattern, "", line[i])
		line[i] = int(line[i])
		z = SquareAndMultiply(line[i], a, n)
		plaintext = Decode(z, plaintext)
print "\nPlaintext:"
print plaintext



