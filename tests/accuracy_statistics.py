import cPickle
from collections import defaultdict
from project.caesar_cipher import encrypt as caesar_cipher_encrypt
from project.crack_caesar_cipher import crack_caesar_cipher

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
            shift, decryption = crack_caesar_cipher(caesar_cipher_encrypt(word, 5))
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
        total_success_rate = num_sucs/float(num_total)*100
        print "General Success Rate: %.2f%%" % total_success_rate

        # per success rate for each word length
        print "Success rate per string length"
        success_freq = self._frequency_string_length(successes)
        failure_freq = self._frequency_string_length(failures)

        success_rates = []
        i = 0
        while i < len(success_freq):
            success_rate = success_freq[i]/(float(success_freq[i]+failure_freq[i]) or 1.0)
            success_rates.append(success_rate)
            i += 1

        for i in range(2, 250): 
            success_rate = success_rates[i]
            print "%d: %.2f%% (%d/%d)" % (i, success_rate*100, success_freq[i], success_freq[i]+failure_freq[i])

        # bullshit bdata bucketing
        aggregate_success = []
        bin_size = 5
        for i in range(0, 250, bin_size):
            sum_ = 0
            dp_count = 0 # number of non-zero data points for this bucket
            for j in range(i, i+(bin_size-1)):
                if success_rates[i] > 0.0:
                    sum_ += success_rates[i]
                    dp_count += 1
            avg = sum_ / (dp_count or 1.0)
            aggregate_success.append((i, avg))
            print (i, avg)

    def _frequency_string_length(self, strings):
        '''Gives the an aggregate list of how many strings
        have each character length for the list of strings provided
        '''
        freq = defaultdict(int)
        for string in strings:
            freq[len(string)] += 1
        return freq
