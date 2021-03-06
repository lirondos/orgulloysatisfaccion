# Orgullo y satisfacción
This project is a corpus analysis of the Christmas speeches delivered by the King of Spain from 1975 to 2018. It is built using `NLTK`, `spaCy`, `scattertext` and `markovify` libraries. This project was done for the course "Introduction to NLP in Python" at Brandeis University. 
 
For motivations, technical details, etc please see the project `report.pdf` file. 
- HTML visualizations available at: https://lirondos.github.io/orgulloysatisfaccion/ [in Spanish].
- For information about the traditional Christmas speech: https://en.wikipedia.org/wiki/Christmas_Eve_National_Speech.

This project contains the following files: 
* The `speeches` folder contains the files with the Christmas speeches from 1975 to 2018 in `txt` format.
* The `Speech` class creates the object Speech with the information for a given speech.
* The `Corpus` class creates the corpus object that contains the speeches to be analyzed. This class uses the files inside the `speeches` folder. This file also contain the methods to perform the lexical analysis of the created corpus. An example of output of this lexical analysis can be found inside the output.txt file.
* The `visualize.py` script creates interactive HTML visualization from TF-IDF measures using `scattertext` library. The visualization files are stored inside the visualization folder.
* The `markov.py` script generates random speeches automatically with markov models.
* The `crawler.py` script is the script that was used to extract the speeches from http://www.casareal.es. The URLs of the speeches are in this file. Please, note that this process took several tries and was humanly supervised (due to timeout errors from the server and to label each speech with its corresponding year).

The files that have a main method than can be executed are: 
* `corpus.py` (creates several corpus objects for different time periods of time and calls the radiography method in order to get their lexical analysis)
* `visualize.py` (creates an instance of the corpus class and generates several visualization files with TF-IDF measures using the scattertext library)
* `markov.py` (creates an instance of the corpus class and generates randomly generated speeches following the markov chain).

This project requires the following libraries: 
* `nltk`
* `spacy`
* `pandas`
* `scattertext`
* `markovify`
* `os`
* `re`
* `time`
* `newspaper`
* `matplotlib`

The name of the GitHub project (_Orgullo y Satisfacción_, literally "Pride and satisfaction") is a humorous nod to the common belief (and even national joke) that all royal speeches contain the phrase _me llena de orgullo y satisfacción_ (which would translate to ”it is with great pride and satisfaction”). 

Fun fact: contrary to common belief, the phrase _orgullo y satisfacción_ appears only once in the entire corpus
