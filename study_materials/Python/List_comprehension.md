*Последние изменения внесены: 14.03.2023*

# List comprehension

`List comprehension` (_"Генератор списков"_) - позволяет в одну строку кода заполнить список простыми или сложными значениями.

**Все генераторы списка строятся по следующему шаблону:**

[ "Выражение"  **for**  "Переменная"  **in**  "Коллекция"  **if**  "Условие"  **and / or / not** "Второе условие"  ]

    

**1. Простые примеры:**


```python
my_list  = [ 2 for i in range(7)]
print(my_list)
```

    [2, 2, 2, 2, 2, 2, 2]
    


```python
my_list  = [ i for i in range(7)]
print(my_list)
```

    [0, 1, 2, 3, 4, 5, 6]
    


```python
my_list  = [ i ** 2 for i in range(7)]
print(my_list)
```

    [0, 1, 4, 9, 16, 25, 36]
    


```python
my_list  = [ i for i in 'abc']
print(my_list)
```

    ['a', 'b', 's']
    


```python
my_list  = [ i * 3 for i in 'abc']
print(my_list)
```

    ['aaa', 'bbb', 'ccc']
    


```python
my_list  = [ abs(i) for i in [1, 2, -3, -4, -5]]
print(my_list)
```

    [1, 2, 3, 4, 5]
    


```python
string = '11 22 33 44 55'
work_list = string.split()
my_list  = [ int(i) for i in work_list]
print(my_list)
```

    [11, 22, 33, 44, 55]
    

**2. Примеры с логичесским условием:**


```python
my_list  = [ i for i in [1, 2, -3, -4, -5] if i > 0]
print(my_list)
```

    [1, 2]
    


```python
my_list  = [ i for i in [1, 2, -3, -4, -5] if i > 0 and i < 2]
print(my_list)
```

    [1]
    


```python

```

**3. Пример с построением матрицы элементов:**


```python
a = 3
b = 3
square = [['x'] * a for i in range(b)]
print(square)
```

    [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
    


```python
a = 3
b = 3
square = [['x'] * a for i in range(b)]
for line in square:
    print(line)
```

    ['x', 'x', 'x']
    ['x', 'x', 'x']
    ['x', 'x', 'x']
    

Изменение одного элемента:


```python
a = 3
b = 3
square = [['x'] * a for i in range(b)]
square[1][1] = 'O'
for line in square:
    print(line)
```

    ['x', 'x', 'x']
    ['x', 'O', 'x']
    ['x', 'x', 'x']
    

**4. Двойные циклы в генераторах списков:**


```python
a = [(i, g) for i in 'abc' for g in [1, 2, 3]]
print(a)
```

    [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
    

С логическим условием:


```python
a = [i * g for i in [1, 2, 3] for g in [1, 2, 3] if i * g > 5]
print(a)
```

    [6, 6, 9]
    


```python

```
