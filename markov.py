import markovify
from corpus import Corpus
import re
import time


def get_training_text(corpus, from_paragraph, to_paragraph):
    """
    This method takes a corpus object as parameter and extracts the sentences from the speeches in the corpus
    that will be used for training
    :param corpus:
    :param from_paragraph:
    :param to_paragraph:
    :return: training_text
    """
    training_text = ""
    opening_par = []
    for key, speech in corpus.speeches.items():
        opening_par.append(speech.par[from_paragraph:to_paragraph])
    for par in opening_par:
        for sent in par:
            for chain in sent:
                clean_chain = [element for element in chain if element != u'\u200b']
                clean_sentence = " ".join(clean_chain)
                clean_sentence = re.sub(r' ([,:;\.])',r'\1', clean_sentence)
                training_text = clean_sentence + " " + training_text
    return training_text

def get_markovian_text(training_text, n):
    """
    This method takes the training text and creates a concatenation of short and long automatically generated
    sentences in order to create a speech. The number of short and long alternations is parameter n.
    :param training_text:
    :param n:
    :return: markovian speech
    """
    text_model = markovify.Text(training_text)
    my_string = ""
    for n in range(n):
        my_string = text_model.make_short_sentence(140, tries=200) + " " + text_model.make_sentence(tries=200) + " " + my_string
    return my_string

def save(markovian_speech):
    """
    Saves the created speech inside the markovian_speeches folder
    :param markovian_speech:
    """
    my_file = open('./markovian_speeches/speech' + "_" + str(time.time()) + '.txt', 'w', encoding='utf-8')
    my_file.write(markovian_speech)
    my_file.close()

if __name__ == '__main__':
    """
    This main method creates a corpus object with all the speeches. 
    It then trains:
     - opening sentences using only the first two paragraphs.
     - body sentences using paragraphs from the second paragraph until the forth to last
     - ending sentences using four final paragraphs
     
     The automatic speech is then generated with the training material and saved as a file in the markovian_speeches folder.
    """
    corpus = Corpus([])
    training_opening = get_training_text(corpus, 0, 2)
    training_body = get_training_text(corpus, 2, -4)
    training_end = get_training_text(corpus, -4, -1)

    markovian_speech =  get_markovian_text(training_opening , 2) + "\n\n" + get_markovian_text(training_body , 6) + "\n\n" + get_markovian_text(training_end , 3)

    save(markovian_speech)



