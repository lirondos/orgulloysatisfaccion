from newspaper import Article
import re
import time

def save(year, text):
	my_file = open(year + "_" + str(time.time()) + '.txt', 'w', encoding='utf-8')
	my_file.write(text)
	my_file.close()

def get_speech(url):
	speech = Article(url)
	speech.download()
	speech.parse()
	return speech.text
	
def add_index(year, url):
	my_file = open('index.csv', 'a', encoding='utf-8')
	my_file.write(year + ", "  + url + "\n")
	my_file.close()
	
def get_year(texto):
	pattern = "\d{4}"
	new_year = re.search(pattern +"(?!.*\d+)", texto)
	if new_year:
		return str(int(new_year.group(0)) - 1)
	else:
		return str(time.time())

urls = ["http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5632", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5555", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5420", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5292", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5178", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2620", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2483", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2348", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2179", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2004","http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2898", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2667", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5046", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5056", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5090", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5080", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5072", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5065", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5042", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5038", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5032", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5030", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5029", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5023", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5013", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5002", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4991", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4910", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4909", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4905", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4903", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4902", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4901", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4897", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4873", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2824", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2823", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2822", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2821", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=4877", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=5734", "http://www.casareal.es/ES/Actividades/Paginas/actividades_discursos_detalle.aspx?data=2819"]

for url in urls:
	texto = get_speech(url)
	year = get_year(texto)
	save(year, texto)
	add_index(year, url)
	print(year + " " + url)
