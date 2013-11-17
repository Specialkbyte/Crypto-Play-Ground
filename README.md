Caesar Cipher Cracker in Python
===============================

Project made for fun. I always wanted to learn how hard is it to actually do letter frequency analysis to break a simple mono-alphabetic substitution cipher like the Caesar Cipher.

I ended up brute forcing my way to the solution and then used a simple Plaintext Recogniser to find the correct decryption given different shift values.

The simple Plaintext Recogniser used unigram and digrams frequency analysis for the English langauge to choose the right plaintext

## Performance
I ran the program over the 220,000 standard unix text dictionary and big.txt, which is all the Sherlock Homes novels in one file.

For the 220,000 word dictionary:

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
| 20+ | >98.00% |

For big.txt, all the Sherlock Homes novels. This is long form English sentences.

| String Length | Accuracy |
| ------------- | -------: |
| 5-9 | 28.00% | 
| 10-14 | 58.66% |
| 15-19 | 60.29% |
| 20-24 | 71.74% |
| 25-29 | 91.04% |
| 30-34 | 94.73% |
| 35-39 | 97.56% |
| 40-44 | 98.70% |
| 45-50 | 100% |

## Hopes
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