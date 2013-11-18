from caesar_cipher import encrypt as cc_encrypt
from caesar_cipher import decrypt as cc_decrypt
from plaintext_recogniser import PlaintextRecogniser

def crack_caesar_cipher(cipher_text):
    '''Attempts to decrypt the given caesar cipher text by generating all
    26 possible shifts and then using letter frequency analysis distributions
    to predict which of the possible 26 combinations was the correct decrpytion.
    
    Returns:
        Tuple: (shift value, clear text)
    '''
    ptr = PlaintextRecogniser()
    decryptions = []

    # try all 26 possible shifts and calculate the relative entropy for each string to standard english language
    for shift in range(26):
        possible_clear_text = cc_decrypt(cipher_text, shift)
        entropy = ptr.measure_similarity(possible_clear_text)
        decryptions.append((shift, entropy, possible_clear_text))

    sorted_by_entropy = sorted(decryptions, key=lambda tup: tup[1], reverse=True)

    shift, _, entropy = sorted_by_entropy[0]
    return (shift, entropy)
