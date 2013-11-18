
def rot13(clear_text):
    '''ROT13 encryption - Caesar Cipher shifted by 13'''
    return encrypt(clear_text, 13)

def encrypt(clear_text, shift):
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

def decrypt(cipher_text, shift):
    '''Decrpyts the string given the correct decryption shift'''
    result = ""
    for c in cipher_text:
        result += chr(((ord(c) - shift - 65) % 26) +  65)
    return result