*Последние изменения внесены 01.05.2023*

# Запросы

## 1.1 `DISTINCT` - выборка уникальных значений.

* Оператор `DISTINCT` позволяет выбрать уникальные данные по определенным столбцам.

**В таблице товаров разные товары могут иметь одних и тех же производителей. Например, у нас следующая таблица:**

```sql
CREATE TABLE Products
(
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Manufacturer VARCHAR(20) NOT NULL,
    ProductCount INTEGER DEFAULT 0,
    Price NUMERIC
);
```
```sql
INSERT INTO Products  (ProductName, Manufacturer, ProductCount, Price)
VALUES
('iPhone X', 'Apple', 2, 71000),
('iPhone 8', 'Apple', 3, 56000),
('Galaxy S9', 'Samsung', 6, 56000),
('Galaxy S8 Plus', 'Samsung', 2, 46000),
('Desire 12', 'HTC', 3, 26000);
```

**Выберем всех производителей:**

```sql
SELECT DISTINCT Manufacturer FROM Products;
```
* В результате выполнения запросы мы выведем имена всех производителей хранящихся в таблице в поле **Manufacturer** по одному разу, без повторов, тоесть только уникальные значения.

## 1.2 `ORDER BY` - сортировка.

* Оператор `ORDER BY` позволяет отсортировать значения по определенному столбцу. 
* Например, упорядочим выборку из таблицы **Products** по столбцу **ProductCount**:

```sql
SELECT * FROM Products
ORDER BY ProductCount;
```

**Также можно производить упорядочивание данных по псевдониму столбца, который определяется с помощью оператора `AS`:**

```sql
SELECT ProductName, ProductCount * Price AS TotalSum
FROM Products
ORDER BY TotalSum;
```

**В качестве критерия сортировки также можно использовать сложное выражение на основе столбцов:**

```sql
SELECT ProductName, Price, ProductCount
FROM Products
ORDER BY ProductCount * Price;
```

### >>> `DESC` Сортировка по убыванию
**По умолчанию данные сортируются по возрастанию, однако с помощью оператора `DESC` можно задать сортировку по убыванию.**

```sql
SELECT ProductName, Manufacturer
FROM Products
ORDER BY Manufacturer DESC;
```

**По умолчанию вместо `DESC` используется оператор `ASC`, который сортирует по возрастанию:**

```sql
SELECT ProductName, Manufacturer
FROM Products
ORDER BY Manufacturer ASC;
```

### Cотировка по нескольким столбцам.

**Если необходимо отсортировать сразу по нескольким столбцам, то все они перечисляются через запятую после оператора `ORDER BY`:**

```sql
SELECT ProductName, Price, Manufacturer
FROM Products
ORDER BY Manufacturer, ProductName;
```

* В этом случае сначала строки сортируются по столбцу **Manufacturer** по возрастанию.
* Затем если есть две строки, в которых столбец **Manufacturer** имеет одинаковое значение, то они сортируются по столбцу **ProductName** также по возрастанию. 
* Но опять же с помощью `ASC` и `DESC` можно отдельно для разных столбцов определить сортировку по возрастанию и убыванию:

```sql
SELECT ProductName, Price, Manufacturer
FROM Products
ORDER BY Manufacturer ASC, ProductName DESC;
```

## 1.3 `LIMIT` и `OFFSET` - получение диапазона строк. 

**Оператор `LIMIT` позволяет извлечь определенное количество строк:**

```sql
SELECT * FROM Products
ORDER BY ProductName
LIMIT 4;
```


**Оператор `OFFSET` позволяет указать, с какой строки надо начинать выборку. Например, выберем 3 строки, начиная со 2-й:**

```sql
SELECT * FROM Products
ORDER BY ProductName
LIMIT 3 OFFSET 2;
```

**Если нам надо выбрать вообще все строки, начиная с какой-то определенной, то оператор `LIMIT` можно опустить:**

```sql
SELECT * FROM Products
ORDER BY ProductName
OFFSET 2;
```


**Либо после `LIMIT` указать ключевое слово `ALL`:**

```sql
SELECT * FROM Products
ORDER BY ProductName
LIMIT ALL OFFSET 2;
```

## 1.4 Операторы фильтрации.

### >>> Оператор `IN`

**Оператор `IN` позволяет определить набор значений, которые должны иметь столбцы:**

```sql
WHERE выражение [NOT] IN (выражение)
```

* Выражение в скобках после `IN` определяет набор значений. 
* Этот набор может вычисляться динамически на основании, например, еще одного запроса, либо это могут быть константные значения.

Например, выберем товары, у которых производитель либо **Samsung**, либо **Xiaomi**, либо **Huawei**:

```sql
SELECT * FROM Products
WHERE Manufacturer IN ('Samsung', 'HTC', 'Huawei');
```

**В качестве алтернативы можно было бы проверить все эти значения через оператор `OR`:**

```sql
SELECT * FROM Products
WHERE Manufacturer = 'Samsung' OR Manufacturer = 'HTC' OR Manufacturer = 'Huawei';
```

* Однако использование оператора `IN` гораздо удобнее, особенно если подобных значений очень много.

**С помощью оператора `NOT` можно найти все строки, которые, наоборот, не соответствуют набору значений:**

```sql
SELECT * FROM Products
WHERE Manufacturer NOT IN ('Samsung', 'HTC', 'Huawei');
```

### >>> Оператор `BETWEEN`

**Оператор `BETWEEN` определяет диапазон значений с помощью начального и конечного значения, которому должно соответствовать выражение:**

```sql
WHERE выражение [NOT] BETWEEN начальное_значение AND конечное_значение
```

**Например, получим все товары, у которых цена от 20 000 до 50 000 (начальное и конечное значения также включаются в диапазон):**

```sql
SELECT * FROM Products
WHERE Price BETWEEN 20000 AND 50000;
```

**Если надо, наоборот, выбрать те строки, которые не попадают в данный диапазон, то применяется оператор NOT:**

```sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 20000 AND 50000;
```


**Также можно использовать более сложные выражения.**
***Например, получим товары, запасы которых на определенную сумму (цена * количество):**

```sql
SELECT * FROM Products
WHERE Price * ProductCount BETWEEN 90000 AND 150000;
```

### >>> Оператор `LIKE`
**Оператор `LIKE` принимает шаблон строки, которому должно соответствовать выражение, учитывает регистр.**
**Оператор `ILIKE` работает без учета регистра.**

```sql
WHERE выражение [NOT] LIKE шаблон_строки
```
**Для определения шаблона могут применяться ряд специальных символов подстановки:**

* `%` - соответствует любой подстроке, которая может иметь любое количество символов, при этом подстрока может и не содержать ни одного символа

    * Например, выражение **WHERE ProductName LIKE 'Galaxy%'** соответствует таким значениям как **"Galaxy Ace 2" или "Galaxy S7"**
***
* `_` - соответствует любому одиночному символу

    * Например, выражение **WHERE ProductName LIKE 'Galaxy S_'** соответствует таким значениям как **"Galaxy S7" или "Galaxy S8"**.

**Применим оператор `LIKE`:**

```sql
SELECT * FROM Products
WHERE ProductName LIKE 'iPhone%';
```

## 1.5 Агрегатные функции.

**Агрегатные функции** вычисляют одно значение над некоторым набором строк. 

В **PostgreSQL** имеются следующие **агрегатные функции**:

`AVG` находит среднее значение. 
   * Входной параметр должен представлять один из следующих типов: **smallint, int, bigint, real, double precision, numeric, interval**. 
   * Для целочисленнных параметров результатом будет значение типа **numeric**, для параметров, которые представляют число с плавающей точкой, - значение типа **double precision**.

***

`COUNT(*)`: находит количество строк в запросе

***

`COUNT(expression)`: находит количество строк в запросе, для которых **expression** не содержит значение **NULL**.

***

`SUM`: находит сумму значений

***

`MIN`: находит наименьшее значение

***

`MAX`: находит наибольшее значение

***

`BIT_AND` выполняет операцию побитового умножения (операции логического И) для чисел следующих типов: **smallint, int, bigint, bit.** 
   * Если параметр содержит значение **NULL**, то возвращается **NULL**.

***

`BIT_OR`: выполняет операцию побитового сложения (операции логического ИЛИ) для чисел следующих типов: **smallint, int, bigint, bit.** 
* Если параметр содержит значение **NULL**, то возвращается **NULL**.

***

`BOOL_AND`: выполняет операцию логического умножения для значений типа **bool**. 
* Если входные все значения равны **true**, то возвращается **true**, иначе возвращается **false**.

***

`BOOL_OR`: выполняет операцию логического сложения для значений типа **bool**. 
* Если входные хотя бы одно из значений равно **true**, то возвращается **true**, иначе возвращается **false**.

***

`STRING_AGG(expression, delimiter)`: соединяет с помощью **delimiter** все текстовые значения из **expression** в одну строку.

* В качестве параметра все агрегатные функции принимают выражение, которое представляет критерий для определения значений.
* Зачастую, в качестве выражения выступает название столбца, над значениями которого надо проводить вычисления.
* Если в наборе нет строк, то все агрегатные функции за исключением `COUNT(*)` возвращают значение **NULL**.

### `Avg`
**Функция `Avg` возвращает среднее значение на диапазоне значений столбца таблицы.**

Пусть в базе данных у нас есть таблица товаров **Products**, которая описывается следующими выражениями:

```sql
CREATE TABLE Products
(
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Company VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price NUMERIC NOT NULL,
    IsDiscounted BOOL
);

INSERT INTO Products (ProductName, Company, ProductCount, Price, IsDiscounted) 
VALUES
('iPhone X', 'Apple', 3, 76000, false),
('iPhone 8', 'Apple', 2, 71000, true),
('iPhone 7', 'Apple', 5, 42000, true),
('Galaxy S9', 'Samsung', 2, 46000, false),
('Galaxy S8 Plus', 'Samsung', 1, 56000, true),
('Desire 12', 'HTC', 5, 28000, true),
('Nokia 9', 'HMD Global', 6, 38000, true);
```
**Найдем среднюю цену товаров из базы данных:**

```sql
SELECT AVG(Price) AS Average_Price FROM Products;
```

* Для поиска среднего значения в качестве выражения в функцию передается столбец **Price**. 
* Для получаемого значения устанавливается псевдоним **Average_Price**, хотя можно его и не устанавливать.

**Также мы можем применить фильтрацию. Например, найти среднюю цену для товаров какого-то определенного производителя:**

```sql
SELECT AVG(Price) FROM Products
WHERE Company='Apple';
```

**И, кроме того, мы можем находить среднее значение для более сложных выражений. Например, найдем среднюю сумму всех товаров, учитывая их количество:**

```sql 
SELECT AVG(Price * ProductCount) FROM Products
```

### `Count`

**Функция `Count` вычисляет количество строк в выборке. Есть две формы этой функции:**

* Первая форма `COUNT(*)` подсчитывает число строк в выборке:

```sql
SELECT COUNT(*) FROM Products;
```
* Вторая форма функции вычисляет количество строк по определенному столбцу, при этом строки со значениями **NULL** игнорируются:

```sql
SELECT COUNT(DISTINCT Company) FROM Products;
```

* Оператор `DISTINCT` указывает, что надо взять именно уникальные значения из столбца **Company**.

### `Min` и `Max`

**Функции `Min` и `Max` возвращают соответственно минимальное и максимальное значение по столбцу.** 

Например, найдем минимальную цену среди товаров:

```sql
SELECT MIN(Price) FROM Products;
```

Поиск максимальной цены:

```sql
SELECT MAX(Price) FROM Products;
```

* Данные функции также игнорируют значения **NULL** и не учитывают их при подсчете.

### `Sum`

**Функция `Sum` вычисляет сумму значений столбца.**

Например, подсчитаем общее количество товаров:

```sql
SELECT SUM(ProductCount) FROM Products;
```

**Также вместо имени столбца может передаваться вычисляемое выражение.**

Например, найдем общую стоимость всех имеющихся товаров:

```sql
SELECT SUM(ProductCount * Price) FROM Products;
```

### `BOOL_AND` и `BOOL_OR`

* Допустим, нам надо узнать, есть ли в таблице товары, которые подлежать скидке, то есть у которых **IsDiscounted = true**.
* В этом случае можно выполнить функцию `BOOL_OR`, которая возвращает **true**, если хотя бы одно значение в наборе равно **true**:

```sql
SELECT BOOL_OR(IsDiscounted) FROM Products;
```

Если нам надо узнать, все ли товары подлежат скидке, то можно применить функцию `BOOL_AND`, которая возвращает **true**, если все значения в наборе равны **true**:

```sql
SELECT BOOL_AND(IsDiscounted) FROM Products;
```

### `STRING_AGG`

Функция `STRING_AGG()` объединяет набор строковых значений или значений **bytea**. 

**Например, выберем названия всех товаров:**

```sql
SELECT STRING_AGG(ProductName, ', ') FROM Products;
```

**Или выберем всех производителей:**

```sql
SELECT STRING_AGG(DISTINCT Company, ', ') FROM Products;
```

* Чтобы выбрать уникальных производителей, здесь также применяется оператор `DISTINCT`, иначе у нас бы повторялись значения.

### `Комбинирование функций`

Объединим применение нескольких функций:

```sql
SELECT COUNT(*) AS ProdCount,
       SUM(ProductCount) AS TotalCount,
       MIN(Price) AS MinPrice,
       MAX(Price) AS MaxPrice,
       AVG(Price) AS AvgPrice
FROM Products;
```

## 1.6 Группировка `GROUP BY` и `HAVING`

**Для группировки данных в PostgreSQL применяются операторы `GROUP BY` и `HAVING`, для использования которых применяется следующий формальный синтаксис:**

```sql
SELECT столбцы
FROM таблица
[WHERE условие_фильтрации_строк]
[GROUP BY столбцы_для_группировки]
[HAVING условие_фильтрации_групп]
[ORDER BY столбцы_для_сортировки]
```
**Для рассмотрения операторов возьмем следующую таблицу:**

```sql
CREATE TABLE Products
(
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Company VARCHAR(20) NOT NULL,
    ProductCount INT DEFAULT 0,
    Price NUMERIC NOT NULL,
    IsDiscounted BOOL
);
```

### `GROUP BY`

**Оператор `GROUP BY` определяет, как строки будут группироваться.**

Например, сгруппируем товары по производителю:

```sql
SELECT Company, COUNT(*) AS ModelsCount
FROM Products
GROUP BY Company;
```

* Первый столбец в выражении `SELECT` - **Company** представляет название группы, а второй столбец - **ModelsCount** представляет результат функции `Count`, которая вычисляет количество строк в группе.
* Стоит учитывать, что любой столбец, который используется в выражении `SELECT` (не считая столбцов, которые хранят результат агрегатных функций), должны быть указаны после оператора `GROUP BY`. 
* Так, например, в случае выше столбец **Company** указан и в выражении `SELECT`, и в выражении `GROUP BY`.
* И если в выражении `SELECT` производится выборка по одному или нескольким столбцам и также используются агрегатные функции, то необходимо использовать выражение `GROUP BY`. 
* Так, следующий пример работать не будет, так как он не содержит выражение группировки:

```sql
SELECT Company, COUNT(*) AS ModelsCount
FROM Products;
```

**Другой пример, добавим группировку по количеству товаров:***

```sql
SELECT Company, ProductCount, COUNT(*) AS ModelsCount
FROM Products
GROUP BY Company, ProductCount;
```

**Оператор `GROUP BY` может выполнять группировку по множеству столбцов.**
> **Важно !!!** Если столбец, по которому производится группировка, содержит значение **NULL**, то строки со значением **NULL** составят отдельную группу **!!!** 

**Следует учитывать, что выражение `GROUP BY` должно идти после выражения `WHERE`, но до выражения `ORDER BY`:**

```sql
SELECT Company, COUNT(*) AS ModelsCount
FROM Products
WHERE Price > 30000
GROUP BY Company
ORDER BY ModelsCount DESC;
```

### `HAVING` - фильтрация групп. 

* Оператор `HAVING` указывает, какие группы будут включены в выходной результат, то есть выполняет фильтрацию групп. 
* Его использование аналогично применению оператора `WHERE`.

**Например, сгруппируем по производителям и найдем все группы, для которых определено более 1 модели:**

```sql
SELECT Company, COUNT(*) AS ModelsCount
FROM Products
GROUP BY Company
HAVING COUNT(*) > 1;
```

**При этом в одной команде мы можем использовать выражения `WHERE` и `HAVING`:**

```sql
SELECT Company, COUNT(*) AS ModelsCount
FROM Products
WHERE Price * ProductCount > 80000
GROUP BY Company
HAVING COUNT(*) > 1;
```

* То есть в данном случае сначала фильтруются строки: выбираются те товары, общая стоимость которых больше 80000. 
* Затем выбранные товары группируются по производителям. 
* И далее фильтруются сами группы - выбираются те группы, которые содержат больше 1 модели.

**Если при этом необходимо провести сортировку, то выражение ORDER BY идет после выражения `HAVING`:**

```sql
SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Products
WHERE Price * ProductCount > 80000
GROUP BY Company
HAVING SUM(ProductCount) > 2
ORDER BY Units DESC;
```

* Здесь группировка идет по производителям, и также выбирается количество моделей для каждого производителя (Models) и общее количество всех товаров по всем этим моделям (Units). 
* Затем группы сортируются по количеству товаров по убыванию.

## 1.7 Расширения `GROUPING SETS`, `CUBE` и `ROLLUP` для оператора `GROUPE BY`

В дополнение к оператору `GROUP BY` **PostgreSQL** поддерживает еще три специальных расширения для группировки данных: `GROUPING SETS`, `ROLLUP` и `CUBE`.

### `GROUPING SETS`
**Оператор `GROUPING SETS` группирует получемые наборы отдельно:**

```sql
SELECT Company, COUNT(*) AS Models, ProductCount
FROM Products
GROUP BY GROUPING SETS(Company, ProductCount);
```

* В выражении `SELECT` производится выборка компаний, количества моделей и количества товаров. 
* То есть мы получаем три категории. 
* Оператор `GROUPING SETS` производит группировку по двум столбцам - **Company** и **ProductCount**.
* В итоге будет создаваться две группы: 
    1) компании и количество моделей
    2) количество моделей и количество товаров.



### `ROLLUP`
**Оператор `ROLLUP` добавляет суммирующую строку в результирующий набор:**

```sql
SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Products
GROUP BY ROLLUP(Company);
```

* В конце таблицы будет добавлена дополнительная строка, которая суммирует значение столбцов.

**При группировке по нескольким критериям `ROLLUP` будет создавать суммирующую строку для каждой из подгрупп:**

```sql
SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Products
GROUP BY ROLLUP(Company, ProductCount)
ORDER BY Company;
```
* При сортировке с помощью `ORDER BY` следует учитывать, что она применяется уже после добавления суммирующей строки.

### `CUBE`
**`CUBE` похож на `ROLLUP` за тем исключением, что `CUBE` добавляет суммирующие строки для каждой комбинации групп.**

```sql
SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Products
GROUP BY CUBE(Company, ProductCount);
```

## 1.8 Подзапросы

* Подзапросы (**subquery**) представляют такие запросы, которые могут быть встроены в другие запросы.
* Часто одну и ту же задачу возможно решить через `JOIN`ы и подзапросы, рекомендуется выполнить оба варианты и проанализировать какой работает быстрее.

**Например, определим таблицы для товаров, покупателей и заказов:**

```sql

CREATE TABLE Products
(
    Id SERIAL PRIMARY KEY,
    ProductName VARCHAR(30) NOT NULL,
    Company VARCHAR(20) NOT NULL,
    ProductCount INTEGER DEFAULT 0,
    Price NUMERIC NOT NULL
);

CREATE TABLE Customers
(
    Id SERIAL PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL
);

CREATE TABLE Orders
(
    Id SERIAL PRIMARY KEY,
    ProductId INTEGER NOT NULL REFERENCES Products(Id) ON DELETE CASCADE,
    CustomerId INTEGER NOT NULL REFERENCES Customers(Id) ON DELETE CASCADE,
    CreatedAt DATE NOT NULL,
    ProductCount INTEGER DEFAULT 1,
    Price NUMERIC NOT NULL
);
```

* Таблица Orders содержит ссылки на две другие таблицы через поля **ProductId** и **CustomerId**.

Добавим в эти таблицы некоторые данные:

```sql
INSERT INTO Products(ProductName, Company, ProductCount, Price) 
VALUES ('iPhone X', 'Apple', 2, 66000),
       ('iPhone 8', 'Apple', 2, 51000),
       ('iPhone 7', 'Apple', 5, 42000),
       ('Galaxy S9', 'Samsung', 2, 56000),
       ('Galaxy S8 Plus', 'Samsung', 1, 46000),
       ('Nokia 9', 'HDM Global', 2, 26000),
       ('Desire 12', 'HTC', 6, 38000);
  
INSERT INTO Customers(FirstName) 
VALUES ('Tom'), ('Bob'),('Sam');
  
INSERT INTO Orders(ProductId, CustomerId, CreatedAt, ProductCount, Price) 
VALUES
( 
    (SELECT Id FROM Products WHERE ProductName='Galaxy S9'), 
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2017-07-11',  
    2, 
    (SELECT Price FROM Products WHERE ProductName='Galaxy S9')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 8'), 
    (SELECT Id FROM Customers WHERE FirstName='Tom'),
    '2017-07-13',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 8')
),
( 
    (SELECT Id FROM Products WHERE ProductName='iPhone 8'), 
    (SELECT Id FROM Customers WHERE FirstName='Bob'),
    '2017-07-11',  
    1, 
    (SELECT Price FROM Products WHERE ProductName='iPhone 8')
);
```

* При добавлении данных в таблицу **Orders** как раз используются подзапросы. 
* Например, первый заказ был сделан покупателем **Tom** на товар **Galaxy S9**. 
* Поэтому в таблицу **Orders** необходимо сохранить информацию о заказе, где поле **ProductId** указывает на **Id** товара **Galaxy S9**, поле **Price** - на его цену, а поле **CustomerId** - на **Id** покупателя **Tom**. 
* Но на момент написания запроса нам может быть неизвестен ни **Id **покупателя, ни **Id** товара, ни цена товара. 
* В этом случае можно выполнить подзапрос.
* Подзапрос представляет команду `SELECT` и заключается в скобки. 
* В данном же случае при добавлении одного товара выполняется три подзапроса. 
* Каждый подзапрос возвращает одно скалярное значение, например, идентификатор товара или покупателя.


**В данном случае подзапросы выполнялись к другой таблице, но могут выполняться и к той же, к которой вызывается основной запрос.**

Например, найдем товары из таблицы **Products**, которые имеют **минимальную цену**:

```sql
SELECT *
FROM Products
WHERE Price = (SELECT MIN(Price) FROM Products);
```

Или найдем товары, цена которых выше средней:

```sql
SELECT *
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
```

### `Коррелирующие подзапросы`
* Подзапросы бывают `коррелирующими` и `некоррелирующими`. 
* В примерах выше команды `SELECT` выполняли фактически один подзапрос для всей команды, например, подзапрос возвращает минимальную или среднюю цену, которая не изменится, сколько бы мы строк не выбирали в основном запросе. 
* Результат такого подзапроса не зависел от строк, которые выбираются в основном запросе. 
* И такой подзапрос выполняется один раз для всего внешнего запроса.

* Но кроме того есть `коррелирующие подзапросы` (**correlated subquery**), результаты которых зависят от строк, которые извлекаются в основном запросе.

**Например, выберем все заказы из таблицы Orders, добавив к ним информацию о товаре:**

```sql
SELECT  CreatedAt, 
        Price, 
        (SELECT ProductName FROM Products 
        WHERE Products.Id = Orders.ProductId) AS Product
FROM Orders;
```

* Здесь для каждой строки из таблицы **Orders** будет выполняться подзапрос, результат которого зависит от столбца **ProductId**. 
* И каждый подзапрос может возвращать различные данные.

*Коррелирующий подзапрос может выполняться и для той же таблицы, к которой выполняется основной запрос. 

**Например, выберем из таблицы Products те товары, стоимость которых выше средней цены товаров для данного производителя:**

```sql
SELECT ProductName,
       Company,
       Price, 
        (SELECT AVG(Price) FROM Products AS SubProds 
         WHERE SubProds.Company=Prods.Company)  AS AvgPrice
FROM Products AS Prods
WHERE Price > 
    (SELECT AVG(Price) FROM Products AS SubProds 
     WHERE SubProds.Company=Prods.Company)
```

* В данном случае определено два коррелирующих подзапроса. 
* Первый подзапрос определяет спецификацию столбца **AvgPrice**. 
* Он будет выполняться для каждой строки, извлекаемой из таблицы Products. 
* В подзапрос передается производитель товара и на его основе выбирается средняя цена для товаров именно этого производителя. 
* И так как производитель у товаров может отличаться, то и результат подзапроса в каждом случае также может отличаться.

* Второй подзапрос аналогичен, только он используется для фильтрации извлекаемых из таблицы *Products*. 
* И также он будет выполняться для каждой строки.
* Чтобы избежать двойственности при фильтрации в подзапросе при сравнении производителей (**SubProds.Company=Prods.Company**) для внешней выборки установлен псевдоним **Prods**, а для выборки из подзапросов определен псевдоним **SubProds**.


```python

```
