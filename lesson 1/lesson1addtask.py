'''
Реализуйте структуру данных «Участники спора». Она должна представлять собой
список (list) словарей (dict).
Каждый словарь хранит информацию об отдельном участнике. Словарь содержит
пары «ключ-значение» параметрами, то есть характеристиками участника:
наименование, статус, ИНН.
Заполнение данных должно быть произведено пользователем через консоль для трёх
различных участников.
'''
parties = [
    {'name:':str(input('Name of the party: ')), 'status:':str(input('Status of the party: ')), 'inn:':str(input('INN of the party: '))},
    {'name:':str(input('Name of the party: ')), 'status:':str(input('Status of the party: ')), 'inn:':str(input('INN of the party: '))},
    {'name:':str(input('Name of the party: ')), 'status:':str(input('Status of the party: ')), 'inn:':str(input('INN of the party: '))}
]
print(parties[0])