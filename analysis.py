#! /usr/bin/env python3
"""


"""
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
# import collections
from collections import Counter
from nltk.collocations import ngrams
from nltk.text import Text
import numpy
import matplotlib

STOPWORDS_SET = set(stopwords.words('spanish'))
STOPWORDS_SET.add('cada')

class Corpus(object):

    def __init__(self, data_root):
        self.location = data_root
        self.corpus = PlaintextCorpusReader(data_root, '.*')
        self.words = self.corpus.words()
        self.content_words = [word.lower() for word in self.words if word.isalpha() and word.lower() not in STOPWORDS_SET]
        self.bigrams = list(nltk.bigrams(self.corpus.words()))
        self.content_bigrams = [(x, y) for (x, y) in self.bigrams if x.isalpha() and x.lower() not in STOPWORDS_SET and y.isalpha() and y.lower() not in STOPWORDS_SET]
        self.trigrams = ngrams(self.words,3)
        self.content_trigrams = [(x, y, z) for (x, y, z) in self.trigrams if x.isalpha() and x.lower() not in STOPWORDS_SET and y.isalpha() and z.isalpha() and z.lower() not in STOPWORDS_SET]

    def word_appearances(self, word):
        return Counter(words.lower() for words in self.words)[word]

    def documents(self):
        """Return a list of all documents in the corpus."""
        return self.corpus.fileids()

    def longest_words(self):
        """Return an alphabetized list of the longest word(s) in this corpus."""
        longest_len = max(len(word) for word in self.words)
        longest_list = [word for word in set(self.words) if len(word) == longest_len]
        longest_list.sort()
        return longest_list
    '''
    def words_in_file(self, filename):
        """Given a file name as input, return a list of tokenized words."""
        return self.corpus.words(filename)

    def sentences_in_file(self, filename):
        """Given a file name as input, return a list of sentences.""" 
        return nltk.tokenize.sent_tokenize(self.corpus.raw(filename))

    def tokenized_sentences_in_file(self, filename):
        """Given a file name as input, return a list of word tokenized sentences 
        (each sentence is a list of tokens)."""
        return self.corpus.sents(filename)
    '''
    def most_frequent_content_words(self):
        """Return a list with the 25 most frequent content words and their 
        frequencies. The list should have (word, frequency) pairs and be ordered 
        on the frequency. You should use the stop word list in nltk.corpus.words 
        in your definition of what a content word is."""
        freqdist = nltk.FreqDist(self.content_words)
        return freqdist.most_common()

    def most_frequent_bigrams(self):
        """Return a list with the 25 most frequent bigrams that only contain
        content words. The list returned should have pairs where the first 
        element in the pair is the bigram and the second the frequency, as in 
        ((word1, word2), frequency), these should be ordered on frequency."""
        freqdist = nltk.FreqDist(self.content_bigrams)
        return freqdist.most_common()

    def most_frequent_trigrams(self):
        """Return a list with the 25 most frequent bigrams that only contain
        content words. The list returned should have pairs where the first
        element in the pair is the bigram and the second the frequency, as in
        ((word1, word2), frequency), these should be ordered on frequency."""
        freqdist = nltk.FreqDist(self.content_trigrams)
        return freqdist.most_common()

    def concordances(self, word):
        """Return a list with the 25 most frequent bigrams that only contain
        content words. The list returned should have pairs where the first
        element in the pair is the bigram and the second the frequency, as in
        ((word1, word2), frequency), these should be ordered on frequency."""
        return self.concordance(word)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    corpus = Corpus('C:/Users/Elena/Documents/GitHub/orgulloysatisfaccion/discursos')
    cfd = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in corpus.corpus.fileids() for w in corpus.corpus.words(fileid) for target in ['europeo', 'terrorismo', 'dios', 'españoles','democracia', 'libertad', 'franco'] if w.lower().startswith(target))
    cfd.plot()

    print(corpus.documents())
    print(corpus.longest_words())
    print(corpus.most_frequent_content_words())
    print(corpus.most_frequent_bigrams())

