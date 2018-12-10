from corpus import Corpus
import pandas as pd
import scattertext as st
import spacy
from spacy.lang.es.stop_words import STOP_WORDS

STOP_WORDS.add('de+el')
STOP_WORDS.add('a+el')
nlp = spacy.load('es')

def create_corpus(category, speeches_df):
    corpus = st.CorpusFromPandas(speeches_df, category_col=category, text_col='text', nlp=nlp).build()
    update_stop = []
    for term in STOP_WORDS:
        if term in corpus._term_idx_store:
            update_stop.append(term)
    corpus = corpus.remove_terms(update_stop)
    return corpus

def print_graph(corpus, speeches_df, category, type, not_type):
    html = st.produce_scattertext_explorer(corpus, category=type, category_name=type, not_category_name=not_type, width_in_pixels=1000, metadata=speeches_df[category])
    open("./graphs/visualization_" + type + ".html", 'wb').write(html.encode('utf-8'))

def get_type_list(category, speeches_dict):
    values = []
    for dict in speeches_dict:
        value = dict.get(category)
        values.append(value)
    return list(set(values))

def get_visualization(category, my_corpus):
    speeches_dict = my_corpus.to_speeches_list()
    speeches_df = pd.DataFrame(speeches_dict)
    visual_corpus = create_corpus(category, speeches_df)
    types = get_type_list(category, speeches_dict)
    if(len(types) == 2):
        print_graph(visual_corpus, speeches_df, category, types[0], types[1])
    else:
        for type in types:
            print_graph(visual_corpus, speeches_df, category, type, "Not " + type)

if __name__ == '__main__':

    my_corpus = Corpus([])
    categories = ['period', 'king', 'half']
    for category in categories:
        get_visualization(category, my_corpus)



