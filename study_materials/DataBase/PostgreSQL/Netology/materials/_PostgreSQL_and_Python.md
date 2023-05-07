*Последние изменения внесены 08.05.2023*

# Работа с PostgreSQL из Python

### Содержание:
    1. Работа с БД из Python с помощью драйвера psycopg2
    2. Создание таблиц и CRUD операции.

***

## 1. Работа с БД из `python` с помощью драйвера `psycopg2`

* Для подключения к БД из **Python** нужен **драйвер** — это специальная библиотека, которая может взаимодействовать с БД.
* Для **PostgreSQL** таким драйвером является `psycopg2`.
* Для популярных операционных систем есть уже готовая, собранная из исходного кода, версия — `psycopg2-binary`.

### 1.1 Для установки бибилотеки драйвера необходимо выполнить в командной строке следующую команду:

`pip install psycopg2-binary`


### 1.2 Необходимо создать БД, к которой будем подключаться:

`createdb -U postgres netology_db`

* Где: 
    * **createdb** - команда создания БД 
    * **-U** - это ключ обозначающий имя пользователя.
    * **postgres** - имя пользователя postgreSQL по умолчанию.
    * **netology_db** - имя создаваемой БД.

### 1.3 Функции `.connect()` и `.close()` - подключение к БД и отключение от БД из Python.

```python
import psycopg2

conn = psycopg2.connect (database="netology_db" , user="postgres" , password="postgres" )  
```

* Объект `conn` является объектом подключения к БД **netology_db**.
* Если такой БД не существует или неверно указаны `user` и `password` — будет ошибка!

**>>> Подключение к БД занимает ресурсы компьютера.**

После того как поработали с БД, необходимо закрыть соединение, как и при работе с файлом:

```python
import psycopg2

conn = psycopg2.connect (database="netology_db" , user="postgres" , password="postgres" )
# работа с соединением
conn.close()
```

**>>> Для того чтобы не закрывать соединение `conn` вручную, можно воспользоваться контекстным менеджером:**
    
```python
import psycopg2

with psycopg2.connect (database="netology_db" , user="postgres" , password="postgres" ) as conn:
# работа с соединением
```

### 1.4 `.cursor()` - выполнение SQL-запросов.

* Чтобы выполнить SQL-запрос необходим специальный объект курсор — `cursor`. 
* Этот объект выполняет запросы и получает данные в ответ.

**>>> Получить объект курсор можно из подключения к БД:**

```python
cur = conn.cursor()
```

**>>> Теперь можно взаимодействовать с БД:**
* `cur.execute()` — выполнить одну команду
***
* `cur.executemany()` — выполнить несколько команд
***
* `cur.fetchone()` — получить одну строку (при вызове данного метода автоматически выполняется commit)
***
* `cur.fetchmany()` — получить несколько строк (при вызове данного метода автоматически выполняется commit)
***
* `cur.fetchall()` — получить все строки (при вызове данного метода автоматически выполняется commit)

**>>> После окончания работы с курсором его нужно закрыть:**
```python
cur. ()close
```

**>>> Для того чтобы не закрывать курсор вручную, можно воспользоваться контекстным менеджером:**
```python
with conn.cursor() as cur:
# работаем с курсором
# после выхода из блока курсор закроется автоматически
```

### 1.5 Tранзакции: `commit` и `rollback`

**Tранзакция** — это способ применить сразу все изменения или не применить ничего.

(Пример) `Транзакция`:
1. **Шаги:**
    * Списать со **счёта 1** некоторую сумму.
    * Зачислить эту сумму на **счёт 2**.
2. Если в одном из шагов возникнет ошибка, то данные могут быть испорчены. 
    * Деньги уже будут списаны со **счёта 1**, но так и не зачислятся на **счёт 2**.


* По умолчанию **SQL** — запросы не отправляются в БД, а накапливаются в памяти. 
* Чтобы выполнить запросы в БД, необходимо вызвать `commit` — это выполнит все запросы, описанные выше:

### >>> `commit`
```python
conn = psycopg2.connect(database="netology_db" , user= "postgres"  , password="postgres" )

with conn.cursor() as cur:
    cur.execute("CREATE TABLE student(id SERIAL PRIMARY KEY, name VARCHAR(40));") # не забывайте точку с запятой в конце
    conn.commit() # применить все операции выше
```

### >>> `rollback`
```python
conn = psycopg2.connect(database="netology_db" , user= "postgres"  , password="postgres" )

with conn.cursor() as cur:
    cur.execute("CREATE TABLE student(id SERIAL PRIMARY KEY, name VARCHAR(40));") # не забывайте точку с запятой в конце
    conn.rollback() # отменит все операции выше
```

## 2. Создание таблиц и`CRUD` операции.

### 2.1 `CRUD`

* **CRUD** (Create, Read, Update, Delete) - стандартный набор операций для управления данными.

**>>> Пример стандартной конструкции запросов:**
```python
conn = psycopg2.connect(database='TEST', user='postgres', password='*****')
cur = conn.cursor()

cur.execute('Запрос 1')
...
cur.execute('Запрос n')

conn.commit()
conn.close()
```
* Требует `commit` для выполнения транзакции.
* Требует закрытия соединения `.close()`.
* Можно применить `.rollback()` чтобы транзакция не выполняласб и БД оставалась без изменений. 

**>>> Пример конструкции запроса с применением менеджера контекста:**
```Python
import psycopg2

with psycopg2.connect(database='TEST', user='postgres', password='*****') as conn:
    with conn.cursor() as cur:
        cur.execute('Запрос 1')
        ...
        cur.execute('Запрос n')
```
* Не требует применения `.commit()`
* Не требует закрытия соединения `.close()`

### 2.2 `Удаление таблицы.`

**>>> Пример кода:**
```python
import psycopg2

with psycopg2.connect(database='TEST', user='postgres', password='17111985') as conn:
    with conn.cursor() as cur:

         cur.execute("""
         DROP TABLE base_one, base_two;
         """)
```

### 2.3 `Создание таблиц.`

**>>> Пример кода:**
```python
import psycopg2

with psycopg2.connect(database='TEST', user='postgres', password='*****') as conn:
    with conn.cursor() as cur:

        cur.execute("""
        CREATE TABLE IF NOT EXISTS base_one(
             PRIMARY KEY (id),
                  id SERIAL,
                name VARCHAR(50) NOT NULL,
              amount SMALLINT DEFAULT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS base_two(
             PRIMARY KEY (id),
                  id SERIAL,
                name VARCHAR(50) NOT NULL,
              amount SMALLINT DEFAULT NULL
        );
        """)
```

### 2.4 `Добавление данных.`

**>>> Пример кода:**
```python
import psycopg2

with psycopg2.connect(database='TEST', user='postgres', password='17111985') as conn:
    with conn.cursor() as cur:

        cur.execute("""
        INSERT INTO base_one(id, name, amount)
        VALUES (1, 'apples', 10),
               (2, 'banana', 1),
               (3, 'pear', 1);
        """)
```

`RETURNING` - после выполнения запроса и добавления данных в БД позволяет вернуть из БД указанные данные в качестве обратной связи (как подтверждение выполнениия запроса) или для дальнейшей обработки.

**>>> Дополним код выше:**
```python        
    cur.execute("""
        INSERT INTO base_one(id, name, amount)
        VALUES (1, 'apples', 10),
               (2, 'banana', 1),
               (3, 'pear', 1)
               RETURNING name;
        """)
```

**>>> Получим одно значение при помощи `fetchone()`:**
```python
print(cur.fetchone())
```
('apples',)

**>>> Получим несколько значение при помощи `fetchmany()` и параметра в скобках:**
```python
print(cur.fetchmany(2))
```
[('apples',), ('banana',)]

* Поскольку нам возвращается список, то к его элементам можно обращаться по индексам:
```python
print(cur.fetchmany(2)[1])
```
('banana',)  

**>>> Получим все значения при помощи `fetchall()`:**
```python
print(cur.fetchall())
```
[('apples',), ('banana',), ('pear',)]

### 2.5 `Извлечение данных.`

Из той же таблицы, с котороый мы работали выше получим данные:
```python
        cur.execute("""
            SELECT * FROM base_one;
        """)
        print(cur.fetchall())  # извлечь все строки

        cur.execute("""
            SELECT * FROM base_one;
        """)
        print(cur.fetchone())  # извлечь одну строку (аналог LIMIT 1)

        cur.execute("""
            SELECT * FROM base_one;
        """)
        print(cur.fetchmany(2))  # извлечь одну строку (аналог LIMIT N)
```

*Получим соответсвующие результаты:*
```
[(1, 'apples', 10), (2, 'banana', 1), (3, 'pear', 1)]
(1, 'apples', 10)
[(1, 'apples', 10), (2, 'banana', 1)]
```

**Фильтрация `WHERE`**

* Для той же таблицы выполним три варианта SELECT запроса:

```python
   cur.execute("""
                SELECT id FROM base_one WHERE name='apples';
                """)
        print(cur.fetchone()) # явно указываем параметр фильтрации

        cur.execute("""
                SELECT id FROM base_one WHERE name='{}';
                """.format('banana'))  # плохо - возможна SQL инъекция
        print(cur.fetchone())

        cur.execute("""
                SELECT id FROM base_one WHERE name=%s;
                """, ('pear',))  # хорошо, обратите внимание на кортеж
        print(cur.fetchone())
```

*Получим соответсвующие результаты:*
```
(1,)
(2,)
(3,)
```
* **SQL-инъекция** (SQLi) - это уязвимость веб-безопасности, которая позволяет злоумышленнику вмешиваться в запросы, которые приложение делает к своей базе данных. 
* Как правило, это позволяет просматривать данные, которые он обычно не может получить. 
* Это могут быть других пользователей, или любые другие данные, доступ к которым имеет само приложение.

### 2.6 Пример использования SQL запросов внутри функций Python.

* Создадим и наполним таблицу БД.
* Напишем функцию принимающую два аргумента:
    * **курсор**
    * значение поля **name** в созданной таблице БД **base_one**.
* Функция должна возвращать **id** записи.
```python
import psycopg2


def get_course_id(cursor, name: str) -> int:
    cursor.execute("""
            SELECT id FROM base_one WHERE name=%s;
        """, (name,))
    return cur.fetchone()[0]


with psycopg2.connect(database='TEST', user='postgres', password='17111985') as conn:
    with conn.cursor() as cur:

        cur.execute("""
        DROP TABLE base_one;
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS base_one(
             PRIMARY KEY (id),
                  id SERIAL,
                name VARCHAR(50) NOT NULL,
              amount SMALLINT DEFAULT NULL
        );
        """)

        cur.execute("""
        INSERT INTO base_one(id, name, amount)
        VALUES (1, 'apples', 10),
               (2, 'banana', 1),
               (3, 'pear', 1)
               RETURNING name;
        """)

        python_id = get_course_id(cur, 'pear')
        print('pear_id', python_id)
```


*Получим результат:*
```
pear_id 3
```

### 2.7 Обновление данных.

* Используем все ту же таблицу и обновим данные поля **name** используя в качестве параметра фильтрации значение полня **id**

```python
        cur.execute("""
            UPDATE base_one SET name=%s WHERE id=%s RETURNING id, name, amount
            """, ('grapes', 3)
            )
        print(cur.fetchone())
```

*Получим результат:*
```
(3, 'grapes', 1)
```

### 2.8 Удаление данных.

* Удалим только что измененную строку и проверим результат получив все данные из таблицы **base_one**:
```python
        cur.execute("""
            DELETE FROM base_one WHERE id=%s
            """, (3,)
            )

        cur.execute("""
                    SELECT * FROM base_one;
                """)
        print(cur.fetchall())
```

*Получим результат:*
```
[(1, 'apples', 10), (2, 'banana', 1)]
```
* Запись с **id = 3** удалена из таблицы.


```python

```
