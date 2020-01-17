import requests
from bs4 import BeautifulSoup
import os
import sys

# compteur d'images
count = 0
# fonction pour connaitre le nombre de page d'un chapitre chapitre
def nbrePageChapter(manga,chapter):
	chapter = str(chapter)
	web = 'https://www.mangapanda.com/'+manga+'/'+chapter
	r = requests.get(web)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	number = []
	for link in soup.find_all('option'):
		number.append(link.get('value').replace('/'+manga+'/'+chapter+'/',''))
	del number[0]
	number.insert(0,'1')
	return number;
# Fonction pour télécharger une page donné sur un chapitre donné d'un titre de manga donné
def telecharger(manga,chapter,i):	
	manga = str(manga)
	chapter = str(chapter)
	i = str(i)
	web = 'https://www.mangapanda.com/'+manga+'/'+chapter+'/'+i
	r = requests.get(web)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	shortlink = web.split("/")[2]
	fullshort ="http://" + shortlink
	question_mark = "?"

	for link in soup.find_all('img'):
		try:
			image = link.get('src')
			if "http" not in image:
				image = fullshort + image
			image.split(question_mark, maxsplit=1)[0]
			image_name = os.path.split(image)[1]
			# essayer de changer le nom de l'image
			image_name = image_name.split(question_mark, maxsplit=1)[0]
			r2 = requests.get(image)
			print(image_name)
			global count
			count+=1
			try:
				os.makedirs(manga+'/'+chapter)
			except FileExistsError:
				pass
			with open(manga+'/'+chapter+'/'+image_name, 'wb') as f:
				f.write(r2.content)
		except:
			continue
# recupération des arguments d'appel du programme
if len(sys.argv)>1:
	if ',' in sys.argv[2]:
		chapters = sys.argv[2].split(',')
		for chapter in chapters:
			pages = nbrePageChapter(sys.argv[1],chapter)
			i = 0
			while i < len(pages):
				telecharger(sys.argv[1],chapter,i+1)
				i=i+1
	elif '-' in sys.argv[2]:
		chapter_debut = int(sys.argv[2].split('-')[0])
		chapter_fin = int(sys.argv[2].split('-')[1])
		
		chapters = range(chapter_debut,chapter_fin+1)
		for chapter in chapters :
			pages = nbrePageChapter(sys.argv[1],chapter)
			i = 0
			while i < len(pages):
				telecharger(sys.argv[1],chapter,i+1)
				i=i+1
	else:
		manga = sys.argv[1]
		chapter = sys.argv[2]
		pages = nbrePageChapter(manga,chapter)
		i=0
		while i < len(pages):
			telecharger(manga,chapter,i+1)
			i=i+1
# si le programme est applé sans argument on demande a l'utilisateur de les saisir au clavier	
else:
	manga = input("Entrez le nom du manga: ")
	chapter = input("entrez le numero du chapitre: ")
	telecharger(manga,chapter)

print("--------")
print("--------")
print("Total images downloaded:", count)
print("--------")
print("--------")