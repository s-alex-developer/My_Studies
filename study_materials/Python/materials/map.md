*Последние изменения внесены: `25.03.2023`*



# Функция `map` (преобразование данных).

**Функция map()**
* Это встроенная функция в **Python**, которая позволяет обрабатывать и преобразовывать все элементы в итерируемом объекте без использования явного цикла for, методом, широко известным как сопоставление **(mapping)**.
* `map()` полезен, когда вам нужно применить функцию преобразования к каждому элементу в коллекции или в массиве и преобразовать их в новый массив.
* `map()` — один из инструментов, поддерживающих стиль функционального программирования в Python.

Рассмотри преобразование данных списка **work_list** с использованием разных парадигм программирования:


```python
# Возведем все числа списка используя структурный подход программирования:
work_list = [1, 2, 3, 4, 5]

new_list = []

for n in work_list:
    new_list.append(n ** 2)
    
print(new_list)
```

    [1, 4, 9, 16, 25]
    


```python
# Возведем все числа списка используя структурный подход программирования и применение функции (подпрограммы):
work_list = [1, 2, 3, 4, 5]

def square(n):
    return n ** 2

new_list = []

for n in work_list:
    new_list.append(square(n))
    
print(new_list)
```

    [1, 4, 9, 16, 25]
    


```python
# Возведем все числа списка используя функциональный подход программирования и применение функции map():
work_list = [1, 2, 3, 4, 5]

def square(n):
    return n ** 2

new_list = map(square, work_list)

print(new_list)
print(list(new_list))
```

    <map object at 0x000001AFFC3A2B30>
    [1, 4, 9, 16, 25]
    

Еще один пример преобразования данных при помощи функции `map()`:


```python
work_list = [1, 2, 3, 4, 5]

# Преобразуем данные списка из типа int в тип str
new_list = map(str, work_list)

print(list(new_list))
```

    ['1', '2', '3', '4', '5']
    

## ЗАДАЧИ.

### Задача 1. ПЛОЩАДЬ КОМНАТ.
* Создайте функцию для использования внутри map. 
* Функция должна добавлять к каждой комнате в списке rooms элемент с именем square содержащий её площадь.

```python
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

rooms = map()
```

### Задача 2. ТОЛЬКО ЧИСЛА
* В списке **digits** содержатся строки с числами. Эти строки содержат ошибки: лишние пробелы, а также неправильные разделители целой и десятичной части.
* Создайте функцию, которая сначала исправит ошибки в строках, а затем преобразует каждую строку в вещественное число. 
* Примените эту функцию ко всем элементам **digits** с помощью `map`.

```python
digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]

right_digits = map()
```

## РЕШЕНИЯ.

### Задача 1.  ПЛОЩАДЬ КОМНАТ - решение.


```python
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

def square(room):

    _square = room['length'] * room['width']
    room['square'] = _square
    return room


rooms = map(square, rooms)

print(list(rooms))
```

    [{'name': 'кухня', 'length': 6, 'width': 4, 'square': 24}, {'name': 'комната 1', 'length': 5.5, 'width': 4.5, 'square': 24.75}, {'name': 'комната 2', 'length': 5, 'width': 4, 'square': 20}, {'name': 'комната 3', 'length': 7, 'width': 6.3, 'square': 44.1}]
    

### Задача 2.  ТОЛЬКО ЧИСЛА - решение.


```python
def transformation(digit):
    elem = float(digit.strip().replace(' ', '').replace(',', '.'))
    return elem

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]

right_digits = map(transformation, digits)

print(list(right_digits))
```

    [12.0, 145.0, 45.0, 12.4, 45.14, 15645.0]
    


