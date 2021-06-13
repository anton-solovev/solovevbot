import requests
import datetime
import numpy as np
from bs4 import BeautifulSoup
global time_period
time_period = np.array([[700, 1030],[1031, 1200],
                        [1201, 1410],[1411, 1550],
                        [1551, 1730],[1731, 2050],
                        [2001, 2140]], int)
def date():
    today = datetime.datetime.today().weekday()  
    current_time = int(datetime.datetime.today().strftime("%H")+
                     datetime.datetime.today().strftime("%M"))
    return today,current_time
def number_lesson(current_time, time_period):
    counter = 0
    while not( time_period[counter,0] < current_time < time_period[counter,1]):
        counter += 1
    return counter+1
def parsing_lesson(group_id,current_time,today):
    if today == 6:
        print("Сегодня воскресенье!С ума сошел? Иди отдыхай!")
    else:
        url = 'http://r.sf-misis.ru/teacher/'
        page = requests.get(url+group_id)
        soup = BeautifulSoup(page.text, 'lxml')
        print("Сегодня: "
              +soup.find_all(class_='table-weekdays')[today].get_text())
        one = soup.find_all('tr')[today+1]
        lesson = number_lesson(current_time, time_period)
        table = one.find_all('td')[lesson-1].get_text().replace("\t", "")
        exist = "—" in table
        if exist:
            print("У тебя нет пары! Отдохни!")
        else:
            print("У тебя:",lesson,"-ая пара")
            print(" ".join(table.split()).replace(". ",".",1))
