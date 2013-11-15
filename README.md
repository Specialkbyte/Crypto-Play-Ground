Caesar Cipher Cracker in Python
===============================

Project made for fun to test out how easy is it really to do letter frequency analysis to break simple substitution ciphers like the Caesar Cipher, where the encryption is done by shifting every character left or right X places in the alphabet. My implemention of the Caesar Cipher removes all whitespace and puncuation.

## Performance
The cracker does a decent job with strings longer than 15 characters, but currently fails miserably with shorter strings or one word strings. I need to perform more tests so that I can have better numbers on how good this cracker is at picking the best solution.

## Hopes
I hope to improve the cracker's ability to pick the correct decryption by using diagrams and trigrams instead of just unigrams.

I hope to extend this project to also crack the "indecipherable cipher", the Vigenere Cipher.

## Developmennt & Testing
To install the development dependencies run:
```bash
pip install -r dev-requirements.txt
```

I've used the Python Nose testing framework for the tests. There are some tests in the tests directory. To run them run:
```bash
nosetests
```
in the root directory of the repository.