# Сериализация и Десереализация.

> `Сериализация` — процесс преобразования объекта в поток байтов для сохранения или передачи в память, базу данных или файл. Эта операция предназначена для того, чтобы сохранить состояния объекта для последующего воссоздания при необходимости. Обратный процесс называется десериализацией.

# JSON файлы.

### JSON - JavaScript Object Notation

`JSON файлы`:

* Синтаксически и функционально является подмножеством языка YAML
* Файлы имеют "Древовидную" структуру, максимально похожие на словари в Python итд. 
* Основное применение: Базы данных и выгрузки данных. (в т.ч. bson)
* Так же применячется для передачи данных клиент <-> сервер.
* Самый популярный и простой в использовании формат для Python и Java программистов


Основые моменты работы с `JSON` файлами:
    
**Десериализация (читаем файл)**

Из файла: 

   * `json.load(file)`

Из строки:
    
   * `json.loads(str)`

**Сериализация (сохраняем файл)**

В файл: 

   * `json.dump(str, file_name)`
    
В строку: 

   * `json.dumps(data, file_name)`

**Печать не-ascii символов, отступы:**

   * `ensure_ascii=False, indent=2` 

## json.load()

Прочтем содержимое файла `newsafr.json` и преобразуем его содержимое в словарь Python:


**Выполним код:**
```python
import json
from pprint import pprint

with open('newsafr.json') as f:
    file_data = json.load(f)
print(type(file_data))
pprint(file_data)
```

_Результаты:_

<class 'dict'>

```
{'rss': {'_version': '2.0',
         '_xmlns:votpusk': 'https://www.votpusk.ru/news.asp',
         'channel': {'category': 'Туризм - Африка',
                     'description': 'Африка - Лента туристических новостей '
                                    'портала В ОТПУСК.РУ ',
                     'items': [{'_id': '544347',
                                'description': 'Содержание новости',
                                'guid': 'https://www.votpusk.ru/news.asp?msg=544347',
                                'link': 'https://www.votpusk.ru/news.asp?msg=544347 ',
                                'pubDate': 'Mon, 17 Oct 2016 00:28 +0300',
                                'title': 'Израильский турист погиб в ДТП в '
                                         'Африке'},
                               {'_id': '537417',
                                'description': 'Содержание новости',
                                'guid': 'https://www.votpusk.ru/news.asp?msg=537417',
                                'link': 'https://www.votpusk.ru/news.asp?msg=537417 ',
                                'pubDate': 'Thu, 17 Dec 2015 19:13 +0300',
                                'title': 'Ростуризм просит турбизнес сообщать '
                                         'людям о риске заражения в Африке'},
                               {'_id': '534896',
                                'description': 'Содержание новости',
                                'guid': 'https://www.votpusk.ru/news.asp?msg=534896',
                                'pubDate': 'Wed, 16 Sep 2015 14:36 +0300',
                                'title': 'Открытие сафари кемпа Belmond Eagle '
                                         'Island Lodge в Ботсване после '
                                         'реновации'}],
                     'language': 'ru',
                     'lastBuildDate': 'Thu, 1 Dec 2016 17:27 +0300 ',
                     'link': 'https://www.votpusk.ru/news.asp',
                     'title': 'Новости Африка'}}}
```
* В результате открытия и чтения файла 'newsafr.json' в переменную file_data мы поместили словарь, к которому мы можем применять все методы обработки данного класса и выполнять различные действия по работе и обработки данных.

**В качестве примера: дополним код, выедем все заголовки и посчитаем кол-во новостей:***

```python
import json

with open('newsafr.json') as f:
    file_data = json.load(f)

work_list = file_data['rss']['channel']['items']
count = 0
for elem in work_list:
    count += 1
    print(elem['title'])
print(count)
```

*Получим результат:*
```
Израильский турист погиб в ДТП в Африке
Ростуризм просит турбизнес сообщать людям о риске заражения в Африке
Открытие сафари кемпа Belmond Eagle Island Lodge в Ботсване после реновации
3
```

## json.dump()

Запишем содержимое файла `newsafr.json` в новый файл `new.json`:

**Выполним код:**
```python

import json

with open('newsafr.json') as f:
    file_data = json.load(f)

with open('new.json', 'w') as new_f:
    json.dump(file_data, new_f)
    
```

В результате получим файл `new.json` с содержимым:
```
{"rss": {"_xmlns:votpusk": "https://www.votpusk.ru/news.asp", "_version": "2.0", "channel": {"description": "\u0410\u0444\u0440\u0438\u043a\u0430 - \u041b\u0435\u043d\u0442\u0430 \u0442\u0443\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439 \u043f\u043e\u0440\u0442\u0430\u043b\u0430 \u0412 \u041e\u0422\u041f\u0423\u0421\u041a.\u0420\u0423 ", "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ", "items": [{"guid": "https://www.votpusk.ru/news.asp?msg=544347", "_id": "544347", "pubDate": "Mon, 17 Oct 2016 00:28 +0300", "description": "\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438", "link": "https://www.votpusk.ru/news.asp?msg=544347 ", "title": "\u0418\u0437\u0440\u0430\u0438\u043b\u044c\u0441\u043a\u0438\u0439 \u0442\u0443\u0440\u0438\u0441\u0442 \u043f\u043e\u0433\u0438\u0431 \u0432 \u0414\u0422\u041f \u0432 \u0410\u0444\u0440\u0438\u043a\u0435"}, {"guid": "https://www.votpusk.ru/news.asp?msg=537417", "_id": "537417", "pubDate": "Thu, 17 Dec 2015 19:13 +0300", "description": "\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438", "link": "https://www.votpusk.ru/news.asp?msg=537417 ", "title": "\u0420\u043e\u0441\u0442\u0443\u0440\u0438\u0437\u043c \u043f\u0440\u043e\u0441\u0438\u0442 \u0442\u0443\u0440\u0431\u0438\u0437\u043d\u0435\u0441 \u0441\u043e\u043e\u0431\u0449\u0430\u0442\u044c \u043b\u044e\u0434\u044f\u043c \u043e \u0440\u0438\u0441\u043a\u0435 \u0437\u0430\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0432 \u0410\u0444\u0440\u0438\u043a\u0435"}, {"guid": "https://www.votpusk.ru/news.asp?msg=534896", "_id": "534896", "pubDate": "Wed, 16 Sep 2015 14:36 +0300", "description": "\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438", "link": "https://www.votpusk.ru/news.asp?msg=534896 ", "title": "\u041e\u0442\u043a\u0440\u044b\u0442\u0438\u0435 \u0441\u0430\u0444\u0430\u0440\u0438 \u043a\u0435\u043c\u043f\u0430 Belmond Eagle Island Lodge \u0432 \u0411\u043e\u0442\u0441\u0432\u0430\u043d\u0435 \u043f\u043e\u0441\u043b\u0435 \u0440\u0435\u043d\u043e\u0432\u0430\u0446\u0438\u0438"}], "category": "\u0422\u0443\u0440\u0438\u0437\u043c - \u0410\u0444\u0440\u0438\u043a\u0430", "language": "ru", "link": "https://www.votpusk.ru/news.asp", "title": "\u041d\u043e\u0432\u043e\u0441\u0442\u0438 \u0410\u0444\u0440\u0438\u043a\u0430"}}}
```
* **Python** по умолчанию превратил все символы кириллицы в **unicod**.
* Так же мы не задали параметры форматирования для более удобного отображения данных.
* Решить данные проблемы мы можем использовав параметры `ensure_ascii=False` и `indent=2`

### используем параметры `ensure_ascii=False` и `indent=2`

**Выполним код:**
```python

import json

with open('newsafr.json') as f:
    file_data = json.load(f)

with open('new.json', 'w') as new_f:
    json.dump(file_data, new_f, ensure_ascii=False, indent=2)
    
```

В результате получим файл `new.json` с содержимым:
```
{
  "rss": {
    "_xmlns:votpusk": "https://www.votpusk.ru/news.asp",
    "_version": "2.0",
    "channel": {
      "description": "Африка - Лента туристических новостей портала В ОТПУСК.РУ ",
      "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ",
      "items": [
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=544347",
          "_id": "544347",
          "pubDate": "Mon, 17 Oct 2016 00:28 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=544347 ",
          "title": "Израильский турист погиб в ДТП в Африке"
        },
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=537417",
          "_id": "537417",
          "pubDate": "Thu, 17 Dec 2015 19:13 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=537417 ",
          "title": "Ростуризм просит турбизнес сообщать людям о риске заражения в Африке"
        },
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=534896",
          "_id": "534896",
          "pubDate": "Wed, 16 Sep 2015 14:36 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=534896 ",
          "title": "Открытие сафари кемпа Belmond Eagle Island Lodge в Ботсване после реновации"
        }
      ],
      "category": "Туризм - Африка",
      "language": "ru",
      "link": "https://www.votpusk.ru/news.asp",
      "title": "Новости Африка"
    }
  }
}
```
* Проблема с отображением криллицы решена, данные отображаются в улобном для чтения виде.

## json.dumps()

Чтение файла `JSON`, преобразование его данных в строку с последующей записью в файл `new.txt`

**Содержание файла** `newsafr.json`:

```
{
  "rss": {
    "_xmlns:votpusk": "https://www.votpusk.ru/news.asp",
    "_version": "2.0",
    "channel": {
      "description": "Африка - Лента туристических новостей портала В ОТПУСК.РУ ",
      "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ",
      "items": [
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=544347",
          "_id": "544347",
          "pubDate": "Mon, 17 Oct 2016 00:28 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=544347 ",
          "title": "Израильский турист погиб в ДТП в Африке"
        },
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=537417",
          "_id": "537417",
          "pubDate": "Thu, 17 Dec 2015 19:13 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=537417 ",
          "title": "Ростуризм просит турбизнес сообщать людям о риске заражения в Африке"
        },
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=534896",
          "_id": "534896",
          "pubDate": "Wed, 16 Sep 2015 14:36 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=534896 ",
          "title": "Открытие сафари кемпа Belmond Eagle Island Lodge в Ботсване после реновации"
        }
      ],
      "category": "Туризм - Африка",
      "language": "ru",
      "link": "https://www.votpusk.ru/news.asp",
      "title": "Новости Африка"
    }
  }
}
```

**Выполним код:**
```python
with open('newsafr.json') as f:
    file_data = json.load(f)
    json_str = json.dumps(file_data, ensure_ascii=False)

with open('new.txt', 'w') as new_f:
    new_f.write(json_str)
```

*В результате получим файл `new.txt` содержащий строку данных:*
```
{"rss": {"_xmlns:votpusk": "https://www.votpusk.ru/news.asp", "_version": "2.0", "channel": {"description": "Африка - Лента туристических новостей портала В ОТПУСК.РУ ", "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ", "items": [{"guid": "https://www.votpusk.ru/news.asp?msg=544347", "_id": "544347", "pubDate": "Mon, 17 Oct 2016 00:28 +0300", "description": "Содержание новости", "link": "https://www.votpusk.ru/news.asp?msg=544347 ", "title": "Израильский турист погиб в ДТП в Африке"}, {"guid": "https://www.votpusk.ru/news.asp?msg=537417", "_id": "537417", "pubDate": "Thu, 17 Dec 2015 19:13 +0300", "description": "Содержание новости", "link": "https://www.votpusk.ru/news.asp?msg=537417 ", "title": "Ростуризм просит турбизнес сообщать людям о риске заражения в Африке"}, {"guid": "https://www.votpusk.ru/news.asp?msg=534896", "_id": "534896", "pubDate": "Wed, 16 Sep 2015 14:36 +0300", "description": "Содержание новости", "link": "https://www.votpusk.ru/news.asp?msg=534896 ", "title": "Открытие сафари кемпа Belmond Eagle Island Lodge в Ботсване после реновации"}], "category": "Туризм - Африка", "language": "ru", "link": "https://www.votpusk.ru/news.asp", "title": "Новости Африка"}}}
```

## json.loads() 

Прочитаем строку данных из файла `new.txt`, преобразуем в словарь и запишем данные в новый файл `json_new.json` в формате JSON.

**Содержание файла** `new.txt` можно увидеть выше, в прошлом примере.

Выполним код:
```python
import json
from pprint import pprint

# Блок кода №1. Чтение строки файла new.txt:
with open('new.txt') as f:
    _str = f.read()
    # Блок кода №2. Преобразование данных строки в словарь.
    _json = json.loads(_str)

# Блок кода №3.Запись словаря в JSON файл.
with open('json_new.json', 'w') as new_json:
    json.dump(_json, new_json, ensure_ascii=False, indent=2)


print('Результат работы Блока кода №1.')
print("Тип данных переменной _str:", type(_str))
print('Вывод данных переменной _str:', _str)
print("Обращаемся в элементам строки _str через индекс:", _str[:6])
print('===========================================================')
print('Результат работы Блока кода №2.')
print("Тип данных переменной _jsom:", type(_json))
print("Красивый вывод через pprint:")
pprint(_json)
print('Обратимся по ключам к ID первой статьи:', _json['rss']['channel']['items'][1]['_id'])
print('===========================================================')
```

**Результаты выполнения кода в Блоке №1 и №2:**

```
Результат работы Блока кода №1.


Тип данных переменной _str: <class 'str'>

Вывод данных переменной _str: {"rss": {"_xmlns:votpusk": "https://www.votpusk.ru/news.asp", "_version": "2.0", "channel": {"description": "Африка - Лента туристических новостей портала В ОТПУСК.РУ ", "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ", "items": [{"guid": "https://www.votpusk.ru/news.asp?msg=544347", "_id": "544347", "pubDate": "Mon, 17 Oct 2016 00:28 +0300", "description": "Содержание новости", "link": "https://www.votpusk.ru/news.asp?msg=544347 ", "title": "Израильский турист погиб в ДТП в Африке"}, {"guid": "https://www.votpusk.ru/news.asp?msg=537417", "_id": "537417", "pubDate": "Thu, 17 Dec 2015 19:13 +0300", "description": "Содержание новости", "link": "https://www.votpusk.ru/news.asp?msg=537417 ", "title": "Ростуризм просит турбизнес сообщать людям о риске заражения в Африке"}, {"guid": "https://www.votpusk.ru/news.asp?msg=534896", "_id": "534896", "pubDate": "Wed, 16 Sep 2015 14:36 +0300", "description": "Содержание новости", "link": "https://www.votpusk.ru/news.asp?msg=534896 ", "title": "Открытие сафари кемпа Belmond Eagle Island Lodge в Ботсване после реновации"}], "category": "Туризм - Африка", "language": "ru", "link": "https://www.votpusk.ru/news.asp", "title": "Новости Африка"}}}

Обращаемся в элементам строки _str через индекс: {"rss"

===========================================================

Результат работы Блока кода №2.

Тип данных переменной _jsom: <class 'dict'>
Красивый вывод через pprint:
{'rss': {'_version': '2.0',
         '_xmlns:votpusk': 'https://www.votpusk.ru/news.asp',
         'channel': {'category': 'Туризм - Африка',
                     'description': 'Африка - Лента туристических новостей '
                                    'портала В ОТПУСК.РУ ',
                     'items': [{'_id': '544347',
                                'description': 'Содержание новости',
                                'guid': 'https://www.votpusk.ru/news.asp?msg=544347',
                                'link': 'https://www.votpusk.ru/news.asp?msg=544347 ',
                                'pubDate': 'Mon, 17 Oct 2016 00:28 +0300',
                                'title': 'Израильский турист погиб в ДТП в '
                                         'Африке'},
                               {'_id': '537417',
                                'description': 'Содержание новости',
                                'guid': 'https://www.votpusk.ru/news.asp?msg=537417',
                                'link': 'https://www.votpusk.ru/news.asp?msg=537417 ',
                                'pubDate': 'Thu, 17 Dec 2015 19:13 +0300',
                                'title': 'Ростуризм просит турбизнес сообщать '
                                         'людям о риске заражения в Африке'},
                               {'_id': '534896',
                                'description': 'Содержание новости',
                                'guid': 'https://www.votpusk.ru/news.asp?msg=534896',
                                'link': 'https://www.votpusk.ru/news.asp?msg=534896 ',
                                'pubDate': 'Wed, 16 Sep 2015 14:36 +0300',
                                'title': 'Открытие сафари кемпа Belmond Eagle '
                                         'Island Lodge в Ботсване после '
                                         'реновации'}],
                     'language': 'ru',
                     'lastBuildDate': 'Thu, 1 Dec 2016 17:27 +0300 ',
                     'link': 'https://www.votpusk.ru/news.asp',
                     'title': 'Новости Африка'}}}
                     
Обратимся по ключу и получим ID первой статьи: 537417

===========================================================

```

**В результате выполнения кода в Блоке №3 получим новый файл `json_new.json` следующего содержания:**
```
{
  "rss": {
    "_xmlns:votpusk": "https://www.votpusk.ru/news.asp",
    "_version": "2.0",
    "channel": {
      "description": "Африка - Лента туристических новостей портала В ОТПУСК.РУ ",
      "lastBuildDate": "Thu, 1 Dec 2016 17:27 +0300 ",
      "items": [
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=544347",
          "_id": "544347",
          "pubDate": "Mon, 17 Oct 2016 00:28 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=544347 ",
          "title": "Израильский турист погиб в ДТП в Африке"
        },
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=537417",
          "_id": "537417",
          "pubDate": "Thu, 17 Dec 2015 19:13 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=537417 ",
          "title": "Ростуризм просит турбизнес сообщать людям о риске заражения в Африке"
        },
        {
          "guid": "https://www.votpusk.ru/news.asp?msg=534896",
          "_id": "534896",
          "pubDate": "Wed, 16 Sep 2015 14:36 +0300",
          "description": "Содержание новости",
          "link": "https://www.votpusk.ru/news.asp?msg=534896 ",
          "title": "Открытие сафари кемпа Belmond Eagle Island Lodge в Ботсване после реновации"
        }
      ],
      "category": "Туризм - Африка",
      "language": "ru",
      "link": "https://www.votpusk.ru/news.asp",
      "title": "Новости Африка"
    }
  }
}
```

**Мы расмотрели полный цикл работы с файлами JSON:**
   * Открытие файла формата JSON
   * Преобразование данных из файла JSON в словарь Python
      * Запись словаря в новый файл формата JSON
   * Преобразование данных из файла JSON в строку Python
        * Запись строки в новый файл формата .txt
   * Чтение строки данных из файла формата .txt
       * Преобразование строки в словарь Python
       * Запись словаря в новый файл формата JSON
   

# YAML файлы.

> Язак разметки YAML является родительским для JSON

Основное применение формата `YAML`

* Файлы конфигурации
* Самый компактный язык разметки
* Для создания файлов настроек
* Используется для описания классов, ресурсов и манифестов в API

Основые моменты работы с `YAML` файлами:
    
**Десериализация (читаем файл)**

Из файла: 

   * `json.load(file)`

Из строки:
    
   * `json.loads(str)`

**Сериализация (сохраняем файл)**

В файл: 

   * `json.dump(str, file_name)`
    
В строку: 

   * `json.dumps(data, file_name)`

**Печать не-ascii символов, отступы:**

   * `allow_unicode=True, default_flow_style=False` 


```python

```
