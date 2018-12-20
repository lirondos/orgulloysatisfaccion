# Orgullo y satisfacción
A corpus with the king's Christmas speech. 

For otivations, technical details, etc please see the project report. 

This project consists of: 
* A crawler.py script. This was the script that was used to extract the speeches from http://www.casareal.es. The URLs of the speeches are in this file. Please, note that this process took several tries and was humanly supervised (due to timeout errors from the server and to label each speech with its corresponding year).
* A Corpus class that creates the corpus object that contains the speeches to be analyzed. This class uses the txt files inside the speeches folder. This file also contain the methods to perform the lexical analysis of the created corpus. An example of output of this lexical analysis can be found inside the output.txt file.
* A Speech class that creates the object Speech with the information for a given speech.
* A visualize.py script that creates interactive HTML visualization using TF-IDF measures. The visualization files are stored inside the visualization folder.
* A markov.py script that generates random speeches automatically.

The files that have a main method than can be executed are: 
* corpus.py (creates several corpus objects for different time periods of time and calls the radiography method in order to get their lexical analysis)
* visualize.py (creates an instance of the corpus class and generates several visualization files with TF-IDF measures using the scattertext library)
* markov.py (creates an instance of the corpus class and generates randomly generated speeches following the markov chain).

This project requires the following libraries: 
* nltk
* spacy
* pandas
* scattertext
* markovify
* os
* re
* time
* newspaper
* matplotlib

The name of the GitHub project (_Orgullo y Satisfacción_, literally "Pride and satisfaction") is a humorous nod to the common belief (and even national joke)that  all  royal speeches contain the phrase _me llena de orgullo y satisfaccióon_ (which would translate to ”it is with great pride and satisfaction”).  
Fun fact: contrary to common belief, the phrase *orgullo y satisfacción appears only once in the entire corpus
