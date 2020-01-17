FROM python:3-alpine
ADD . /app
WORKDIR /app

RUN pip install requests
RUN pip install bs4
RUN pip install BeautifulSoup4
RUN pip install lxml4 

CMD ["python","download_manga.py"]