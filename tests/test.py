from mock import patch
from unittest import TestCase

from project import caesar_cipher
from project.main import letter_frequency_count

class CaesarCipherEncrpytTest(TestCase):

	def test_rot13(self):
		clear_text = "The brown fox jumped over the cow in the dark field."
		cipher_text = caesar_cipher(clear_text)
		self.assertEqual(cipher_text, "GUROEBJASBKWHZCRQBIREGURPBJVAGURQNEXSVRYQ")

	def test_communtivity(self):
		'''Tests that that if you do the caesar cipher is commutitive with uppercase strings'''
		clear_text = "Hello world! Goodbye world!"
		unencrypted_clear_text = ""
		for c in clear_text.upper():
			if c.isupper():
				unencrypted_clear_text += c
		self.assertEqual(unencrypted_clear_text, caesar_cipher(caesar_cipher(clear_text)))

	def test_encrpyt_with_custom_shift(self):
		'''Tests that you can do a caesar cipher with an arbitary shift value'''
		clear_text = "Hello world!"
		cipher_text = caesar_cipher(clear_text, 3)
		self.assertEqual(cipher_text, "KHOORZRUOG")

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


class LetterFrequncyCounterTest(TestCase):

	def test_count(self):
		result = letter_frequency_count("hello world, hello world helloo")
		expected_result = [('L', 8), ('O', 6), ('E', 3), ('H', 3), ('D', 2), ('R', 2), ('W', 2)]
		self.assertEqual(result, expected_result)