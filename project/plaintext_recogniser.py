import json
import math

class PlaintextRecogniser(object):

    frequencies = {} # dictionary of frequency statistics for a given language

    def __init__(self, language='EN'):
        if language == 'EN':
            self._get_frequency_data('project/frequencies.json') # TODO: tidy this shit up
        else:
            raise Exception("Unknown language - we have no frequency data on that language")

    def measure_similarity(self, clear_text):
        unigrams = self._measure_relative_unigram_entropy(clear_text, self.frequencies['letters'])
        digraphs = self._measure_relative_digraph_entropy(clear_text, self.frequencies['digraphs'])

        return unigrams + digraphs

    def _measure_relative_unigram_entropy(self, clear_text, letter_frequencies):
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

    def _measure_relative_digraph_entropy(self, clear_text, diagraph_frequencies):
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
                pass # we have no data on this possible diagraph - ignore

        return sum_ / math.log(2) / len(clear_text) # bits of entropy per character

    def _get_frequency_data(self, filename):
        '''Loads in the letter/diagram/etc. frequency data from
        the JSON file into the class

        Returns: None
        '''
        # get the frequencies data loaded in from the JSON file
        json_data = open(filename)
        self.frequencies = json.load(json_data)
        json_data.close()

