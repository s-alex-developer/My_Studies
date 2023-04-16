_Последние изменения внесены: 14.04.2023_

[Видео лекции (перейти и скачать)](/study_materials/DataBase/PostgreSQL/Netology/video/creatdb_and_connect_psql.mp4)

# Создание БД, подключение через psql

## 1. `createdb` - создание базы данных PostrgeSQL

* `createdb` - одна из программ устанавливаема совместно с PostrgeSQL
* Служит для удобного создания БД в командной строке
* Для создания новой БД необходимо:
    * В командной строке ввести команду `createdb`.
    * Используя ключ `-U` указать имя пользователя, от чьего имени будет создана новая БД (в Windows по умолчанию супер-пользователь **postgres**).
    * Далее указать название БД.
    * Ввести пароль пользователя для подтвержения создания БД.

> *Итоговая команда будет выглядеть так:* `createdb -U postgres test`

* Если в результате выплнения команды не произошло никаких ошибок, значит БД успешно создана.

## 2. `psql` - подключение к БД PostgreSQL в командной строке.

* Для подключения необходим выполнить команду `psql -U имя_пользователя -d имя_БД`
* Вводим пароль пользователя и подключаемся к управлению БД.

* Используем команду `help` для ознакомления с основными возможностями.
* Команду `\?` - для доступа к основным командам
* Чтобы выйти из режима просмотра вводим `q`
* Для выхода из режима управления БД необходимо ввести `\q`

## 3. `dropdb` - удаление БД

* Для удаления БД необходимо выполнитькоманду `dropdb -U имя_пользователя имя_БД`
* Вводим пароль пользователя, тем самым подтверждая удаление БД.
* Отсутствие сообщения об ошибках говорит о том, что БД успешно удалена и подключится к ней больше не получится.


```python

```