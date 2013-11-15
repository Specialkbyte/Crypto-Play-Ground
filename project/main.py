import json
import math
from collections import defaultdict

frequencies = None

def rot13(clear_text):
    '''ROT13 encryption - Caesar Cipher shifted by 13'''
    return caesar_cipher_encrypt(clear_text, 13)

def caesar_cipher_encrypt(clear_text, shift):
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

def caesar_cipher_decrypt(cipher_text, shift):
    '''Decrpyts the string given the correct decryption shift'''
    result = ""
    for c in cipher_text:
        result += chr(((ord(c) - shift - 65) % 26) +  65)
    return result

def crack_caesar_cipher(cipher_text):
    '''Attempts to decrypt the given caesar cipher text by generating all
    26 possible shifts and then using letter frequency analysis distributions
    to predict which of the possible 26 combinations was the correct decrpytion.
    '''
    frequency_data = _get_frequency_data('project/frequencies.json')
    decryptions = []

    # try all 26 possible shifts and calculate the relative entropy for each string
    for shift in range(26):
        possible_clear_text = caesar_cipher_decrypt(cipher_text, shift)
        entropy = measure_similarity(possible_clear_text, frequency_data)
        decryptions.append((shift, entropy, possible_clear_text))

    sorted_by_entropy = sorted(decryptions, key=lambda tup: tup[1], reverse=True)

    return sorted_by_entropy[0]

def measure_similarity(clear_text, frequencies):
    unigrams = measure_relative_unigram_entropy(clear_text, frequencies['letters'])
    diagraphs = measure_relative_diagraph_entropy(clear_text, frequencies['diagraphs'])

    return unigrams + diagraphs

def measure_relative_unigram_entropy(clear_text, letter_frequencies):
    '''This function measures the relative entropy (sometimes called the
    Kullback-Leibler divergence) of a string relative to the standard
    distribution of letters in the english language.
    '''
    if len(clear_text) is 0:
        return 0.0

    sum_ = 0.0
    for c in clear_text:
        if c.isupper():
            sum_ += math.log(letter_frequencies[c])

    return sum_ / math.log(2) / len(clear_text)

def measure_relative_diagraph_entropy(clear_text, diagraph_frequencies):
    '''Uses known common diagraph (two character pairs) in the english 
    language to better predict the correct crack
    '''
    sum_ = 0.0
    length = len(clear_text)
    if length is 0:
        return 0.0

    for i in range(0, length-2):
        try:
            diagraph = clear_text[i] + clear_text[i+1]
            sum_ += math.log(diagraph_frequencies[diagraph])
        except KeyError:
            pass # we have no data on this 

    return sum_ / math.log(2) / len(clear_text)

def _get_frequency_data(filename):
    '''Loads in the letter/diagram/etc. frequency data from
    the JSON file
    '''
    global frequencies

    if frequencies is None:
        # get the frequencies data loaded in from the JSON file
        json_data = open(filename)
        frequencies = json.load(json_data)
        json_data.close()
    return frequencies
