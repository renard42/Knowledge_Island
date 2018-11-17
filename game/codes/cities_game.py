 en_US.UTF-8

from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup

url = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote('Список_городов_России'))
soup = BeautifulSoup(url, 'html.parser')

cities_db = {}
table = soup.find_all('tbody')
for row in soup.find_all('tr',{'class':None}):
    cities = [city.text.strip() for city in row.find_all('td')]
    try:
        link = 'https://ru.wikipedia.org/'+row.find_all('td', {'align':'left'})[0].findChild()['href']
        soup_info = BeautifulSoup(request.urlopen(link), 'html.parser')

        for i in soup_info.find('div', {'class':'mw-parser-output'}).find_all('p'):
            if cities[2] in i.text.strip():
                info = i.text.strip()
                break
        cities_db[cities[2]] = [int(cities[5]), info]
    except:
        pass
    if len(cities_db) == 10:
        break

#print(cities_db)
import unidecode
print(unidecode.unidecode('Абду́лино'))


