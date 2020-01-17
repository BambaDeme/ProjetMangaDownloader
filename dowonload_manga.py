import requests
from bs4 import BeautifulSoup
import os
import sys

# compteur d'images
count = 0

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
print("--------")
print("--------")
print("Total images downloaded:", count)
print("--------")
print("--------")