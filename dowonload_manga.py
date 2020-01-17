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

print("--------")
print("--------")
print("Total images downloaded:", count)
print("--------")
print("--------")