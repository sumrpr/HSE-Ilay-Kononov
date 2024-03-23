'''
Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле
traders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла
traders.txt в файл traders.csv.

'''

import json
import csv
f = open('traders.txt', 'r')
innlist = f.readlines()
f.close()
rows = []
#print(innlist)
traders = open('traders.json', 'r')
traderslist = json.load(traders)
#print(traderslist)
for i in innlist:
    a = i.rstrip('\n')
    for m in traderslist:
        if m['inn'] == a:
            rows.append([m['inn'],m['ogrn'],m['address'].replace(',', ' ')])
#print(rows)
#кодировка делает созданный файл читаемым в редакторе, без кодировки он читаем в Экселе: encoding="UTF8". В качестве разделителя использую ";", т.к. Эксель предпочитатет именно это символ
with open('traders.csv', 'w', newline='') as csvfile:     
    csvwriter = csv.writer(csvfile, delimiter=';')    
    csvwriter.writerows(rows)
