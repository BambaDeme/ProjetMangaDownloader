FROM python:3
ADD download_manga.py /home
WORKDIR home

RUN pip install requests
RUN pip install bs4
RUN pip install BeautifulSoup4 
RUN pip install lxml

CMD ["python","download_manga.py"] > ../home

VOLUME ../home