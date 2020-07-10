import requests #Подключение библиотеки запросов. 
from bs4 import BeautifulSoup as BS #Подключение библиотеки для парсинга,для работы с тегами аштиэмэль,для добывания инфы

class Parse(): #Класс для работы с парсом. Сюда мы будем получать информацию
    def __init__(self, url): #С помощью этого мы будем посылать запрос на сайт
        self.url = url
        self.values = []
        #Запрос и получение аштиэмэль
        source = requests.get(self.url)
        self.html = BS(source.text, 'lxml') #Первый параметр - что достаём, второй - как достаём 
    
    def get_content(self):
        table = self.html.find("table", {'id' : "courses-main"} ) #Первый параметр - название тега, который мы ищем, а вторым - словарь. В словаре находятся все параметры этого тега(Ключ - название тега, значение - содержание тега)
        tbody = table.find("tbody")

        for tr in tbody.find_all('tr'): #Получаем все нужные нам элементы
            td = tr.find_all ('td', {'class': ''})
            for value in td:
                if value.text != '':
                    self.values.append(value.text.lstrip())
    
        self.values = self.values[4:]

        return self.values   
