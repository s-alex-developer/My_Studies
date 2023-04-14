*Последние изменения внесены: `25.03.2023`*

[<<< Предыдущее меню.](/study_materials/Python/Python_study_materials.md)

# Функция  `filter` (сортировка)

**Функция filter()**
* в **Python** применяет другую **"функцию-критерий"** к заданному итерируемому объекту (список, строка, словарь и так далее), проверяя, нужно ли сохранить конкретный элемент или нет. 
* Простыми словами, она отфильтровывает то, что не проходит и возвращает все остальное.
* **Объект фильтра** — это итерируемый объект. Он сохраняет те элементы, для которых функция вернула `True`. Также можно конвертировать его в `list`, `tuple` или другие типы последовательностей с помощью фабричных методов. 

Получим из списка `list` все четные числа, которые больше 10, разные подходы программирования:


```python
#Структурный стиль:
my_list = [1, 23, 11, 5, 74, 100, 2, 10]

result = []

for i in my_list:
    if i % 2 == 0 and i > 10:
        result.append(i)

print(result)
```

    [74, 100]
    


```python
#Структурный стиль c используванием функций(подпрограмм):
my_list = [1, 23, 11, 5, 74, 100, 2, 10]

result = []

def is_even(i):
    return i % 2 == 0

def greater(i):
    return i > 10

for i in my_list:
    if is_even(i) and greater(i):
        result.append(i)

print(result)
```

    [74, 100]
    


```python
#Стиль функционального программирования и функция filter:
my_list = [1, 23, 11, 5, 74, 100, 2, 10]

result = []

def is_even(i):
    return i % 2 == 0

def greater(i):
    return i > 10

#Функция filter может иметь как одиночную так и вложенную структуру, как в нашем примере:
result = filter(greater, filter(is_even, my_list))

print(result)
print(list(result))
```

    <filter object at 0x000002B733E33B50>
    [74, 100]
    

* В результате работы функции `filter` мы получаем объект типа `filter object`, который моможем обернуть в 'list' или 'tuple'.
* Код записанный в структурном стиле более наглядный и читабельный, но **и работе с большими объемами данных функция `filter` будет работать значительно быстрее.**

Расммотрим как устроена функция `filter` изнутри, если алгоритм ее работы записать в структурной парадигме праграммирования:


```python
def is_even(n):
    return n % 2 == 0

# Алгоритм работы функции filter() записанный в структурной парадигме программирования:
def x_function (fun, data):
    new_data = []
    for i in data:
        if fun(i):
            new_data.append(i)
    return new_data

l = [1, 2, 3, 4, 5]

print(x_function(is_even, l))
```

    [2, 4]
    


```python
Тот же алгоритм обработки данных реализованный при помощи функции filter():
```


```python
def is_even(n):
    return n % 2 == 0

l = [1, 2, 3, 4, 5]

print(list(filter(is_even, l)))
```

    [2, 4]
    

Тот же алгоритм с добавлением `lambda`:


```python
l = [1, 2, 3, 4, 5]

print(list(filter(lambda n: n % 2 == 0, l)))
```

    [2, 4]
    

Или так)))


```python
print(list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5])))
```

    [2, 4]
    

## ЗАДАЧА:
### ЦЕЛЕВАЯ АУДИТОРИЯ.
* Сайт предназначен для мужчин от 20 до 30 лет включительно. 
* Отфильтруйте список people, чтобы в нем осталась только целевая аудитория сайта.
* Результат должен быть помещен в переменную my_people.


```python
peoples = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]


def focus_pll(people):
    return 20 <= people['age'] <= 30 and people['sex'] == 'm'

sorted_people = filter(focus_pll, peoples)
print(list(sorted_people))

```

    [{'sex': 'm', 'age': 20}, {'sex': 'm', 'age': 27}]
    


```python

```
