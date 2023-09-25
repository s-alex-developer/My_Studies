*Последние изменения внесены 25.09.2023*

# Django. Обработка запросов и шаблоны.

## 1.  Параметры запросов.

**Варианты добавления параметров в запросы:**
   1. Использование опционального **GET-параметра** в запросе (`когда параметры опциональны!!!`).
   2. Через часть **URL** (`когда параметры являются обязательной частью запроса!!!`).
   3. **HTTP** заголовками.

### 1.1. `GET-параметры` в запросе.

_Пример 1:_
* **URL запроса:** `http://127.0.0.1:8000/hello/?name=Alex`

* **Обработчик:**            
```python
def hello_view(request):
name = request.GET['name']
return HttpResponse(f'{name}, Hello from Django')
```
`
* **В результате получим текст на странице:** `Alex, Hello from Django`
***

_Пример 2 (несколько параметров через амперсанд `&`):_
* **URL запроса:** `127.0.0.1:8000/hello/?name=Alex&year=2023`

* **Обработчик:**            
```python
def hello_view(request):
    name = request.GET['name']
    year = request.GET['year']
    return HttpResponse(f'{name}, Hello from Django in {year}')
```

* **В результате получим текст на странице:** `Alex, Hello from Django in 2023`
* **По умолчанию все получаемые данные из запроса строковые.**
* **При необхоимости мы можем изменить тип данных, например преобразотать год в число:**
```python
year = int(request.GET['year'])
```
***

_Пример 3 (Использование метода `get()`):_

Если мы не передадим какой -то из параметров в обработчки, например `year=2023` то это приведет к ошибке:
* **URL запроса:** `127.0.0.1:8000/hello/?name=Alex`

* **Обработчик:**            
```python
def hello_view(request):
    name = request.GET['name']
    year = request.GET['year']
    return HttpResponse(f'{name}, Hello from Django in {year}')
```

* **В результате получим ошибку на странице:** 
```
MultiValueDictKeyError at /hello/
'year'
```

**Мы можем обработать исключение при помощи `try / except` или же воспользоваться методом `get()`, который не приведет к ошибке, а вернет `None` в случае отсутсвия параметра в запросе:**

* **URL запроса:** `127.0.0.1:8000/hello/?name=Alex`

* **Обработчик:** 
```python
def hello_view(request):
    name = request.GET['name']
    year = request.GET.get('year')
    return HttpResponse(f'{name}, Hello from Django in {year}')
```
* **В результате получим ошибку на странице:** `Alex, Hello from Django in None`

*** 

### 1.2. Передача параметров через часть `URL`.

_Пример 1:_
* **URL запроса:** `http://127.0.0.1:8000/sum/2/3/`

* **Прописанный маршрут с применение конвертации типа данных:** 
    
```python
urlpatterns = [
    path('sum/<int:a>/<int:b>/', sum_view),
]

```
            
* **Обработчик:**            
```python
def sum_view(request, a, b):
    result = a + b
    return HttpResponse(f'Сумма параметров: {result}')
```
`
* **В результате получим текст на странице:** `Сумма параметров: 5`
***

### 1.3. Конвертеры маршрутов в Django 

1. Конвертеры маршрутов в Django существуют не для всех типов данных.
***
2. Стандартные конвертеры описаны в документации: [ссылка >>>](https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters)
***
3. Django помимо стандартных конвертеров предоставляет возможность создать свой конвертер и описать правила конвертации так, как угодно.
***
4. Для этого надо сделать два шага:
    * Описать класс конвертера.
    * Зарегистрировать конвертер.
***
5. Класс конвертера — это класс с определённым набором атрибутов и методов, описанных в документации (на мой взгляд, несколько странно, что разработчики не сделали базовый абстрактный класс). Сами требования:
***
6. Должен быть атрибут `regex`, описывающий регулярное выражение для быстрого поиска требуемой подпоследовательности. Чуть позже покажу, как он используется.
***
7. Реализовать метод `def to_python(self, value: str)` для конвертации из строки (ведь передаваемый маршрут — это всегда строка) в объект **python**, который в итоге будет передаваться в обработчик.
***
8. Реализовать метод `def to_url(self, value) -> str` для обратной конвертации из объекта **python** в строку (используется, когда вызываем django.urls.reverse или тег url).
***
**Класс для конвертации даты будет выглядеть так:**

```python
class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, '%Y-%m-%d')

   def to_url(self, value: datetime) -> str:
       return value.strftime('%Y-%m-%d')
```

**Вынесем формат даты в атрибут для упрощения поддержки конвертера:***

```python
class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> datetime:
       return datetime.strptime(value, self.format)

   def to_url(self, value: datetime) -> str:
       return value.strftime(self.format)
```

* **По итогу описания класса можно зарегистрировать его как конвертер.**
* Для этого в функции `register_converter` надо указать описанный класс и название конвертера, чтобы использовать его в маршрутах.

```python
from django.urls import register_converter
register_converter(DateConverter, 'date')
```

* **Опишем маршруты в urls.py:**

```python
path('users/<int:id>/reports/<date:dt>/', user_report, name='user_report'),
path('teams/<int:id>/reports/<date:dt>/', team_report, name='team_report'),
```

* **Теперь гарантируется, что обработчики вызываются только в том случае, если конвертер отработает корректно, а это значит, что в обработчик придут параметры нужного типа:**

```python
def user_report(request, id: int, dt: datetime):
   # больше никакой валидации в обработчиках
   # сразу правильные типы и никак иначе
```

## 2. Введение в шаблоны.

### 2.1 Функция `render`

Шаблоны используются для форматирования и отображения данных на тсранице пользователя.

**Настройка шаблонов производится в файле проекта Django `settings.py`**



```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Директории хранения шаблонов
        'APP_DIRS': True, # Поиск по умолчанию внутри приложения в папке templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Шаблоны должны быть расположены внутри директории приложения, которым они используются, в папке `templates`**

_Пример 1:_
* **URL запроса:** `http://127.0.0.1:8000/hello/`
* **Прописанный маршрут:** 
    
```python
urlpatterns = [
    path('hello/', hello_view),
]

```
            
* **Обработчик:**            
```python
from django.shortcuts import render


def hello_view(request):
    return render(request, 'hello.html')
```

* **Шаблон:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello</title>
</head>
<body>
    Hello from Django!
</body>
</html>
```
    
    
* **В результате получим текст на странице:** `Hello from Django!`
***

**Используя параметр `context` мы можем передавать при помщи функции `render` переменные Python в HTML шаблон:**

_Пример 2:_
* **URL запроса:** `http://127.0.0.1:8000/hello/`
* **Прописанный маршрут:** 
    
```python
urlpatterns = [
    path('hello/', hello_view),
]

```
            
* **Обработчик:**            
```python
from django.shortcuts import render


def hello_view(request):

    context = {
        'text': 'Hello from Django!',
        'name': 'alex',
        'numbers': [1, 10, 2, 20, 30, 3],
    }

    return render(request, 'hello.html', context)
```

* **Шаблон:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello</title>
</head>
<body>
    {{ text }}<br>
    {{ name.upper }}<br>

    {% for num in numbers %}
        {% if num > 9 %}
            <i>{{ num }}</i><br>
        {% endif %}
    {% endfor%}
</body>
</html>
```
    
    
* **В результате получим текст на странице:** 
```
Hello from Django!
ALEX
10
20
30
```
***
1. Мы вевели текст `Hello from Django!`.
2. Привели имя `ALEX` к верхнему регистру.
3. При помощи цикла `for` и опреатора `if` вывели на экран все числа списка, которые больше 9.
***

## 3.Пагинация

### 3.1. Введение.

**Пагинация** - способ выводить контент постранично.

Что нужно учитывать при пагинации:
   * Кол-во страниц (если есть навигация на произвольную страницу).
   * Есть ли следующая или предыдущая страница.
   * Переход на несуществующую страницу.

**В `Django` реализован пагинатор, решающий все эти задачи.**

_Пример 1 (Отображение элементов конкретной страницы, метод `get_page()`):_ 
* **URL запроса:** `http://127.0.0.1:8000/pagi/`
* **Прописанный маршрут:** 
    
```python
urlpatterns = [
    path('pagi/', pagi_view),
]

```
            
* **Обработчик:**            
```python
from django.shortcuts import render
from django.core.paginator import Paginator

# Сгенерируем тестовый контент:
CONTENT = [str(i) for i in range(100)]


def pagi_view(request):

    # Создаем объект класса Paginator (принимает контент и кол-во одновременно отображаемых элементов на странице)
    paginator = Paginator(CONTENT, 10)

    # В переменную page с помощью метода get_page() помещаем страницу, которую хотим отобразить.
    page = paginator.get_page(5)

    # Помещаем страницу page в переменную context для передачи в шаблон страницы.
    context = {
        'page': page
    }

    return render(request, 'pagi.html', context)
```

* **Шаблон:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Пагинатор</title>
</head>
<body>
    {% for el in page %}
        {{ el }}<br>
    {% endfor %}
</body>
</html>
```
    
    
* **В результате получим текст на странице:** 
```
40
41
42
43
44
45
46
47
48
49
```
> _Подобный вывод не удобен в реальной практике, так как мы сами задаем номер отображаемой страницы в коде, а необходимо чтобы пользователь сам мог выбирать страницы и перемещаться по ним._
***


_Пример 2 (Получение значения страницы для отображения из `GET` параметра):_ 
* **URL запроса:** `http://127.0.0.1:8000/pagi/?page=3`
* **Прописанный маршрут:** 
    
```python
urlpatterns = [
    path('pagi/', pagi_view),
]

```
            
* **Обработчик:**            
```python
from django.shortcuts import render
from django.core.paginator import Paginator

# Сгенерируем тестовый контент:
CONTENT = [str(i) for i in range(100)]


def pagi_view(request):

    # Создадим переменную page_number куда поместим номер запрашиваемой пользователем страницы из GET параметра:
    page_number = int(request.GET.get('page', 1))  # по умолчанию будет выводиться страница 1.

    # Создаем объект класса Paginator (принимает контент и кол-во одновременно отображаемых элементов на странице)
    paginator = Paginator(CONTENT, 10)

    # В переменную page передаем параметр page_number с номером страницы для отображения.
    page = paginator.get_page(page_number)

    # Помещаем страницу page в переменную context для передачи в шаблон страницы.
    context = {
        'page': page
    }

    return render(request, 'pagi.html', context)t)
```

* **Шаблон:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Пагинатор</title>
</head>
<body>
    {% for el in page %}
        {{ el }}<br>
    {% endfor %}
</body>
</html>
```
    
    
* **В результате получим текст на странице:** 
```
20
21
22
23
24
25
26
27
28
29
```
***


### 3.2. Свойства объекта `page` и реализация `Пагинации`.

> Как и любой объект в **Python** объект `page` имеем свойства, которые мы можем использовать для реализации пагинации на странице. 

**Ознакомимся со свойствами объекта `page`:**
```python
from pprint import pprint

pprint(dir(page))
```

**Получим результат:**
```python
['__abstractmethods__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__setattr__',
 '__sizeof__',
 '__slots__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_abc_impl',
 'count',
 'end_index',
 'has_next',
 'has_other_pages',
 'has_previous',
 'index',
 'next_page_number',
 'number',
 'object_list',
 'paginator',
 'previous_page_number',
 'start_index']
```

* **В следующем примере используем свойста объекта `page` и реализуем пагинацию с возвожность перехода между страницами:**

_Пример 3:_
* **Обработчик:**            
```python
from django.shortcuts import render
from django.core.paginator import Paginator

# Сгенерируем тестовый контент:
CONTENT = [str(i) for i in range(100)]


def pagi_view(request):

    # Создадим переменную page_number куда поместим номер запрашиваемой пользователем страницы из GET параметра:
    page_number = int(request.GET.get('page', 1))  # по умолчанию будет выводиться страница 1.

    # Создаем объект класса Paginator (принимает контент и кол-во одновременно отображаемых элементов на странице)
    paginator = Paginator(CONTENT, 10)

    # В переменную page передаем параметр page_number с номером страницы для отображения.
    page = paginator.get_page(page_number)

    # Помещаем страницу page в переменную context для передачи в шаблон страницы.
    context = {
        'page': page
    }

    return render(request, 'pagi.html', context)
```

* **Шаблон:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Пагинатор</title>
</head>
<body>
    {% for el in page %}
        <p>{{ el }}</p>
    {% endfor %}

    {% if page.has_previous %}
    <a href='?page={{ page.previous_page_number }}'> Назад </a>
    {% endif %}

    {% if page.has_next %}
     <a href='?page={{ page.next_page_number }}'> Вперед </a>
    {% endif %}
</body>
</html>
```
    
    
* **В результате на стартовой странице `http://127.0.0.1:8000/pagi/?page=1` мы получим:** 
```
0

1

2

3

4

5

6

7

8

9

Вперед
```
***
* **Нажав "Вперед" мы перейдем на вторую страницу `http://127.0.0.1:8000/pagi/?page=2` со следующем содержанием:** 
```
10

11

12

13

14

15

16

17

18

19

Назад Вперед
```
***


```python

```
