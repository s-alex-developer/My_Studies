# Django. Общая информация.

* **Django** — фреймворк для быстрого создания веб-приложений, полностью
написанный на Python.

* **Django** является очень популярным проектом и используется многими
крупными компаниями.
## 1. Почему DJANGO? 
<details>
    <summary>смотреть</summary> 
    
        1. Грамотно спроектированная архитектура
        2. Прозрачная работа с базой данных
        3. Серьезное отношение к безопасности
        4. Огромное количество библиотек и написанного кода
        5. Подробная документация (на английском) 
        
</details>

## 2. Установка:
<details>
<summary>смотреть</summary>
    
* Для установки Django, выполните команду в консоли:

        pip install django

* Чтобы убедиться, что все установилось корректно:

      python -m django --version
  
</details>

## 3. Что такое проект и приложение?

<details>
<summary>смотреть</summary>

Под **проектом** можно понимать полноценный сайт. 

Это:
* коллекция настроек;
* база данных;
* подключенные приложения.

*Например*, **YouTube** - *это проект*

* **Приложени**е — это изолированная часть функциональности. 
* Приложения могут переиспользоваться в различных проектах. 
* Ближайшая аналогия — модули в Python.
  
</details>

## 4. Создание проекта:

<details>
<summary>смотреть</summary>
    
* **Необходимо выполнить команду:** 

        django-admin startproject dj_study .

    * где `dj_study` - имя проекта
    * Указывая через пробел точку в конце структура создается в корневом каталоге проекта, а не в дополнительной папке.
    * Получим следующую структуру:
    ```
        Django 
        ├──.dj_venv
        ├── dj_study
        │    ├── __init__.py
        │    ├── asgi.py
        │    ├── settings.py   (настройки проекта)
        │    ├── urls.py   (пути - адреса страниц)
        │    └── wsgi.py (файл для подключеня веб-сервера)
        └── manage.py  (Управляющий файл Django для запуска всех сервисных команд)
    ```
</details>

## 5. Создание приложения

<details>
<summary>смотреть</summary>
    
* **Приложение** в **Django** — это своеобразный модуль с некоторой функциональностью. 
* Например, приложение для работы с email, с пользователями и т.д.

`manage.py` — запускает команды в контексте **Django**-приложения

**Создание приложения:**

    python manage.py startapp main_app 

* где `main_app` название приложения.
* название подбирается исходя из функционала приложения и должно отражать суть выполняемых действий.

* В результате выполнения команды **Django** создаст готовую структуру приложения:

        apps
        ├── migrations
        │    └── __init__.py
        ├── __init__.py
        ├── admin.py   (модуль работы с административной панелью)
        ├── apps.py   (настройки приложения)
        ├── models.py   (работа с моделями БД)
        ├── tests.py   (тесты приложения)
        └── views.py   (контроллеры - классы и функции обработки входящих запросов)

* После создания приложения информацию о нем необходимо внести в модуль `dj_study\settings.py`:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    
        'main_app'
    ]
    ```
* Если не выполнить данное действие приложение будет невидимо для сервисных команд, например `makemigrations`.
  
</details>

## 6. Клиент и сервер.

<details>
<summary>смотреть</summary>

**Клиент:**
    
1. Программа, которая хочет получить информацию;
2. Физическое устройство, на котором работает программа-клиент.

**Сервер:**
    
1. Специальная программа, которая дает информацию;
2. Физическое устройство, на котором запущена программа-сервер.

* Обычно **Клиент** и **Сервер** расположены на разных вычислительных машинах и взаимодействуют между собой по различным протоколам, но они могут быть расположены и на одной машине.


* **Локальное раположение** (на одной машине) **Клиента** и **Сервера** удобно на тапе разработки проекта.


* Веб-приложение реализует **клиент-серверное** взаимодействие.


* Пользователи шлют запросы к серверу, он выдает им результат в виде HTML или JSON данных.

**Django**-проект выступает в роли сервера. 

* Для того чтобы запустить проект, выполните команды:
    
        python manage.py migrate

*  Создает базу данных, если мы планируем использовать встроенные возможности **Django** и использовать БД SQL-Lite, не создавая внешнюю БД.

  * При первом запуске команды, для своей работы **Django** по умолчанию создаст 14 служебных миграций(таблиц БД), которые поместит в директорию `db_sqlite3`.


    python manage.py runserver

* Запускает проект, остановить сервер можно сочетанием клавиш `CTRL+C`
* После выполнения команды мы увидим служебную информацию и адрес по которому мы можем открыть наш проект в браузере:

    ```
    Performing system checks...

    System check identified no issues (0 silenced).
    July 13, 2023 - 16:23:48
    Django version 4.2.3, using settings 'dj_study.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

    ```
</details>

## 7. Подключение сторонней БД к проекту на Django (на примере PostgreSQL)

Создаем базу данных выполнив команду:

    createdb -U postgres dj_database
* где `postgres` - имя пользователя, а `dj_database` - имя базы данных.
* действие необходимо подтвердить паролем.

Устанавливаем драйвер для БД **PostgreSQL**:

    pip install psycopg2-binary

После создания базы данных нам необходимо изменить настройки проекта:

* Заходим в модуль `dj_study\settings.py`
* Находим настройки БД (по умолчанию):

  ```python
  # Database
  # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
  }

* Вносим изменения в настройки:

  ```python
  # Database
  # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_database',
        'USER': 'postgres',
        'PASSWORD': '17111985'
    }
  }
  
* Выполним команду:

      python manage.py migrate

* Ознакомимся с результатом:

<details>
    <summary> Созданные миграции Django (по умолчанию) </summary>
      
>>> Вставить фото >>> сюда ![](1)

</details>

## 8. MVC и Django

* **Django** генерирует структуру проекта самостоятельно. Благодаря этому
даже новые разработчики знают, где и что можно искать.


* При разработке **Django**-приложений очень важно придерживаться
соглашений.


* Проекты на **Django** должны придерживаться паттерна `MVC`:

  `model-view-controller` (модель-представление-контроллер).

**DJANGO** и разделение ответственности:

* управление логикой при ответе -> `view`
* как будет выглядеть страница -> `template`
* состояние приложения -> `model`

> Правило: не мешать всё в одну кучу !!!

## 9. В качестве примера добавим сообщение "Hellow World!" на главную страницу проекта.

Создадим функцию `index_page`в модуле `\main_app\views.py`:

```python
from django.http import HttpResponse

def index_page(request):

    """ Функция отправит текст на указанную в модуеле urls.py страницу проекта. """

    message = "Hello World!"

    return HttpResponse(message)
```

Добавим пути в модуль `\dj_study\urls.py`:

```python
from main_app.views import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name="Index")
]
```
Запустим сервер, перейдем на главную страницу проекта и увидим результат:

>>>Вставить фото >>> сюда ![Фото](2)

## 10. Добавление и выгрузка данных из БД на страницу проекта:

Добавим модель создания таблицы БД для приложения `main_app` в модуль  `\main_app\models.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'main_app'
]
```

Выполним команду: `python manage.py makemigrations` для создания первой записи миграции `\main_app\migrations\0001_initial.py`

Получим результат:

>>>Вставить фото >>> сюда ![Фото](3)

>>>Вставить фото >>> сюда ![Фото](4)

* Каждая запись миграции это своеобразный `"git commit"`, который позволяет нам детально фиксировать каждое действие и при необходимости откатить изменения.

Далее выполнит команду `python manage.py migrate` чтобы добавить все миграции в БД и ознакомимся с результатом:

>>>Вставить фото >>> сюда ![Фото](5)

**Добавим данные в созданную таблицу:**

Сделать это можно 4-мя способами:
1. При помощи скрипта СУБД (_в нашем случае **DBeaver**_).


2. При помощи встроенного интерпретатора **Django** (_расширенная версия **Python Shell**_). 


   * Вызывается командой: `python manage.py shell`
   * Данный интерпретатор имеет доступ ко всем установленным в проекте модулям.
   * Чтобы сделать запись в БД необходимо выполнить последовательность действий:
     * `from main_app.models import Product`
     * `product = Product(name='Арбуз', description='Зеленый снаружи, спелый и вкусный внутри.', price=50)`
     * ` product.save()`
     * Запись должна появится в таблице БД `main_app_product`:
     >>>Вставить фото >>> сюда ![Фото](6)

3. При помощи встроенных методов для работы с моделями в Django:

  * Используем менеджер `.objects` и метод `.create()`:
    * Выполним команду:
    
      `Products.objects.create(name='Дыня', description='Желтая снаружи, белая и сладкая внутри.', price=30)`
    
    * В случае успешного выполнения увидим сообщение:
      
      `<Products: Модель: Дыня, описание: Желтая снаружи, белая и сладкая внутри., стоимость: 30 руб.>`
    * Запись должна появится в таблице БД `main_app_product`:
     >>>Вставить фото >>> сюда ![Фото](7)

4. При помощи встроенной административной панели **Django**:
   * Взаимодействие происходит через модуль `admin.py`, который есть в каждом приложении.
   * Для работы с административной панелью нам необходимо создать учетную запись ****:
     * Выполним команду: `python manage.py createsuperuser`
     * Далее необходимо указать имя пользователя, e-mail, пароль и подтвердить действие:
     ``` 
     Username: Алексей
     Email address: 1@gmail.com
     Password:
     Password (again):
     This password is entirely numeric.
     Bypass password validation and create user anyway? [y/N]: y
     Superuser created successfully.
     ```
     * Учетная запись администратора создана.
     * Запускаем сервер и переходим на страницу `http://127.0.0.1:8000/admin`
     * Вводим логи и пароль созданной учетной записи **Администратора**
        >>>Вставить фото >>> сюда ![Фото](8)
     * Переходим в раздел с БД и добавляем новую запись "Апельсин" в таблицу "Products"
        >>>Вставить фото >>> сюда ![Фото](9)
        >>>Вставить фото >>> сюда ![Фото](10)
     

   * Открываем модуль `\main_app\admin.py` и регистрируем модель `Product`:
       ```python
       from main_app.models import Product

       admin.site.register(Product)
       ```

Создаем контролер в модуле `\main_app\views.py` для выгрузки данных из таблицы БД `main_app_product`:

```python
from main_app.models import Product


def products_list(request):

    """ Функция возвращает из таблицы БД 'main_app_product' все записи. """

    product = Product.objects.all()

    return HttpResponse(product)
```

В модуле `\dj_study\urls.py` импорт функции `products_list` прописываем путь до страницы:

```python
from main_app.views import index_page, products_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name="Index"),
    path('products/', products_list, name="Listing"),
]
```
Запускаем сервер, переходим на страницу `http://127.0.0.1:8000/products/` и смотрим результат:

>>>Вставить фото >>> сюда ![Фото](11)

* Произведена последовательная выгрузка данных из БД, данные слиты воедино, без какого-либо форматирования.

Добавим простейшее форматирование страницы `http://127.0.0.1:8000/products/` при помощи HTML:
* необходимо создать папку `templates` где будут храниться шаблоны разметки страниц.
* папку `templates` можно создавать в корневом каталоге и там создавать отдельные папки для каждого приложения или же отдельно в каждом каталоге приложения.

Создадим папку `\main_app\templates\` и файл шаблона `list.html`:

>>>Вставить фото >>> сюда ![Фото](12)

* Файл создается с базовой разметкой.

Страницы HTML создаваемые при помощи Django дают возможность использования дополнительного функционала:

* В нашем примере из БД на страницу проекта мы выгружаем не одну запись, а все.
* При помощи специальных тегов мы можем произвести выгрузку при помощи цикла и к каждому результату применить форматирование:
   
   ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Список продуктов</title>
    </head>
    <body>
    <h1>Список продуктов</h1>
    {% for item in products %}
        <h2>{{ item.name }}</h2>
        <h3>{{ item.description }}</h3>
        <p>{{ item.price }}</p>
        <p>*****************************************************************</p>
    {% endfor %}
    </body>
    </html>
  
* Внесем изменения в контроллер в модуле `\main_app\views.py`:

    ```python
    from django.shortcuts import render
    from main_app.models import Product


    def products_list(request):

    """ Функция возвращает из таблицы БД 'main_app_product' все записи. """

    product = Product.objects.all()

    template_name = 'list.html'

    # 'products' - это ключ, указанный в файле шаблона list.html в качестве итерируемого объекта в цикле for
    return render(request, template_name, {'products': product})
  
* Запустим сервер, перейдем на страницу `http://127.0.0.1:8000/products/` и посмотрим результат:

    >>>Вставить фото >>> сюда ![Фото](13)

## 11. Работа с урлами. Роутинг в Django.

**View и гипертекст:**
* Пользователь взаимодействует с системой через гипертекст: клики, скролы, нажатия клавиш. 
* Сервер реагирует на эти взаимодействия и с помощью `view` подготавливает новое состояние — ответ.

**Маршрутизация:**
```python
urlpatterns = [
path('', home_view, name='home'),
]
```
*  `''` (первый параметр) — фактический адрес, который будет указан в адресной строке браузера.


* `home_view` (второй параметр) — **view-функция**, которая будет вызвана при обработке запроса.


* `name` (третий параметр) — позволяет получать конкретный урл по имени.
Это позволяет приложению не ломаться, если урлы будут меняться и делает код более понятным

## 12. `Revers`

**Revers** - позволяет получить путь по имени.

**Как получить урл по имени:**
```python
urlpatterns = [
    path('', home_view, name='home'),
    path('profile', profile_view, name='profile'),
    path('long/address/orders', orders_view, name='orders')
]
```
Выполним следующие действия в **Django shell**:

* `python manage.py shell`


* `from django.urls import reverse`


* `reverse('orders')`
  * _Результат:_ `'/long/address/orders'`


* `reverse('profile')`
  * _Результат:_ `'/profile'`

    
* `reverse('product_details', args=[1])` (*данный пример будет использован ниже*)
  * _Результат:_ `'/products/1/'`


* `reverse('product_details', kwargs={'product_id': 2})`  (*данный пример будет использован ниже*)
  * _Результат:_ `'/products/2/'`

## 13. Вывод информации о продукте на отдельную страницу.

Создадим новый контроллер в модуле `\main_app\views.py`:

```python
from django.shortcuts import render, get_object_or_404
from main_app.models import Product


def product_details(request, product_id):

    """ Возвращает одну запись из таблицы БД по указанному id """

    product = get_object_or_404(Product, id=product_id)

    template_name = 'product.html'

    return render(request, template_name, {'item': product})
```
* Функция `get_object_or_404` возвращает объект класса или вызывает ошибку `404`

Создадим новый шаблон `product.html` в `\main_app\templates\`:

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Выбранные продукт</title>
</head>
<body>
    <h1>{{ item.name }}</h1>
    <h2>{{ item.description }}</h2>
    <p>{{ item.price }}</p>
</body>
</html>
```
В модуле `\dj_study\urls.py` прописываем импорт функции `product_details` путь до страницы продукта с указанным id:
```python
from main_app.views import index_page, products_list, product_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name="Index"),
    path('products/', products_list, name="Listing"),
    path('products/<int:product_id>/', product_details, name='product_details'),
]
```
Запускаем сервер и получаем результат:

>>>Вставить фото >>> сюда ![Фото](14)

* На отдельную страницу мы произвели выгрузку товара из таблицы БД с идентификатором `id=1`.

## 14. Перехода между страницами по ссылкам и кнопкам.
 
*Внесем изменения в наши шаблоны:**

В `\main_app\templates\list.html` превратим имена продуктов в гиперссылки:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Список продуктов</title>
</head>
<body>
    <h1>Список продуктов</h1>
    {% for item in products %}
    <a href= "{% url 'product_details' item.id %}"><h2>{{ item.name }}</h2></a>
        <h3>{{ item.description }}</h3>
        <p>{{ item.price }}</p>
        <p>*****************************************************************</p>
    {% endfor %}
</body>
</html>
```

* В `\main_app\templates\product.html` добавим кнопку **Вернуться к списку продуктов**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Выбранные продукт</title>
</head>
<body>
    <h1>{{ item.name }}</h1>
    <h2>{{ item.description }}</h2>
    <p>{{ item.price }}</p>
    <a href="{%url 'Listing'%}"><button>Вернуться к списку продуктов.</button></a>
</body>
</html>
```

Получим результат: 

>>>Вставить фото >>> сюда ![Фото](15)

## 15. Как дебажить Django-проект.

### 1. `print` - функции
* **Django-проект** — это Python приложение. 


* Поэтому можно использовать возможности **Python** и использовать print’ы для дебага и отладки кода.

### 2. `manage.py shell`
* Запускает интерактивный интерпретатор в контексте **Django** - проекта.

### 3. `Сообщения об ошибках Django на веб страницах проекта при попытке их загрузки.`

* Средство фреймворка. 


* Если включен DEBUG-режим, то Django собирает и агрегирует информацию об ошибке.

### 4. `Debug и точки остановки (они же breakpoints)`
* Удобнее всего использовать в **IDE Pycharm** или **VS Code**.
  * Необходимо выполнить настройку `Run\Debug configuration`.
  * Переходим в настройки:
  >>>  Вставить фото >>> сюда ![Фото](16)
  * Заполняем параметры: `name`, `Script path`, `Parameters`, `Python interpreter`
  >>>Вставить фото >>> сюда ![Фото](17)
  * Далее используя конфигурацию `manage.py` мы можем запускать наш сервер и **debug** режим.
  >>>Вставить фото >>> сюда ![Фото](18)
  * Сообщения об ошибках **Django** на веб страницах проекта при попытке их загрузки подскажут нам в каких модулях 
  и строках кода возникли ошибки.
  * Расстановка breakpoints, в **debug** режиме мы сможем отслеживать каждый шаг выполнения кода и находить ошибки.
