*Последние изменения внесены 23.05.2023*

# Концепт ORM

# 1. Object-Relational Mapping

> **ORM** (объектно-реляционное отображение) — это дополнительный способ взаимодействия с БД из кода, который работает с таблицами и запросами к БД как с классами, объектами и методами в ООП.

* ORM работает поверх стандартных SQL-запросов. 
* Все правила и закономерности реляционных связей остаются

> **SQLAlchemy** - Популярная **ORM** для **Python**.

**>>> Для установки данной библиотеки в командной строке необходимо выполнить команду:**

`pip install sqlalchemy`

### Плюсы и минусы использования `ORM`

**Плюсы:**
* Необязательно знать SQL и специальные функции СУБД
* Возможность десериализации (распаковки) результата из БД в удобном формате для API или обработки.
* Не нужно придумывать сложные парсеры массивов, работаем с готовыми структурами данных
* Один и тот же код может работать в разных БД, если на это рассчитана ORM
* Разработчиками ORM продуманы примитивные вопросы безопасности, экранирования и оптимизации запросов

**Минусы:**
* Изначально не очевидны итоговые запросы
* Ограничения и читаемость при построении сложных,

# 2. SQLAlchemy и Абстракции ORM

## 2.1 Абстракция `Сессия`

### Создание движка `engine` и сессии `Session`

Создадим `сессию` и `движок` для работы с БД в файле **main.py**
```python
import sqlalchemy
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:17111985@localhost:5432/testbase' # DSN (Data Source Name) - имя источника данных:

engine = sqlalchemy.create_engine(DSN)  # Создание движка.

Session = sessionmaker(bind=engine)  # Создание сессии (класс Session, аналог cursor'a):

session = Session()  # Cоздание сессии (session - объект класса Session)

""" Блок кода сессии """

session.close()  # После выполнения кода ссессию необходимо закрыть.
```

**Описание кода выше:**
* Импортируем необходимые модули и бибилиотеки.
* Создаем переменную с именем **DNS (Data Source Name)** которой сохраним параметры необходимые для работы с БД:
    * `postgresql` - драйвер.
    * `postgres:17111985` - имя пользователя и пароль БД.
    * `localhost:5432` - стандартные имя хостинга и порта для БД postgreSQL установленной на нашем ПК.
    * `testbase` - имя нашей БД.
* Создаем движок **engine** при помощи функции **.create_engine()** и переданного в нее в качетстве аргумента **DSN**.
* Далее при помощи функции **sessionmaker()** создаем класс **Session** и связываем через параметр **bind=engine** сессию с нашим движком.
* Созданный класс **Session** умеет создавать сессии работы с БД, отправлять и получать данные из БД.
* Для открытия сессии по работе с БД необходимо создать объект класса **session**
* По окончанию работы с БД сессию небходимо закрыть - **session.close()**

## 2.2 Абстракция `Модель`

> **Модель** - в **SQLalchemy** это специальный клаасс, который наследуется от базового класса, то есть является подклассом родительского класса.

В файле **models.py** создадим `модели` и `методы` работы с ними:

```python
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Course(Base):
    
    ''' Модель создания таблицы course в БД '''

    __tablename__ = 'course'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

    
    # Переопределяем метод __str__ подкласса Course для форматирования вывода данных на экран через функцию print():
    def __str__(self):
        return f'Course {self.id}: {self.name}'


class Homework(Base):
    
        ''' Модель создания таблицы homework в БД '''

    __tablename__ = 'homework'

    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey('course.id'), nullable=False)
    
    
    # Переопределяем метод __str__ подкласса Homework для форматирования вывода данных на экран через функцию print():
    def __str__(self):
        return f'Homework {self.id}: ({self.number}, {self.description}, {self.course_id})'
    
    # Создаем свойство course для создания связи моделей Course и Homework
    course = relationship(Course, backref='homeworks') 


def delete_tables(engine):
    
    ''' Метод удаления всех таблиц (моделей) из нашей БД '''
    
    Base.metadata.drop_all(engine)


def create_tables(engine):
    
    ''' Метод создания всех таблиц (моделей) в нашей БД '''
    
    Base.metadata.create_all(engine)
```

## 2.3 Создание таблиц в БД и наполнение их данными.

Вернемся в файл **main.py** и добавим код создающий таблицы БД и добавляющий данные в них.

```python
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import delete_tables, create_tables, Course, Homework

DSN = 'postgresql://postgres:17111985@localhost:5432/testbase' # DSN (Data Source Name) - имя источника данных:
engine = sqlalchemy.create_engine(DSN)  # Создание движка.

# Производим удаление таблиц (бывает необходимо при отладке кода)
delete_tables(engine)

# Создаем таблицы:
create_tables(engine)

Session = sessionmaker(bind=engine)  # Создание сессии (класс Session, аналог cursor'a):
session = Session()  # Cоздание сессии (session - объект класса Session)


# Добавляем название курсов в таблицу "course" 
course_1 = Course(name='Python')
course_2 = Course(name='PHP')
course_3 = Course(name='Java')

session.add(course_1) # Добавим данные в сессию для последующего commit'a

session.add_all([course_2, course_3]) # Добавим данные в сессию для последующего commit'a

# Добавим домашние задания в таблицу "homework"
hw_1 = Homework(number=1, description='Простое задание Python', course=course_1)
hw_2 = Homework(number=2, description='Сложное задание Python', course=course_1)
hw_3 = Homework(number=3, description='Простое задание PHP', course=course_2)
hw_4 = Homework(number=4, description='Сложное задание PHP', course=course_2)
hw_5 = Homework(number=5, description='Простое задание Java', course=course_3)
hw_6 = Homework(number=6, description='Сложное задание Java', course=course_3)
session.add_all([hw_1, hw_2, hw_3, hw_4, hw_5, hw_6])

session.commit() # Фиксируем изменения, выполняется транзакция и в случаем отсутсвия ошибок данные будут добавлены в БД.

session.close() # Не забываем закрыть сессию.
```

### `.query()` - получение данных.

**>>> Мы можем получить данные по какой то записи целиком или указам конкретный атрибут модели, соответсвующий конкретному полю в таблице БД:**

```python
print(course_1)
```

*Получим результат:*

```
Course 1: Python
```

* Вывод на экран переопредел в методе `__str__` при создании подкласса (модели) **Course**
* По умолчанию мы бы получили следующий результат **<modul.Course object at 0x000001808A02D810>**

**>>> Обратимся к конкретному атрибуту:**

```python
print(course_1.name)
```

*Получим результат:*

```
Python
```
* При обращении к атрибуту мы получим имменно данные из БД, независимо от того переопределен метод `__str__` или нет.

**>>> Получим все данные из таблиц `"course"` и `"homework"`:**
```python
for c in session.query(Course).all():  # Код работает без .all() см.пример ниже.
    print(c)
```

*Получим результат:*

```
Course 1: Python
Course 2: PHP
Course 3: Java
```

```python
for c in session.query(Homework):
    print(c)
```

*Получим результат:*

```
Homework 1: (1, Простое задание Python, 1)
Homework 2: (2, Сложное задание Python, 1)
Homework 3: (3, Простое задание PHP, 2)
Homework 4: (4, Сложное задание PHP, 2)
Homework 5: (5, Простое задание Java, 3)
Homework 6: (6, Сложное задание Java, 3)
```

### `.filter()` и `.like()`- фильтрация данных.

**>>> Рассмотрим пример и получим все курсы имя, который начинается на заглавную букву латинского алфавита 'P':**

```python 
for c in session.query(Course).filter(Course.name.like('P%')): # регистр имеет значение.
    print(c)
```

*Получим результат:*

```
Course 1: Python
Course 2: PHP
```

**>>> Рассмотрим пример и получим все домашние задания, номер которых больше 3:**

```python 
for c in session.query(Homework).filter(Homework.number > 3):
    print(c)
```

*Получим результат:*

```
Homework 4: (4, Сложное задание PHP, 2)
Homework 5: (5, Простое задание Java, 3)
Homework 6: (6, Сложное задание Java, 3)
```

### `.join` - объединение таблиц.

**>>> Рассмотрим пример объединенного запроса из двух таблиц, с условиями фильтрации по каждой таблице:**

Создадим запрос:
```python
sql_request = session.query(Course).filter(Course.name.like("%H%")).join(Homework).filter(Homework.number > 3)
```

Мы всегда можем ознакомится с **sql** запросом выведя его на экран при помощи функции **print()**
```python
print(sql_request)
```
*Получим резльтат:*
```sql
SELECT course.id AS course_id, course.name AS course_name 
FROM course JOIN homework ON course.id = homework.course_id 
WHERE course.name LIKE %(name_1)s AND homework.number > %(number_1)s
```

**>>> Получим данные из БД по нашему запросу:**
```python
for c in sql_request:
    print(c)
```

*Результат:*
```
Course 2: PHP
```
* Мы получили все курсы из таблицы **course** в имени которых содержится буква **H** и номера домашних работ по этому курсу **больше 3** в связанной таблице **homework**

### `.subquery()` - подзапросы

**>>> Создадим запрос извлекающий из таблицы `"homework"` все домашние задания по курсу с `id=2`:**
    
```python
q = session.query(Homework).filter(Homework.course_id == 2)

for c in q:
    print(c)
```

*Получим резльтат:*
    
```
Homework 3: (3, Простое задание PHP, 2)
Homework 4: (4, Сложное задание PHP, 2)
```

**>>> Преобразуем наш запрос `q` в подзапрос:**
```python
subq = q.subquery() # Проебразование запроса в подзапрос при помощи метода .subquery()

print(session.query(Course).join(subq)) # Основной запрос объединенный с подзапросом при помощи .join()
```
 *Ознакомимся с содержимым объединенного **sql** запроса:*
 ```sql
SELECT course.id AS course_id, course.name AS course_name 
FROM course JOIN (SELECT homework.id AS id, homework.number AS number, homework.description AS description, homework.course_id AS course_id 
FROM homework 
WHERE homework.course_id = %(course_id_1)s) AS anon_1 ON course.id = anon_1.course_id
 ```


**>>> Выполним основной запрос:**
```python
for c in session.query(Course).join(subq):
    print(c)
```
*Получим результат:*
```
Course 2: PHP
```
* В результате мы получили название курса из таблицы **"course"**, который сооответсвует домашним работам полученным при помощи подзапроса из таблицы **"homework"** со значение **course_id=2**.

### `.update()` и `.delete()` - обновление и удаление данных.

Удалим из таблицы **"course"** курс с названием `"PHP"` и имзеним название курса `"Java"` на `"JavaScript"`:

```python
session.query(Course).filter(Course.name == 'PHP').delete()
session.query(Course).filter(Course.name == 'Java').update({'name': 'JavaScript'})
session.commit()


print()
for c in session.query(Course):
    print(c)

session.close()
```

*Получим результаты:*
```
Course 1: Python
Course 3: JavaScript
```


```python

```
