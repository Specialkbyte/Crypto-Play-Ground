from unittest import TestCase

from project.caesar_cipher import rot13
from project.caesar_cipher import encrypt as caesar_cipher_encrypt
from project.caesar_cipher import decrypt as caesar_cipher_decrypt
from project.crack_caesar_cipher import crack_caesar_cipher
from project.plaintext_recogniser import PlaintextRecogniser

class CaesarCipherTests(TestCase):
	'''Tests the Caesar Cipher (& ROT13) encryption and decryption
	as some properties of those functions like that ROT13 is
	commutitive.
	'''

	def test_rot13(self):
		clear_text = "The brown fox jumped over the cow in the dark field."
		self.assertEqual(rot13(clear_text), "GUROEBJASBKWHZCRQBIREGURPBJVAGURQNEXSVRYQ")

	def test_rot13_communtivity(self):
		'''Tests that that this ROT13 implemention is commutitive'''
		clear_text = "Hello world! Goodbye world!"
		# the returned decrypted text will be uppercase and contain no spaces/puncuation
		self.assertEqual(decrypted_text(clear_text), rot13(rot13(clear_text)))

	def test_encrpyt(self):
		'''Tests that you can do a caesar cipher with an arbitary shift value'''
		clear_text = "Hello world!"
		cipher_text = caesar_cipher_encrypt(clear_text, 3)
		self.assertEqual(cipher_text, "KHOORZRUOG")

	def test_encrpyt_2(self):
		'''Tests that you can do a caesar cipher with an arbitary shift value'''
		clear_text = "Hello world!"
		cipher_text = caesar_cipher_encrypt(clear_text, 5)
		self.assertEqual(cipher_text, "MJQQTBTWQI")

	def test_decrypt(self):
		clear_text = "Hello world!"
		decryption = caesar_cipher_decrypt(caesar_cipher_encrypt(clear_text, 3), 3)
		self.assertEqual(decryption, decrypted_text(clear_text))

	def test_encrpyt_with_large_shift(self):
		'''Tests that the caesar cipher works when given a shift value greater than 25'''
		clear_text = "Hello World!"
		cipher_text = caesar_cipher_encrypt(clear_text, 29)
		self.assertEqual(cipher_text, "KHOORZRUOG")

	def test_encrypt_with_negative_shift(self):
		'''Tests that the caesar cipher is implmented correctly if given a
		negative shift value, i.e. we want to shift the characters X place
		to the left.
		'''
		clear_text = "Hello world"
		self.assertEqual(caesar_cipher_encrypt(clear_text, -3), "EBIILTLOIA")

	def test_encrpyt_with_large_negative_shift(self):
		'''Tests that the if we give the caesar cipher function a shift
		less than -26 we still get the expected result
		'''
		clear_text = "Hello World"
		self.assertEqual(caesar_cipher_encrypt(clear_text, -29), "EBIILTLOIA")


class PlaintextRecogniserTest(TestCase):

	ptr = PlaintextRecogniser()

	def test_unigram_entropy(self):
		'''Simple bog standard test of relative entropy measurer'''
		clear_text = "THIS IS SOME SAMPLE TEXT HERE."
		result = self.ptr._measure_relative_unigram_entropy(clear_text, self.ptr.frequencies['letters'])
		self.assertAlmostEqual(result, 2.0202, places=4)

	def test_unigram_entropy_empty_string(self):
		'''Tests that if we give it an empty string it doesn't die '''
		clear_text = ""
		result = self.ptr._measure_relative_unigram_entropy(clear_text, self.ptr.frequencies['letters'])
		self.assertEqual(result, 0.0)

class CrackingCaesarCipherTest(TestCase):

	def test_crack_rot13(self):
		clear_text = "This is some sample text here."
		shift, decryption = crack_caesar_cipher(rot13(clear_text))
		self.assertEqual(shift, 13)
		self.assertEqual(decryption, "THISISSOMESAMPLETEXTHERE")

	def test_crack_caesar_cipher(self):
		clear_text = "Mr. Obama, seeking to address an outcry."
		shift, decryption = crack_caesar_cipher(caesar_cipher_encrypt(clear_text, 16))
		self.assertEqual(shift, 16)
		self.assertEqual(decryption, decrypted_text(clear_text))

	def test_crack_long_string(self):
		clear_text = "Mr. Obama, seeking to address an outcry that has shaken public confidence in \
		the new health law, told reporters at the White House that the changes should allow most people\
		to retain."
		shift, decryption = crack_caesar_cipher(caesar_cipher_encrypt(clear_text, 5))
		self.assertEqual(shift, 5)
		self.assertEqual(decryption, decrypted_text(clear_text))

def decrypted_text(clear_text):
	'''Were we to decrpyt encrpyted text we would expect
	all the puncuation to be removed and all the characters
	to be uppercase.
	'''
	unencrypted_clear_text = ""
	for c in clear_text.upper():
		if c.isupper():
			unencrypted_clear_text += c
	return unencrypted_clear_text	

