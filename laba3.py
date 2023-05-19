import re
from functools import reduce
from collections import OrderedDict

lenta = '''
5 Курс биткоина вырос до 1000 долларов.
10 В новогоднюю ночь выйдет новая первая серия нового сезона "Шерлока".
7 В Новосибирске из автобуса сбежала кондуктор.
1 Самолет «Почты России» вылетел с опозданием в несколько месяцев.
20 Козёл Тимур подружился с тигром Амуром.
10 Инженерам из Space X удалось посадить первую ступень ракеты на землю.
1 произошел теракт
21 произошла пасха
24 стало круто
1 налоги повысили 
20 налоги понизил'''

news_list = re.findall(r'\d+ .+', lenta)

def get_number(lenta):
    return int(lenta.split()[0])

published_news = []
for lenta in news_list:
    if not published_news or get_number(lenta) > get_number(published_news[-1]):
        published_news.append(lenta)

for lenta in published_news:
    print(lenta)


