Caesar Cipher Cracker in Python
===============================

Project made for fun to test out how easy is it really to do letter frequency analysis to break simple substitution ciphers like the Caesar Cipher, where the encryption is done by shifting every character left or right X places in the alphabet. My implemention of the Caesar Cipher removes all whitespace and puncuation.

## Performance
Using the simple single word dictionary containing over 220,000 words the program currently cracks correctly the first time depending on how much cipher text there is to work with. The longer the cleartext the better it works:

| String Length | Accuracy |
| ------------- | -------: |
| 2 | 3.85% |
| 3 | 10.62% | 
| 4 | 13.66% |
| 5 | 22.21% |
| 6 | 30.76% |
| 7 | 42.57% |
| 8 | 51.42% |
| 9 | 60.69% |
| 10 | 68.60% |
| 11 | 74.50% |
| 12 | 80.64% |
| 13 | 84.68% |
| 14 | 88.43% |
| 15 | 91.20% |
| 16 | 93.16% |
| 17 | 94.34% | 
| 18 | 95.75% |
| 19 | 97.03% |
| 20 | 97.66% |
| 21 | 98.99% |
| 22 | 92.68% |
| 23 | 97.56% |

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