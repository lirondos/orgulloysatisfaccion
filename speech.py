import nltk
import spacy
# from es_lemmatizer import lemmatize
from nltk.collocations import ngrams
from spacy.lang.es.stop_words import STOP_WORDS

STOP_WORDS.add('a')
STOP_WORDS.add('y')
STOP_WORDS.add('e')
STOP_WORDS.add('o')
STOP_WORDS.add('que')
STOP_WORDS.add('el')
STOP_WORDS.add('la')
STOP_WORDS.add('nos')
STOP_WORDS.add('todos')
STOP_WORDS.add('hemos')
STOP_WORDS.add('estos')
STOP_WORDS.add('pero')
STOP_WORDS.add('cuando')
STOP_WORDS.add('otro')
STOP_WORDS.add('dentro')
STOP_WORDS.add('he')
STOP_WORDS.add('cada')
STOP_WORDS.add('tal')
STOP_WORDS.add('cuyo')
STOP_WORDS.add('cuya')


nlp = spacy.load('es', disable=['parser', 'ner'])
# nlp.add_pipe(lemmatize, after="tagger")


class Speech:
    def __init__(self, text, words, sents, par, year, king, half, period):
        self.raw_text = text
        self.tokens = words
        self.sents = sents
        self.par = par
        #self.lemmatized_text, self.tagged_text = lemmatize_tag_text(text)
        self.text = nltk.Text(words)
        self.year = year
        self.king = king
        self.half = half
        self.period = period

    def word_appearances(self, word):
        return self.tokens.count(word)

    def length(self):
        return len(self.text.tokens)

    def concordance(self, word):
        return self.text.concordance(word)

    def similar(self, word):
        return self.text.similar(word)
    
    def content_words(self):
       return [word.lower() for word in self.tokens if word.isalpha() and word.lower() not in STOP_WORDS]

    def bigrams(self):
        return list(nltk.bigrams(self.tokens))
    
    def content_bigrams(self):
        bigrams = self.bigrams()
        return [(x, y) for (x, y) in bigrams if x.isalpha() and x.lower() not in STOP_WORDS and y.isalpha() and y.lower() not in STOP_WORDS]

    def trigrams(self):
        return ngrams(self.tokens, 3)
        
    def content_trigrams(self):
        trigrams = self.trigrams()
        return [(x, y, z) for (x, y, z) in trigrams if
                                 x.isalpha() and x.lower() not in STOP_WORDS and y.isalpha() and z.isalpha() and z.lower() not in STOP_WORDS]

    def longest_words(self):
        """Return an alphabetized list of the longest word(s) in this corpus."""
        longest_len = max(len(word) for word in self.tokens)
        longest_list = [word for word in set(self.tokens) if len(word) == longest_len]
        longest_list.sort()
        return longest_list

    def most_frequent_content_words(self):
        """Return a list with the 25 most frequent content words and their
        frequencies. The list should have (word, frequency) pairs and be ordered
        on the frequency. You should use the stop word list in nltk.corpus.words
        in your definition of what a content word is."""
        content_words = self.content_words()
        freqdist = nltk.FreqDist(content_words)
        return freqdist.most_common()

    def most_frequent_bigrams(self):
        """Return a list with the 25 most frequent bigrams that only contain
        content words. The list returned should have pairs where the first
        element in the pair is the bigram and the second the frequency, as in
        ((word1, word2), frequency), these should be ordered on frequency."""
        content_bigrams = self.content_bigrams()
        freqdist = nltk.FreqDist(content_bigrams)
        return freqdist.most_common()

    def most_frequent_trigrams(self):
        """Return a list with the 25 most frequent bigrams that only contain
        content words. The list returned should have pairs where the first
        element in the pair is the bigram and the second the frequency, as in
        ((word1, word2), frequency), these should be ordered on frequency."""
        content_trigrams = self.content_trigrams()
        freqdist = nltk.FreqDist(content_trigrams)
        return freqdist.most_common()

    def dispersion_plot(self, my_words):
        self.text.dispersion_plot(my_words)

    def frequencies(self):
        fd = nltk.FreqDist(self.text)
        return fd.most_common(50)

    def frequency(self, word):
        fd = nltk.FreqDist(self.text)
        return fd[word]

    def hapaxes(self):
        fd = nltk.FreqDist(self.text)
        return fd.hapaxes()

    def speech_to_dict(self):
        speech_dict = dict()
        speech_dict['year'] = self.year
        speech_dict['half'] = self.half
        speech_dict['king'] = self.king
        speech_dict['period'] = self.period
        speech_dict['text'] = self.raw_text
        return speech_dict



def lemmatize_tag_text(text):
    doc = nlp(text.encode('utf-8').decode('utf-8'))
    lemmas = [token.lemma_ for token in doc]
    tagged_words = [token.text + '/' + token.pos_ for token in doc]
    lemmatized_text = str(" ".join(lemmas))
    tagged_text = " ".join(tagged_words)
    return lemmatized_text, tagged_text


def get_tokens(text):
    tokens = nltk.word_tokenize(text)
    return tokens
