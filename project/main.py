from collections import defaultdict

def caesar_cipher(clear_text, shift=13):
	'''Encrypts the given clear text using the super 
	simple caesar cipher. This is case insensetive
	and strips characters outside range A-Z
	'''
	upper_text = clear_text.upper()
	result = ""
	for c in upper_text:
		if c.isupper():
			result += chr(((ord(c) + shift - 65) % 26) +  65)
	return result

def letter_frequency_count(string):
	'''Counts the frequency of each letter in the string
	Returns: sorted list of tuples (count, character)
	'''
	freq = defaultdict(int)
	for c in string.upper():
		if c.isupper():
			freq[c] += 1
	return [(k, freq[k]) for k in sorted(freq, key=freq.get, reverse=True)]

if __name__ == "__main__":
	while True:
		text = raw_input("Text to encrypt: ")
		if text == "quit":
			break
		print caesar_cipher(text)