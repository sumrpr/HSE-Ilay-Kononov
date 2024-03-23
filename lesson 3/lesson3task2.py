'''
Напишите регулярное выражение для поиска email-адресов в тексте.
Для этого напишите функцию, которая принимает в качестве аргумента текст в виде
строки и возвращает список найденных email-адресов или пустой список, если
email-адреса не найдены.
Используйте датасет на 1 000 сообщений из Единого федерального реестра сведений
о банкротстве (ЕФРСБ) для практики.
Есть датасеты и побольше:
● датасет на 10 000 сообщений,
● датасет на 100 000 сообщений.
Если компьютер слабый, ограничьтесь самым маленьким.
Текст сообщений можно найти по ключу msg_text.
Найдите все email-адреса в датасете и соберите их в словарь, где ключом будет
выступать ИНН опубликовавшего сообщение publisher_inn, а в значении будет
храниться множество set() с email-адресами. Пример:
{
“77010127248512”: {“name_surname@yandex.ru”, “name_surname@mail.ru”}
“77011235421242”: {“name_surname@yandex.ru”, “name_surname@gmail.com”}
…
}
Сохраните собранные данные в файл emails.json.
'''


import json
import re
inndict = {}
def emailfinder(m):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return(re.findall(pattern, m))
rows = []
traders = open('1000_efrsb_messages.json', 'r')
traderslist = json.load(traders)
for m in traderslist:
    inn = m['publisher_inn']
    emails = emailfinder(m['msg_text'])
    if inn and emails:
        inndict[inn] = emails
jsonfile = open("emails.json", "w")  
json.dump(inndict, jsonfile, indent = 6)
