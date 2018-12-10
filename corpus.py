from speech import Speech
import nltk
from nltk.corpus import PlaintextCorpusReader
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

    def to_speeches_list(self):
        speeches_list = []
        for key,speech in self.speeches.items():
            speeches_list.append(speech.speech_to_dict())
        return speeches_list

    def printGraph(self, my_words):
        cfd = nltk.ConditionalFreqDist((target, fileid) for fileid in self.speeches.keys() for w in self.speeches[fileid].tokens for target in my_words if w.lower() == target)
        cfd.plot()


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
    corpus_trasition = create_corpus(1975, 1981)
    corpus_socialism = create_corpus(1982, 1995)
    corpus_bubble = create_corpus(1996, 2008)
    corpus_recession = create_corpus(2009, 2017)
    print(corpus_trasition.speech.frequencies())
    print(corpus_trasition.speech.frequency('noche'))
    print(corpus_trasition.speech.hapaxes())
    print(corpus_trasition.speech.most_frequent_bigrams())
    print(corpus_socialism.speech.most_frequent_bigrams())
    print(corpus_bubble.speech.most_frequent_bigrams())
    print(corpus_recession.speech.most_frequent_bigrams())


    #print(my_corpus_transicion.speech.most_frequent_trigrams())
    #print(my_corpus_transicion.speech.most_frequent_bigrams())
    #print(my_corpus_transicion.speech.concordance('patria'))
    #print(my_corpus_transicion.speech.similar('España'))
    #print(my_corpus_transicion.speech.most_frequent_content_words())
"""
    my_corpus = Corpus([])
    print(my_corpus.speech.concordance('Generalísimo'))
    print(my_corpus.speech.most_frequent_trigrams())
    print(my_corpus.speech.most_frequent_bigrams())
    print(my_corpus.speech.concordance('patria'))
    most_freq_tuples = (my_corpus.speech.most_frequent_content_words())
    #print(most_freq_tuples)
    my_corpus.printGraph(['españa', 'democracia'])

    my_corpus.speech.text.dispersion_plot(["España", "Europa", "terrorismo", "Dios"])
"""

