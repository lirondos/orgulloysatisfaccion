import markovify
from os import listdir
from os.path import isfile, join

discursos_path = "C:/Users/Elena/Documents/GitHub/orgulloysatisfaccion/discursos"
# Get raw text as string.
discursos = [f for f in listdir(discursos_path) if isfile(join(discursos_path, f))]
text = ""
for discurso in discursos:
    f = open(discursos_path+"/"+discurso, 'r', encoding='utf-8')
    text = text + f.read()
    f.close()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))