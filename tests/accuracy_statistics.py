import cPickle
from collections import defaultdict
from project import crack_caesar_cipher, caesar_cipher_encrypt

class AccuracyStatistics(object):

    def word_accuracy(self):
        '''Takes a list of words encrpyts them and then attempts to 
        break the encryption. Using single words as the corpus is 
        very small.
        '''
        self._words = open('/usr/share/dict/words')

        failures = []
        successes = []

        # encrypt every word with the caesar cipher and attempt to crack it
        for word in self._words:
            shift, _, decryption = crack_caesar_cipher(caesar_cipher_encrypt(word, 5))
            if shift is 5:
                successes.append(word)
            else:
                failures.append(word)

        cPickle.dump(successes, open('successes.p', 'wb')) 
        cPickle.dump(failures, open('failures.p', 'wb')) 

    def statistics(self):
        '''Generates printable statistics on the words that were 
        cracker successfully and words that aren't
        '''
        # build statistics from the previous tests
        successes = cPickle.load(open('successes.p', 'rb')) 
        failures = cPickle.load(open('failures.p', 'rb')) 

        num_sucs = len(successes)
        num_fails = len(failures)
        num_total = num_sucs + num_fails
        success_rate = num_sucs/float(num_total)*100
        print "Success Rate: %.2f%%" % success_rate

        # per success rate for each word length
        print "Success rate per word length"
        success_freq = self._frequency_word_length(successes)
        failure_freq = self._frequency_word_length(failures)

        for i in range(2, 24): 
            success_rate = (success_freq[i] / float(success_freq[i]+failure_freq[i])) * 100
            print "%d: %.2f%%" % (i, success_rate)

    def _frequency_word_length(self, words):
        '''Gives the an aggregate list of how many words
        have each word length for the list of words provided
        '''
        freq = defaultdict(int)
        for word in words:
            freq[len(word)] += 1
        return freq
