from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup
import pandas as pd

url = request.urlopen('https://ru.wikipedia.org/wiki/'+ quote('Список_городов_России'))
soup = BeautifulSoup(url, 'html.parser')

cities_db = {}
table = soup.find_all('tbody')
for row in soup.find_all('tr'):
    cities = [city.text.strip() for city in row.find_all('td')]
    try:
        link = 'https://ru.wikipedia.org/'+row.find_all('td', {'align':'left'})[0].findChild()['href']
        soup_info = BeautifulSoup(request.urlopen(link), 'html.parser')

        for i in soup_info.find('div', {'class':'mw-parser-output'}).find_all('p'):
            if cities[2].replace(u'\u0301', '') in i.text.strip().replace(u'\u0301', ''):
                info = i.text.strip().replace(u'\u0301', '')
                break
        cities_db[cities[2]] = [int(cities[5]), info]
        #print(cities[2])
    except:
        pass


pd.DataFrame.from_dict(cities_db, orient='index').sort_values(by=0, ascending=False).to_csv('cities.csv')





