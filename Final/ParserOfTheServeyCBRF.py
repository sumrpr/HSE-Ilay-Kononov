'''
Это то же, что и было в задании 13. К сожалению, я не смог придумать новых методов анализа данных 
(или не имел достаточно понимания, чтобы их имплементировать в разумные сроки, когда что-то придумывалось)
Технически, этот код соответвует требованиям из задания - он парсит сайт ЦБ, анализирует полученный файл,
достает информацию о количестве различных вхождений в таблице, буде то регионы РФ или ответы респондентов
'''

import requests
from bs4 import BeautifulSoup
import zipfile
import io
import csv

class ParserCBRF:

    def __init__(self):
        self.soup = None


    def __getdata__(self):
        url = "https://cbr.ru/ec_research/vserossiyskoe-obsledovanie-domokhozyaystv-po-potrebitel-skim-finansam/"
        r = requests.get(url)
        r.raise_for_status()
        self.soup = BeautifulSoup(r.text, 'html.parser')

    def __householddataExtractor__(self):
        file = self.soup.find(id="a_145697file").get('href')
        response = requests.get(f"https://cbr.ru{file}")
        with zipfile.ZipFile(io.BytesIO(response.content)) as myzip:
            myzip.extract("5th_wave_hh_230323.csv")
        
    def __csvUnderTheHudWork__(self, searchkey, searchterm):
        counter = 0
        householdFilecsv = open("5th_wave_hh_230323.csv", "r", encoding="cp1251", newline="")
        householdDictreder = csv.DictReader(householdFilecsv)
        for row in householdDictreder:
            if row[searchkey] == searchterm:
                counter += 1
        print(counter)
        householdFilecsv.close()


    def __main__(self, searchkey, searchterm):
        self.__getdata__()
        self.__householddataExtractor__()
        self.__csvUnderTheHudWork__(searchkey, searchterm)

    def start(self, searchkey, searchterm):
        self.__main__(searchkey, searchterm)


nice = ParserCBRF()
nice.start("psu", "Ленинградская область")
