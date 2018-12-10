import markovify
from corpus import Corpus
import re

def get_training_text(corpus, from_paragraph, to_paragraph):
    training_text = ""
    opening_par = []
    for key, speech in corpus.speeches.items():
        opening_par.append(speech.par[from_paragraph:to_paragraph])
    for par in opening_par:
        for sent in par:
            for chain in sent:
                #print(chain)
                clean_chain = [element for element in chain if element != u'\u200b']
                clean_sentence = " ".join(clean_chain)
                clean_sentence = re.sub(r' ([,;\.])',r'\1', clean_sentence)
                training_text = clean_sentence + " " + training_text
    return training_text

def get_markovian_text(training_text, n):
    text_model = markovify.Text(training_text)
    my_string = ""
    for n in range(n):
        my_string = text_model.make_short_sentence(140, tries=200) + " " + text_model.make_sentence(tries=200) + " " + my_string
    return my_string

corpus = Corpus([])
training_opening = get_training_text(corpus, 0, 2)
training_body = get_training_text(corpus, 2, -4)
training_end = get_training_text(corpus, -4, -1)

markovian_speech =  get_markovian_text(training_opening , 2) + "\n" + get_markovian_text(training_body , 6) + "\n" + get_markovian_text(training_end , 3)

print(markovian_speech)



