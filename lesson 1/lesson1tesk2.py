'''
2.	Пользователь вводит время в секундах. Рассчитайте время и сохраните отдельно в каждую переменную количество часов, минут и секунд. Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
'''
timeinseconds = int(input())
hours = timeinseconds // 3600
minutes = (timeinseconds % 3600) // 60
seconds = timeinseconds - ((hours * 3600) + (minutes * 60))
print('the time is ',hours,':',minutes,':',seconds)
