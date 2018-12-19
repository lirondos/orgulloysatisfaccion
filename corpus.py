from speech import Speech
import nltk
from nltk.corpus import PlaintextCorpusReader
import os
import numpy as np

import matplotlib.pyplot as plt

plt.style.use('_classic_test')

class Corpus:
    def __init__(self, files):
        if not files:
            self.corpus = PlaintextCorpusReader('./speeches', '.*')
        else:
            self.corpus = PlaintextCorpusReader('./speeches', files)
        self.speech = Speech(self.corpus.raw(), self.corpus.words(), self.corpus.sents(),self.corpus.paras(), None, None, None, None)
        self.speeches = build_speeches_dict(self.corpus)
        self.years = [int(year.split('.')[0]) for year in self.corpus.fileids()]
        complementary_years = list(set(os.listdir("./speeches")) - set([str(years) + '.txt' for years in self.years]))
        if not files:
            self.complementary = None
            self.unique_words = None
        else:
            self.complementary = Complementary_Corpus(complementary_years)
            self.unique_words = [word for word in self.speech.tokens if word not in self.complementary.speech.tokens]


    def to_speeches_list(self):
        speeches_list = []
        for key,speech in self.speeches.items():
            speeches_list.append(speech.speech_to_dict())
        return speeches_list

    def printGraph(self, my_words):
        cfd = nltk.ConditionalFreqDist((target, fileid) for fileid in self.speeches.keys() for w in self.speeches[fileid].tokens for target in my_words if w.lower() == target)
        cfd.plot()

    def get_files(self):
        return self.corpus.fileids()

    def unique_words_freq(self):
        if self.unique_words is None:
            return "The corpus contains all speeches, so no comparison can be made"
        else:
            return nltk.FreqDist(self.unique_words).most_common()

    def unique_bigrams(self):
        return list(set(self.speech.bigrams()) - set(self.complementary.speech.bigrams()))

    def radiography(self):
        print("Lexical data for period from " + str(self.years[0]) + " to " + str(self.years[-1]))
        print(str(len(self.years)) + " total speeches")
        print(str(len(self.corpus.words())) + " total words")
        print(str(len(self.corpus.words()) / len(self.get_files())) + " words per speech")
        print("Frequency distribution:")
        print(self.speech.frequencies())
        print("Content words frequency distribution:")
        print(self.speech.most_frequent_content_words())
        print("Hapaxes:")
        print(self.speech.hapaxes())
        print("Unique words frequency distribution:")
        print(self.unique_words_freq())
        print("Most frequent content bigrams:")
        print(self.speech.most_frequent_bigrams())
        print("Most frequent content trigrams:")
        print(self.speech.most_frequent_trigrams())
        print("#######################################")





class Complementary_Corpus(Corpus):
    def __init__(self, files):
        Corpus.corpus = PlaintextCorpusReader('./speeches', files)
        Corpus.speech = Speech(self.corpus.raw(), self.corpus.words(), self.corpus.sents(), self.corpus.paras(), None, None, None, None)
        Corpus.speeches = None
        Corpus.years = [int(year.split('.')[0]) for year in self.corpus.fileids()]
        #print(sorted(Corpus.speech.types))
        Corpus.complementary = None


def build_speeches_dict(corpus):
    speeches = dict()
    for fileid in corpus.fileids():
        text = corpus.raw(fileid)
        words = corpus.words(fileid)
        sents = corpus.sents(fileid)
        par = corpus.paras(fileid)
        year = int(fileid.split('.')[0])
        king = get_king(year)
        half = get_half(year)
        period = get_period(year)
        my_speech = Speech(text, words, sents, par, year, king, half, period)
        speeches[year] = my_speech
    return speeches


def get_king(year):
    if (year < 2014):
        return "Juan Carlos"
    else:
        return "Felipe"

def get_half(year):
    if (year < 1996):
        return "1"
    else:
        return "2"

def get_period(year):
    if year < 1982:
        return "Transition"
    elif (year>=1982 and year<1996):
        return "Socialism"
    elif(year >= 1996 and year < 2008):
        return "Bubble"
    elif(year>=2008):
        return "Recession"

def create_corpus(first_year, last_year):
    files = []
    for year in range(first_year, last_year + 1):
        file_name = str(year) + '.txt'
        files.append(file_name)
    corpus = Corpus(files)
    return corpus



if __name__ == '__main__':
    general = Corpus([])
    general.radiography()

    my_corpora = [create_corpus(1975, 1981), create_corpus(1982, 1995), create_corpus(1996, 2008), create_corpus(2009, 2017)]
    for corpus in my_corpora:
        corpus.radiography()




