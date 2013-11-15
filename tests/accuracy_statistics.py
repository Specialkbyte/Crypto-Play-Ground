import cPickle
from collections import defaultdict
from project import crack_caesar_cipher, caesar_cipher_encrypt

class AccuracyStatistics(object):

    def word_accuracy(self, filename):
        '''Takes a list of words encrpyts them and then attempts to 
        break the encryption. Using single words as the corpus is 
        very small.
        '''
        self._words = open('tests/' + filename)

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
        '''Generates printable statistics on the strings that were 
        cracker successfully and strings that aren't
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
        print "Success rate per string length"
        success_freq = self._frequency_string_length(successes)
        failure_freq = self._frequency_string_length(failures)

        for i in range(2, 50): 
            success_rate = (success_freq[i] / (float(success_freq[i]+failure_freq[i]) or 1.0)) * 100
            print "%d: %.2f%% (%d/%d)" % (i, success_rate, success_freq[i], success_freq[i]+failure_freq[i])

    def _frequency_string_length(self, strings):
        '''Gives the an aggregate list of how many strings
        have each character length for the list of strings provided
        '''
        freq = defaultdict(int)
        for string in strings:
            freq[len(string)] += 1
        return freq
