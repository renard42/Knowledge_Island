import random
cities =open('cities.csv', 'r', encoding='utf-8').read()
cities_db = [line.split(',')[0] for line in cities.split('\n')]
print('Киров' in cities_db)
