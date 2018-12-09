import pandas as pd
import os
from os import listdir
from os.path import isfile, join
import nltk
from nltk.corpus import PlaintextCorpusReader
import scattertext as st
import spacy
from pprint import pprint
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

def get_king_from_year(year):
    if(year<2014):
        return "Juan Carlos"
    else:
        return "Felipe"

def get_half_from_year(year):
    if (year < 1996):
        return "1"
    else:
        return "2"

def get_period_from_year(year):
    if year < 1982:
        return "Transition"
    elif (year>=1982 and year<1996):
        return "Socialism"
    elif(year >= 1996 and year < 2008):
        return "Bubble"
    elif(year>=2008):
        return "Recession"

def get_speech_text(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def get_speech_length(speeches_path, year):
    my_corpus = nltk.corpus.PlaintextCorpusReader(speeches_path, str(year) + '\.txt')
    return len(my_corpus.words())

def create_corpus(category):
    corpus = st.CorpusFromPandas(speeches_df, category_col=category, text_col='text', nlp=nlp).build()
    update_stop = []
    for term in STOP_WORDS:
        if term in corpus._term_idx_store:
            update_stop.append(term)
    corpus = corpus.remove_terms(update_stop)
    return corpus

def get_relevant_words(corpus, category, selection, number):
    term_freq_df = corpus.get_term_freq_df()
    term_freq_df[category] = corpus.get_scaled_f_scores(selection)
    pprint(list(term_freq_df.sort_values(by=category, ascending=False).index[:number]))

def print_graph(corpus, category, type, not_type):
    html = st.produce_scattertext_explorer(corpus, category=type, category_name=type, not_category_name=not_type, width_in_pixels=1000, metadata=speeches_df[category])
    open("Visualization_" + type + ".html", 'wb').write(html.encode('utf-8'))


speeches_path = "C:/Users/Elena/Documents/GitHub/orgulloysatisfaccion/discursos"
# Get raw text as string.
speeches = [f for f in listdir(speeches_path) if isfile(join(speeches_path, f))]
speeches_list = []
for speech in speeches:
    path = speeches_path+"/"+ speech
    year = int(os.path.splitext(speech)[0])
    my_speech = dict()
    my_speech['year'] = year
    my_speech['king'] = get_king_from_year(year)
    my_speech['half'] = get_half_from_year(year)
    my_speech['period'] = get_period_from_year(year)
    my_speech['length'] = get_speech_length(speeches_path, year)
    my_speech['text'] = get_speech_text(path)
    speeches_list.append(my_speech)

speeches_df = pd.DataFrame(speeches_list)
# print(speeches_df.iloc[0])
nlp = spacy.load('es')
# king
"""
corpus = create_corpus('king')

print(list(corpus.get_scaled_f_scores_vs_background().index[:20]))
term_freq_df = corpus.get_term_freq_df()
term_freq_df['king'] = corpus.get_scaled_f_scores('Felipe')
pprint(list(term_freq_df.sort_values(by='king', ascending=False).index[:10]))
"""
"""
# period
corpus = create_corpus('period')
get_relevant_words(corpus, 'period', 'Transition', 20)
print_graph(corpus, 'period', 'Transition')
"""

categories = {"king":["Juan Carlos", "Felipe"], "half":["1", "2"], "period":["Transition", "Socialism", "Bubble", "Recession"]}
for category in categories.keys():
    corpus = create_corpus(category)
    types = categories.get(category)
    if(len(types) == 2):
        # get_relevant_words(corpus, category, type, 20)
        print_graph(corpus, category, types[0], types[1])
    else:
        for type in types:
            #get_relevant_words(corpus, category, type, 20)
            print_graph(corpus, category, type, "Not " + type)

"""
# print
html = st.produce_scattertext_explorer(corpus, category='Transition', category_name='Transition', not_category_name='Not Transition', width_in_pixels=1000, metadata=speeches_df['period'])

open("Visualization.html", 'wb').write(html.encode('utf-8'))
"""
