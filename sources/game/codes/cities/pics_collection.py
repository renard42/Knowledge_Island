from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup

cities = open('cities.txt', 'r').read()
cities_db = [line.split(',')[0] for line in cities.split('\n')[:101]]

for i in cities_db:
    try:
        url = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote(i))
    except:
        url = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote(i+'_(город)'))
    soup = BeautifulSoup(url, 'html.parser')
    try:
        table = soup.find_all('table',{'class':'infobox vcard'})[0]
    except:
        url = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote(i+'_(город)'))
        soup = BeautifulSoup(url, 'html.parser')


    for num,img in enumerate(table.find_all('a', {'class':'image'})):
        if num == 0:
            request.urlretrieve('https:'+img.findChild()['src'],i+".png")
        if img.findChild()['alt'] == 'Герб':
            request.urlretrieve('https:'+img.findChild()['src'],i+"_герб.png")


