from mock import patch
from unittest import TestCase

from project import caesar_cipher
from project import crack_caesar_cipher
from project.main import _measure_relative_entropy
from project.main import _get_frequency_data

class CaesarCipherEncrpytTest(TestCase):

	def test_rot13(self):
		clear_text = "The brown fox jumped over the cow in the dark field."
		cipher_text = caesar_cipher(clear_text)
		self.assertEqual(cipher_text, "GUROEBJASBKWHZCRQBIREGURPBJVAGURQNEXSVRYQ")

	def test_communtivity(self):
		'''Tests that that if you do the caesar cipher is commutitive with uppercase strings'''
		clear_text = "Hello world! Goodbye world!"
		self.assertEqual(decrypted_text(clear_text), caesar_cipher(caesar_cipher(clear_text)))

	def test_encrpyt_with_custom_shift(self):
		'''Tests that you can do a caesar cipher with an arbitary shift value'''
		clear_text = "Hello world!"
		cipher_text = caesar_cipher(clear_text, 3)
		self.assertEqual(cipher_text, "KHOORZRUOG")

	def test_encrpyt_with_custom_shift(self):
		'''Tests that you can do a caesar cipher with an arbitary shift value'''
		clear_text = "Hello world!"
		cipher_text = caesar_cipher(clear_text, 5)
		self.assertEqual(cipher_text, "MJQQTBTWQI")

	def test_encrpyt_with_large_shift(self):
		'''Tests that the caesar cipher works when given a shift value greater than 25'''
		clear_text = "Hello World!"
		cipher_text = caesar_cipher(clear_text, 29)
		self.assertEqual(cipher_text, "KHOORZRUOG")

	def test_encrypt_with_negative_shift(self):
		'''Tests that the caesar cipher is implmented correctly if given a
		negative shift value, i.e. we want to shift the characters X place
		to the left.
		'''
		clear_text = "Hello world"
		self.assertEqual(caesar_cipher(clear_text, -3), "EBIILTLOIA")

	def test_encrpyt_with_large_negative_shift(self):
		'''Tests that the if we give the caesar cipher function a shift
		less than -26 we still get the expected result
		'''
		clear_text = "Hello World"
		self.assertEqual(caesar_cipher(clear_text, -29), "EBIILTLOIA")


class MeasureRelativeEntropyTest(TestCase):

	def setUp(self):
		'''Load in the letter frequency data from the JSON file'''
		self.frequencies = _get_frequency_data('project/frequencies.json')

	def test_measure(self):
		'''Simple bog standard test'''
		clear_text = "THIS IS SOME SAMPLE TEXT HERE."
		result = _measure_relative_entropy(clear_text, self.frequencies)
		self.assertAlmostEqual(result, 2.0202, places=4)

class CrackingCaesarCipherTest(TestCase):

	def test_crack(self):
		clear_text = "This is some sample text here."
		shift, _, decryption = crack_caesar_cipher(caesar_cipher(clear_text))
		self.assertEqual(shift, 13)
		self.assertEqual(decryption, "THISISSOMESAMPLETEXTHERE")

	def test_crack_custom_shift(self):
		clear_text = "Mr. Obama, seeking to address an outcry."
		shift, _, decryption = crack_caesar_cipher(caesar_cipher(clear_text, 16))
		self.assertEqual(shift, 16)
		self.assertEqual(decryption, decrypted_text(clear_text))

	def test_crack_long_string(self):
		clear_text = "Mr. Obama, seeking to address an outcry that has shaken public confidence in \
		the new health law, told reporters at the White House that the changes should allow most people\
		to retain their health care plans for a year despite having received letters saying they could no \
		longer keep their insurance."
		shift, _, decryption = crack_caesar_cipher(caesar_cipher(clear_text, 5))
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

