*Последние изменения внесены: `29.03.2023`*

[<<< Предыдущее меню.]()

# Функция reduce()

**Функция reduce()**
* Как можно понять из названия, применяет переданную функцию к итерируемому объекту и возвращает одно значение.
* Данная функция используется для организации цепочных вычислений.
* Начиная с **Python 3** функция `reduce()` перенесена в модуль `functools`, чтобы ей воспользоваться необходимо произвести импорт: 
```python
from functools import reduce
```

**Синтаксис:**
```python
from functools import reduce

reduce(function, iterable[, initializer])
```
**Параметры:**
* `function` - пользовательская функция, принимающая 2 аргумента,
* `iterable` - итерируемая последовательность,
* `initializer` - начальное значение.

**Возвращаемое значение:**
* требуемое единственное значение.

### Пример:
Рассмотрим пример использования функции `reduce` для вычисления факториала числа:

_**Факториал числа n** — это произведение всех натуральных чисел от 1 до **n** включительно. Обозначается переменной **n!**_


```python
from functools import reduce

# Вычислим факториал 5:
l = range(1, 6)

def mult(x, y):
    return x * y

factorial = reduce(mult, l)

print(factorial)
```

    120
    

### Пример:
Рассмотрим пример совместного использования функции `reduce()` с функцией `map()`:


```python
super_heroes = [
    {'name': 'Hulk', 'power': 90, 'agility': 10},
    {'name': 'Spider Man', 'power': 45, 'agility': 90},
    {'name': 'Aqua Man', 'power': 65, 'agility': 60}
]

# Найдем абсолютную силу каждго героя сложив показатели power и agility используя возможности функции map(): 
new_heroes = []

def sum_power(hero):
    return {'name': hero['name'], 'hero power': hero['power'] + hero['agility']} 

heroes_pow = list(map(sum_power, super_heroes))

print(heroes_pow)

```

    [{'name': 'Hulk', 'hero power': 100}, {'name': 'Spider Man', 'hero power': 135}, {'name': 'Aqua Man', 'hero power': 125}]
    

К полученному результату применим функцию `reduce()` и определим самого сильного героя:


```python
def abs_hero(hero1, hero2):
    if hero1['hero power'] >  hero1['hero power']:
        return hero1
    return  hero2

top_hero = reduce(abs_hero, heroes_pow)
print(top_hero)
```

    {'name': 'Aqua Man', 'hero power': 125}
    


```python
# Можно записать более компактно:
top_hero = reduce(abs_hero, map(sum_power, super_heroes))
print(top_hero)
```

    {'name': 'Aqua Man', 'hero power': 125}
    

## ЗАДАЧИ.

### Задача 1. СКЛЕЙКА.
* Склейте элементы списка **whoami** в строку с помощью функции `reduce`.

```python
from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

whoami = reduce()
```

### Задача 2. ПЛОЩАДЬ КВАРТИРЫ.
* Используйте `map` и `reduce`, чтобы посчитать площадь квартиры, состоящей из комнат rooms.
```pytho
from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

rooms = map()
square = reduce()
```

### Задача 3. ФУНКЦИОНАЛЬНЫЙ ПОИСК МАКСИМУМОВ.

* Иногда в систему поступает много данных и нужно фиксировать только те, которые выросли в значении. 
* Например, если в программу пришли числа 34, 56, 12, 55, 74, 58. То нужно оставить только 34, 56, и 74. То есть мы каждый раз оставляем только максимальное число относительно всех предыдущий значений.
* Напишите программу, которая получает из аргументов командной строки произвольное количество чисел, а затем выводит только максимумы. Выводимые числа нужно разделить запятой с пробелом.
* Используйте для расчета функцию `reduce`. Учитывайте, что `reduce` в качестве параметров может принимать не только числа или строки, но и списки, кортежи и словари. А также более сложные типы данных.
* Для упрощения кода можете использовать третий аргумент reduсe - `initializer`

*Пример использования в командной строке:*
> python trend.py 34 56 12 55 74 58 59 74 75

*Результат:* **34, 56, 74, 75**

## РЕШЕНИЯ.

### Задача 1. СКЛЕЙКА - решение.


```python
from functools import reduce

def concat(x, y):
    el = x + y
    return el

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

whoami = reduce(concat, whoami)

print(whoami)
```

    Я программист
    

### Задача 2. ПЛОЩАДЬ КВАРТИРЫ - решение.


```python
from functools import reduce

def square(room):
    s = room["length"] * room["width"]
    return s

def summ(a, b):
    s = a + b
    return s

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

rooms = map(square, rooms)
square = reduce(summ, rooms)

print(square)
```

    112.85
    

### Задача 3. ФУНКЦИОНАЛЬНЫЙ ПОИСК МАКСИМУМОВ - решение.


```python
from functools import reduce

# import sys
# work_list = [int(n) for n in sys.argv[1:]]

work_list = '34 56 12 55 74 58 59 74 75'.split()

def gt(a, b):
    if max(a) < b:
        a.add(b)
        return a
    else:
        return a

result = sorted(list(reduce(gt, work_list, {work_list[0]})))

print(*result, sep=', ')
```

    34, 56, 74, 75
    


```python

```
