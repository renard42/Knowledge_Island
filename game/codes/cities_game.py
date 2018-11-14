from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup

url = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote('Список_городов_России'))
soup = BeautifulSoup(url, 'html.parser')

cities_db = {}
table = soup.find_all('tbody')
for row in soup.find_all('tr',{'class':None}):
    cities = [city.text.strip() for city in row.find_all('td')]
    print(cities)
    try:
        url_info = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote(cities[2]))
        soup_info = BeautifulSoup(url_info, 'html.parser')
        info = soup_info.find_all('div', {'class':"mw-parser-output"})[0]
        
        cities_db[cities[2]] = int(cities[5])
    except:
        pass
    if len(cities_db) == 5:
        break

print(cities_db)

