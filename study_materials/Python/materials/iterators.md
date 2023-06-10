*Последние изменения внесены: `10.06.2023`*

# Итераторы и Итерируемые объекты.

### Итерируемые объекты.

* **Итерируемый объект** это объект, который можно проитерировать, т.е. пройтись по элементам объекта в цикле. 
* Например, итерируемым объектом может быть список или кортеж. 
* В **Python**, чтобы объект был итерируемым, он должен реализовывать метод `__iter__`. 
* Этот метод-болванка принимает в качестве входных данных только экземпляр объекта `self` и должен возвращать объект-итератор. 
* Вы можете использовать встроенную функцию `iter`, чтобы получить итератор итерируемого объекта.
* В **Python** последовательности сами по себе не являются итераторами. Скорее у каждой есть соответствующий класс-итератор, отвечающий за итерацию. 

Пример преобразования списка в итерируемый объект (объект класса-итератора):


```python
l = [1, 2, 3, 4, 5]

it_1 = iter(l)

print(type(it_1))
```

    <class 'list_iterator'>
    

> Итерируемый объект не обязательно является итератором. Поскольку на самом деле сам по себе он не выполняет итерацию. У вас может быть отдельный объект-итератор, который возвращается из итерируемого класса, а не класс, обрабатывающий свою собственную итерацию.

### Итераторы.

* `Итераторы` – это уровень абстракции, который инкапсулирует знания о том, как брать элементы из некоторой последовательности. 
* `Итератор` - это класс, реализующий магичесские методы `__next__` и `__iter__`. 
* «Последовательность», с которой работает `итератор` может быть чем угодно, от списков и файлов до потоков данных из базы данных или удаленного сервиса. 
* В итераторах замечательно то, что код, использующий итератор, даже не должен знать, какой источник данных используется, а вместо этого он может сосредоточиться только на одном, а именно: «Что мне делать с каждым элементом?».


```python
l = [1, 2, 3, 4, 5]

it_1 = iter(l)

print(next(it_1)) # Итерация 1
print(next(it_1)) # Итерация 2
print(next(it_1)) # Итерация 3
print(next(it_1)) # Итерация 4
print(next(it_1)) # Итерация 5
print(next(it_1)) # Итерация 6 - индекс очередного элемента выходит за пределы списка, мы вызываем StopIteration 
```

    1
    2
    3
    4
    5
    


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    Cell In[27], line 10
          8 print(next(it_1)) # Итерация 4
          9 print(next(it_1)) # Итерация 5
    ---> 10 print(next(it_1))
    

    StopIteration: 


> Все циклы `for` в **Python** используют итераторы:


```python
chars = 'abc'

for char in chars:
    print(char)
```

    a
    b
    c
    

По сути в цикле `for` происходит следующее:


```python
chars = iter('ABC')
print(next(chars))
print(next(chars))
print(next(chars))

```

    A
    B
    C
    

Попытка обратится к следующему несуществующему элементу вызовит исключение `StopIteration`:


```python
print(next(chars))
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    Cell In[7], line 1
    ----> 1 print(next(chars))
    

    StopIteration: 


**Реализация итератора чисел Фибонначи в парадигме ООП:**


```python
class Fib:
    
    def __init__(self, max_items):
        self.max_items = max_items
        
    def __next__(self):
        self.items += 1
        if self.items > self.max_items:
            raise StopIteration
    
        self.fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return self.fib
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        self.items = 0
        return self
    
if __name__ == '__main__':
    
    fib = Fib(10)
    
    for item in fib:
        print(item)       
```

    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    

**>>> Реализация цикла `for` через ООП:**


```python
class Print_Hello_World:
    
    def __init__(self, n):
        
        """ Через параметр n задаем кол-во итераций при инициализации объекта класса"""   
        
        self.n = n
    
    def __iter__(self):
        
        """ При использовании объекта класса в качестве итерируемого объекта создается счетчик итераций counter """
        
        self.counter = 0
        return self
    
    def __next__(self):
        
        """ 
            1. При каждой итерации в цикле for значение счетчика увеличивается на 1.
            2. Если текущее значение значение счетчика conter больше значение n цикл вызывает исключение и прерывается.
            3. Каждая выполненная итерация в цикле for возвращает надпиь 'Hello World'
        """
        
        self.counter += 1
        
        if self.counter > self.n:
            raise StopIteration
        
        return 'Hello World'

if __name__ == '__main__':
    
    my_print = Print_Hello_World(3)
    
    for element in my_print:
        print(element)
```

    Hello World
    Hello World
    Hello World
    

**>>> Реализация цикла `range` через ООП:**


```python
class Range:

        def __init__(self, start, end):
            
            self.start = start
            self.end = end
        
        def __iter__(self):
            
            self.counter = self.start - 1
            return self
        
        def __next__(self):
            self.counter += 1
            
            if self.counter == self.end:
                raise StopIteration
                
            return f'Итерация: {self.counter}.'
        
if __name__ == '__main__':
    
    my_range = Range(1, 9)
    
    for element in my_range:
        print(element)
```

    Итерация: 1.
    Итерация: 2.
    Итерация: 3.
    Итерация: 4.
    Итерация: 5.
    Итерация: 6.
    Итерация: 7.
    Итерация: 8.
    

**>>> СУПЕР ГЕРОИ. При помощи `итератора` и `API` с сайта `https://swapi.dev/` получим данные по всем супергероям:** 


```python
import requests as re
from pprint import pprint


class SuperPeoples:

    def __init__(self):
        pass

    def __iter__(self):

        self.url = 'https://swapi.dev/api/people'
        self.peoples = []
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.peoples):
            if self.url is None:
                raise StopIteration

            response = re.get(self.url).json()
            self.url = response['next']
            self.peoples = response['results']
            self.index = 0

        return self.peoples[self.index]


if __name__ == '__main__':

    super_heroes = SuperPeoples()

    hero_count = 0

    for hero in super_heroes:
        pprint(hero)
        hero_count += 1

    print(f'Найдено героев: {hero_count}.')
```

    {'birth_year': '19BBY',
     'created': '2014-12-09T13:50:51.644000Z',
     'edited': '2014-12-20T21:17:56.891000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'blond',
     'height': '172',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '77',
     'name': 'Luke Skywalker',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/12/',
                   'https://swapi.dev/api/starships/22/'],
     'url': 'https://swapi.dev/api/people/1/',
     'vehicles': ['https://swapi.dev/api/vehicles/14/',
                  'https://swapi.dev/api/vehicles/30/']}
    {'birth_year': '112BBY',
     'created': '2014-12-10T15:10:51.357000Z',
     'edited': '2014-12-20T21:17:50.309000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'n/a',
     'hair_color': 'n/a',
     'height': '167',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '75',
     'name': 'C-3PO',
     'skin_color': 'gold',
     'species': ['https://swapi.dev/api/species/2/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/2/',
     'vehicles': []}
    {'birth_year': '33BBY',
     'created': '2014-12-10T15:11:50.376000Z',
     'edited': '2014-12-20T21:17:50.311000Z',
     'eye_color': 'red',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'n/a',
     'hair_color': 'n/a',
     'height': '96',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': '32',
     'name': 'R2-D2',
     'skin_color': 'white, blue',
     'species': ['https://swapi.dev/api/species/2/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/3/',
     'vehicles': []}
    {'birth_year': '41.9BBY',
     'created': '2014-12-10T15:18:20.704000Z',
     'edited': '2014-12-20T21:17:50.313000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '202',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '136',
     'name': 'Darth Vader',
     'skin_color': 'white',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/13/'],
     'url': 'https://swapi.dev/api/people/4/',
     'vehicles': []}
    {'birth_year': '19BBY',
     'created': '2014-12-10T15:20:09.791000Z',
     'edited': '2014-12-20T21:17:50.315000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'brown',
     'height': '150',
     'homeworld': 'https://swapi.dev/api/planets/2/',
     'mass': '49',
     'name': 'Leia Organa',
     'skin_color': 'light',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/5/',
     'vehicles': ['https://swapi.dev/api/vehicles/30/']}
    {'birth_year': '52BBY',
     'created': '2014-12-10T15:52:14.024000Z',
     'edited': '2014-12-20T21:17:50.317000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'brown, grey',
     'height': '178',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '120',
     'name': 'Owen Lars',
     'skin_color': 'light',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/6/',
     'vehicles': []}
    {'birth_year': '47BBY',
     'created': '2014-12-10T15:53:41.121000Z',
     'edited': '2014-12-20T21:17:50.319000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'brown',
     'height': '165',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '75',
     'name': 'Beru Whitesun lars',
     'skin_color': 'light',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/7/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-10T15:57:50.959000Z',
     'edited': '2014-12-20T21:17:50.321000Z',
     'eye_color': 'red',
     'films': ['https://swapi.dev/api/films/1/'],
     'gender': 'n/a',
     'hair_color': 'n/a',
     'height': '97',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '32',
     'name': 'R5-D4',
     'skin_color': 'white, red',
     'species': ['https://swapi.dev/api/species/2/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/8/',
     'vehicles': []}
    {'birth_year': '24BBY',
     'created': '2014-12-10T15:59:50.509000Z',
     'edited': '2014-12-20T21:17:50.323000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/1/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '84',
     'name': 'Biggs Darklighter',
     'skin_color': 'light',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/12/'],
     'url': 'https://swapi.dev/api/people/9/',
     'vehicles': []}
    {'birth_year': '57BBY',
     'created': '2014-12-10T16:16:29.192000Z',
     'edited': '2014-12-20T21:17:50.325000Z',
     'eye_color': 'blue-gray',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'auburn, white',
     'height': '182',
     'homeworld': 'https://swapi.dev/api/planets/20/',
     'mass': '77',
     'name': 'Obi-Wan Kenobi',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/48/',
                   'https://swapi.dev/api/starships/59/',
                   'https://swapi.dev/api/starships/64/',
                   'https://swapi.dev/api/starships/65/',
                   'https://swapi.dev/api/starships/74/'],
     'url': 'https://swapi.dev/api/people/10/',
     'vehicles': ['https://swapi.dev/api/vehicles/38/']}
    {'birth_year': '41.9BBY',
     'created': '2014-12-10T16:20:44.310000Z',
     'edited': '2014-12-20T21:17:50.327000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'blond',
     'height': '188',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': '84',
     'name': 'Anakin Skywalker',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/39/',
                   'https://swapi.dev/api/starships/59/',
                   'https://swapi.dev/api/starships/65/'],
     'url': 'https://swapi.dev/api/people/11/',
     'vehicles': ['https://swapi.dev/api/vehicles/44/',
                  'https://swapi.dev/api/vehicles/46/']}
    {'birth_year': '64BBY',
     'created': '2014-12-10T16:26:56.138000Z',
     'edited': '2014-12-20T21:17:50.330000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'auburn, grey',
     'height': '180',
     'homeworld': 'https://swapi.dev/api/planets/21/',
     'mass': 'unknown',
     'name': 'Wilhuff Tarkin',
     'skin_color': 'fair',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/12/',
     'vehicles': []}
    {'birth_year': '200BBY',
     'created': '2014-12-10T16:42:45.066000Z',
     'edited': '2014-12-20T21:17:50.332000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '228',
     'homeworld': 'https://swapi.dev/api/planets/14/',
     'mass': '112',
     'name': 'Chewbacca',
     'skin_color': 'unknown',
     'species': ['https://swapi.dev/api/species/3/'],
     'starships': ['https://swapi.dev/api/starships/10/',
                   'https://swapi.dev/api/starships/22/'],
     'url': 'https://swapi.dev/api/people/13/',
     'vehicles': ['https://swapi.dev/api/vehicles/19/']}
    {'birth_year': '29BBY',
     'created': '2014-12-10T16:49:14.582000Z',
     'edited': '2014-12-20T21:17:50.334000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '180',
     'homeworld': 'https://swapi.dev/api/planets/22/',
     'mass': '80',
     'name': 'Han Solo',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/10/',
                   'https://swapi.dev/api/starships/22/'],
     'url': 'https://swapi.dev/api/people/14/',
     'vehicles': []}
    {'birth_year': '44BBY',
     'created': '2014-12-10T17:03:30.334000Z',
     'edited': '2014-12-20T21:17:50.336000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/1/'],
     'gender': 'male',
     'hair_color': 'n/a',
     'height': '173',
     'homeworld': 'https://swapi.dev/api/planets/23/',
     'mass': '74',
     'name': 'Greedo',
     'skin_color': 'green',
     'species': ['https://swapi.dev/api/species/4/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/15/',
     'vehicles': []}
    {'birth_year': '600BBY',
     'created': '2014-12-10T17:11:31.638000Z',
     'edited': '2014-12-20T21:17:50.338000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/4/'],
     'gender': 'hermaphrodite',
     'hair_color': 'n/a',
     'height': '175',
     'homeworld': 'https://swapi.dev/api/planets/24/',
     'mass': '1,358',
     'name': 'Jabba Desilijic Tiure',
     'skin_color': 'green-tan, brown',
     'species': ['https://swapi.dev/api/species/5/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/16/',
     'vehicles': []}
    {'birth_year': '21BBY',
     'created': '2014-12-12T11:08:06.469000Z',
     'edited': '2014-12-20T21:17:50.341000Z',
     'eye_color': 'hazel',
     'films': ['https://swapi.dev/api/films/1/',
               'https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '170',
     'homeworld': 'https://swapi.dev/api/planets/22/',
     'mass': '77',
     'name': 'Wedge Antilles',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/12/'],
     'url': 'https://swapi.dev/api/people/18/',
     'vehicles': ['https://swapi.dev/api/vehicles/14/']}
    {'birth_year': 'unknown',
     'created': '2014-12-12T11:16:56.569000Z',
     'edited': '2014-12-20T21:17:50.343000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/1/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '180',
     'homeworld': 'https://swapi.dev/api/planets/26/',
     'mass': '110',
     'name': 'Jek Tono Porkins',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/12/'],
     'url': 'https://swapi.dev/api/people/19/',
     'vehicles': []}
    {'birth_year': '896BBY',
     'created': '2014-12-15T12:26:01.042000Z',
     'edited': '2014-12-20T21:17:50.345000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'white',
     'height': '66',
     'homeworld': 'https://swapi.dev/api/planets/28/',
     'mass': '17',
     'name': 'Yoda',
     'skin_color': 'green',
     'species': ['https://swapi.dev/api/species/6/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/20/',
     'vehicles': []}
    {'birth_year': '82BBY',
     'created': '2014-12-15T12:48:05.971000Z',
     'edited': '2014-12-20T21:17:50.347000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'grey',
     'height': '170',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': '75',
     'name': 'Palpatine',
     'skin_color': 'pale',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/21/',
     'vehicles': []}
    {'birth_year': '31.5BBY',
     'created': '2014-12-15T12:49:32.457000Z',
     'edited': '2014-12-20T21:17:50.349000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/2/',
               'https://swapi.dev/api/films/3/',
               'https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/10/',
     'mass': '78.2',
     'name': 'Boba Fett',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/21/'],
     'url': 'https://swapi.dev/api/people/22/',
     'vehicles': []}
    {'birth_year': '15BBY',
     'created': '2014-12-15T12:51:10.076000Z',
     'edited': '2014-12-20T21:17:50.351000Z',
     'eye_color': 'red',
     'films': ['https://swapi.dev/api/films/2/'],
     'gender': 'none',
     'hair_color': 'none',
     'height': '200',
     'homeworld': 'https://swapi.dev/api/planets/28/',
     'mass': '140',
     'name': 'IG-88',
     'skin_color': 'metal',
     'species': ['https://swapi.dev/api/species/2/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/23/',
     'vehicles': []}
    {'birth_year': '53BBY',
     'created': '2014-12-15T12:53:49.297000Z',
     'edited': '2014-12-20T21:17:50.355000Z',
     'eye_color': 'red',
     'films': ['https://swapi.dev/api/films/2/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '190',
     'homeworld': 'https://swapi.dev/api/planets/29/',
     'mass': '113',
     'name': 'Bossk',
     'skin_color': 'green',
     'species': ['https://swapi.dev/api/species/7/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/24/',
     'vehicles': []}
    {'birth_year': '31BBY',
     'created': '2014-12-15T12:56:32.683000Z',
     'edited': '2014-12-20T21:17:50.357000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '177',
     'homeworld': 'https://swapi.dev/api/planets/30/',
     'mass': '79',
     'name': 'Lando Calrissian',
     'skin_color': 'dark',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/10/'],
     'url': 'https://swapi.dev/api/people/25/',
     'vehicles': []}
    {'birth_year': '37BBY',
     'created': '2014-12-15T13:01:57.178000Z',
     'edited': '2014-12-20T21:17:50.359000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/2/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '175',
     'homeworld': 'https://swapi.dev/api/planets/6/',
     'mass': '79',
     'name': 'Lobot',
     'skin_color': 'light',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/26/',
     'vehicles': []}
    {'birth_year': '41BBY',
     'created': '2014-12-18T11:07:50.584000Z',
     'edited': '2014-12-20T21:17:50.362000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '180',
     'homeworld': 'https://swapi.dev/api/planets/31/',
     'mass': '83',
     'name': 'Ackbar',
     'skin_color': 'brown mottle',
     'species': ['https://swapi.dev/api/species/8/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/27/',
     'vehicles': []}
    {'birth_year': '48BBY',
     'created': '2014-12-18T11:12:38.895000Z',
     'edited': '2014-12-20T21:17:50.364000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/3/'],
     'gender': 'female',
     'hair_color': 'auburn',
     'height': '150',
     'homeworld': 'https://swapi.dev/api/planets/32/',
     'mass': 'unknown',
     'name': 'Mon Mothma',
     'skin_color': 'fair',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/28/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-18T11:16:33.020000Z',
     'edited': '2014-12-20T21:17:50.367000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': 'unknown',
     'homeworld': 'https://swapi.dev/api/planets/28/',
     'mass': 'unknown',
     'name': 'Arvel Crynyd',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/28/'],
     'url': 'https://swapi.dev/api/people/29/',
     'vehicles': []}
    {'birth_year': '8BBY',
     'created': '2014-12-18T11:21:58.954000Z',
     'edited': '2014-12-20T21:17:50.369000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '88',
     'homeworld': 'https://swapi.dev/api/planets/7/',
     'mass': '20',
     'name': 'Wicket Systri Warrick',
     'skin_color': 'brown',
     'species': ['https://swapi.dev/api/species/9/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/30/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-18T11:26:18.541000Z',
     'edited': '2014-12-20T21:17:50.371000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '160',
     'homeworld': 'https://swapi.dev/api/planets/33/',
     'mass': '68',
     'name': 'Nien Nunb',
     'skin_color': 'grey',
     'species': ['https://swapi.dev/api/species/10/'],
     'starships': ['https://swapi.dev/api/starships/10/'],
     'url': 'https://swapi.dev/api/people/31/',
     'vehicles': []}
    {'birth_year': '92BBY',
     'created': '2014-12-19T16:54:53.618000Z',
     'edited': '2014-12-20T21:17:50.375000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '193',
     'homeworld': 'https://swapi.dev/api/planets/28/',
     'mass': '89',
     'name': 'Qui-Gon Jinn',
     'skin_color': 'fair',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/32/',
     'vehicles': ['https://swapi.dev/api/vehicles/38/']}
    {'birth_year': 'unknown',
     'created': '2014-12-19T17:05:57.357000Z',
     'edited': '2014-12-20T21:17:50.377000Z',
     'eye_color': 'red',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '191',
     'homeworld': 'https://swapi.dev/api/planets/18/',
     'mass': '90',
     'name': 'Nute Gunray',
     'skin_color': 'mottled green',
     'species': ['https://swapi.dev/api/species/11/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/33/',
     'vehicles': []}
    {'birth_year': '91BBY',
     'created': '2014-12-19T17:21:45.915000Z',
     'edited': '2014-12-20T21:17:50.379000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'blond',
     'height': '170',
     'homeworld': 'https://swapi.dev/api/planets/9/',
     'mass': 'unknown',
     'name': 'Finis Valorum',
     'skin_color': 'fair',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/34/',
     'vehicles': []}
    {'birth_year': '46BBY',
     'created': '2014-12-19T17:28:26.926000Z',
     'edited': '2014-12-20T21:17:50.381000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'brown',
     'height': '185',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': '45',
     'name': 'Padmé Amidala',
     'skin_color': 'light',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/39/',
                   'https://swapi.dev/api/starships/49/',
                   'https://swapi.dev/api/starships/64/'],
     'url': 'https://swapi.dev/api/people/35/',
     'vehicles': []}
    {'birth_year': '52BBY',
     'created': '2014-12-19T17:29:32.489000Z',
     'edited': '2014-12-20T21:17:50.383000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '196',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': '66',
     'name': 'Jar Jar Binks',
     'skin_color': 'orange',
     'species': ['https://swapi.dev/api/species/12/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/36/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-19T17:32:56.741000Z',
     'edited': '2014-12-20T21:17:50.385000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '224',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': '82',
     'name': 'Roos Tarpals',
     'skin_color': 'grey',
     'species': ['https://swapi.dev/api/species/12/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/37/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-19T17:33:38.909000Z',
     'edited': '2014-12-20T21:17:50.388000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '206',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': 'unknown',
     'name': 'Rugor Nass',
     'skin_color': 'green',
     'species': ['https://swapi.dev/api/species/12/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/38/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-19T17:45:01.522000Z',
     'edited': '2014-12-20T21:17:50.392000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': 'unknown',
     'name': 'Ric Olié',
     'skin_color': 'fair',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/40/'],
     'url': 'https://swapi.dev/api/people/39/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-19T17:48:54.647000Z',
     'edited': '2014-12-20T21:17:50.395000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '137',
     'homeworld': 'https://swapi.dev/api/planets/34/',
     'mass': 'unknown',
     'name': 'Watto',
     'skin_color': 'blue, grey',
     'species': ['https://swapi.dev/api/species/13/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/40/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-19T17:53:02.586000Z',
     'edited': '2014-12-20T21:17:50.397000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '112',
     'homeworld': 'https://swapi.dev/api/planets/35/',
     'mass': '40',
     'name': 'Sebulba',
     'skin_color': 'grey, red',
     'species': ['https://swapi.dev/api/species/14/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/41/',
     'vehicles': []}
    {'birth_year': '62BBY',
     'created': '2014-12-19T17:55:43.348000Z',
     'edited': '2014-12-20T21:17:50.399000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': 'unknown',
     'name': 'Quarsh Panaka',
     'skin_color': 'dark',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/42/',
     'vehicles': []}
    {'birth_year': '72BBY',
     'created': '2014-12-19T17:57:41.191000Z',
     'edited': '2014-12-20T21:17:50.401000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'black',
     'height': '163',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': 'unknown',
     'name': 'Shmi Skywalker',
     'skin_color': 'fair',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/43/',
     'vehicles': []}
    {'birth_year': '54BBY',
     'created': '2014-12-19T18:00:41.929000Z',
     'edited': '2014-12-20T21:17:50.403000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '175',
     'homeworld': 'https://swapi.dev/api/planets/36/',
     'mass': '80',
     'name': 'Darth Maul',
     'skin_color': 'red',
     'species': ['https://swapi.dev/api/species/22/'],
     'starships': ['https://swapi.dev/api/starships/41/'],
     'url': 'https://swapi.dev/api/people/44/',
     'vehicles': ['https://swapi.dev/api/vehicles/42/']}
    {'birth_year': 'unknown',
     'created': '2014-12-20T09:47:02.512000Z',
     'edited': '2014-12-20T21:17:50.407000Z',
     'eye_color': 'pink',
     'films': ['https://swapi.dev/api/films/3/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '180',
     'homeworld': 'https://swapi.dev/api/planets/37/',
     'mass': 'unknown',
     'name': 'Bib Fortuna',
     'skin_color': 'pale',
     'species': ['https://swapi.dev/api/species/15/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/45/',
     'vehicles': []}
    {'birth_year': '48BBY',
     'created': '2014-12-20T09:48:01.172000Z',
     'edited': '2014-12-20T21:17:50.409000Z',
     'eye_color': 'hazel',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'none',
     'height': '178',
     'homeworld': 'https://swapi.dev/api/planets/37/',
     'mass': '55',
     'name': 'Ayla Secura',
     'skin_color': 'blue',
     'species': ['https://swapi.dev/api/species/15/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/46/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T09:53:15.086000Z',
     'edited': '2014-12-20T21:17:50.410000Z',
     'eye_color': 'unknown',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '79',
     'homeworld': 'https://swapi.dev/api/planets/38/',
     'mass': '15',
     'name': 'Ratts Tyerel',
     'skin_color': 'grey, blue',
     'species': ['https://swapi.dev/api/species/16/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/47/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T09:57:31.858000Z',
     'edited': '2014-12-20T21:17:50.414000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '94',
     'homeworld': 'https://swapi.dev/api/planets/39/',
     'mass': '45',
     'name': 'Dud Bolt',
     'skin_color': 'blue, grey',
     'species': ['https://swapi.dev/api/species/17/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/48/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:02:12.223000Z',
     'edited': '2014-12-20T21:17:50.416000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '122',
     'homeworld': 'https://swapi.dev/api/planets/40/',
     'mass': 'unknown',
     'name': 'Gasgano',
     'skin_color': 'white, blue',
     'species': ['https://swapi.dev/api/species/18/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/49/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:08:33.777000Z',
     'edited': '2014-12-20T21:17:50.417000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '163',
     'homeworld': 'https://swapi.dev/api/planets/41/',
     'mass': '65',
     'name': 'Ben Quadinaros',
     'skin_color': 'grey, green, yellow',
     'species': ['https://swapi.dev/api/species/19/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/50/',
     'vehicles': []}
    {'birth_year': '72BBY',
     'created': '2014-12-20T10:12:30.846000Z',
     'edited': '2014-12-20T21:17:50.420000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '188',
     'homeworld': 'https://swapi.dev/api/planets/42/',
     'mass': '84',
     'name': 'Mace Windu',
     'skin_color': 'dark',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/51/',
     'vehicles': []}
    {'birth_year': '92BBY',
     'created': '2014-12-20T10:15:32.293000Z',
     'edited': '2014-12-20T21:17:50.422000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'white',
     'height': '198',
     'homeworld': 'https://swapi.dev/api/planets/43/',
     'mass': '82',
     'name': 'Ki-Adi-Mundi',
     'skin_color': 'pale',
     'species': ['https://swapi.dev/api/species/20/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/52/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:18:57.202000Z',
     'edited': '2014-12-20T21:17:50.424000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '196',
     'homeworld': 'https://swapi.dev/api/planets/44/',
     'mass': '87',
     'name': 'Kit Fisto',
     'skin_color': 'green',
     'species': ['https://swapi.dev/api/species/21/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/53/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:26:47.902000Z',
     'edited': '2014-12-20T21:17:50.427000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '171',
     'homeworld': 'https://swapi.dev/api/planets/45/',
     'mass': 'unknown',
     'name': 'Eeth Koth',
     'skin_color': 'brown',
     'species': ['https://swapi.dev/api/species/22/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/54/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:29:11.661000Z',
     'edited': '2014-12-20T21:17:50.432000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'none',
     'height': '184',
     'homeworld': 'https://swapi.dev/api/planets/9/',
     'mass': '50',
     'name': 'Adi Gallia',
     'skin_color': 'dark',
     'species': ['https://swapi.dev/api/species/23/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/55/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:32:11.669000Z',
     'edited': '2014-12-20T21:17:50.434000Z',
     'eye_color': 'orange',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '188',
     'homeworld': 'https://swapi.dev/api/planets/47/',
     'mass': 'unknown',
     'name': 'Saesee Tiin',
     'skin_color': 'pale',
     'species': ['https://swapi.dev/api/species/24/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/56/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:34:48.725000Z',
     'edited': '2014-12-20T21:17:50.437000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/4/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '264',
     'homeworld': 'https://swapi.dev/api/planets/48/',
     'mass': 'unknown',
     'name': 'Yarael Poof',
     'skin_color': 'white',
     'species': ['https://swapi.dev/api/species/25/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/57/',
     'vehicles': []}
    {'birth_year': '22BBY',
     'created': '2014-12-20T10:49:19.859000Z',
     'edited': '2014-12-20T21:17:50.439000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/4/',
               'https://swapi.dev/api/films/5/',
               'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '188',
     'homeworld': 'https://swapi.dev/api/planets/49/',
     'mass': '80',
     'name': 'Plo Koon',
     'skin_color': 'orange',
     'species': ['https://swapi.dev/api/species/26/'],
     'starships': ['https://swapi.dev/api/starships/48/'],
     'url': 'https://swapi.dev/api/people/58/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T10:53:26.457000Z',
     'edited': '2014-12-20T21:17:50.442000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/4/', 'https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '196',
     'homeworld': 'https://swapi.dev/api/planets/50/',
     'mass': 'unknown',
     'name': 'Mas Amedda',
     'skin_color': 'blue',
     'species': ['https://swapi.dev/api/species/27/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/59/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T11:10:10.381000Z',
     'edited': '2014-12-20T21:17:50.445000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '185',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': '85',
     'name': 'Gregar Typho',
     'skin_color': 'dark',
     'species': [],
     'starships': ['https://swapi.dev/api/starships/39/'],
     'url': 'https://swapi.dev/api/people/60/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T11:11:39.630000Z',
     'edited': '2014-12-20T21:17:50.449000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'brown',
     'height': '157',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': 'unknown',
     'name': 'Cordé',
     'skin_color': 'light',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/61/',
     'vehicles': []}
    {'birth_year': '82BBY',
     'created': '2014-12-20T15:59:03.958000Z',
     'edited': '2014-12-20T21:17:50.451000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/1/',
     'mass': 'unknown',
     'name': 'Cliegg Lars',
     'skin_color': 'fair',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/62/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T16:40:43.977000Z',
     'edited': '2014-12-20T21:17:50.453000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/11/',
     'mass': '80',
     'name': 'Poggle the Lesser',
     'skin_color': 'green',
     'species': ['https://swapi.dev/api/species/28/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/63/',
     'vehicles': []}
    {'birth_year': '58BBY',
     'created': '2014-12-20T16:45:53.668000Z',
     'edited': '2014-12-20T21:17:50.455000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'black',
     'height': '170',
     'homeworld': 'https://swapi.dev/api/planets/51/',
     'mass': '56.2',
     'name': 'Luminara Unduli',
     'skin_color': 'yellow',
     'species': ['https://swapi.dev/api/species/29/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/64/',
     'vehicles': []}
    {'birth_year': '40BBY',
     'created': '2014-12-20T16:46:40.440000Z',
     'edited': '2014-12-20T21:17:50.457000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'black',
     'height': '166',
     'homeworld': 'https://swapi.dev/api/planets/51/',
     'mass': '50',
     'name': 'Barriss Offee',
     'skin_color': 'yellow',
     'species': ['https://swapi.dev/api/species/29/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/65/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T16:49:14.640000Z',
     'edited': '2014-12-20T21:17:50.460000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'brown',
     'height': '165',
     'homeworld': 'https://swapi.dev/api/planets/8/',
     'mass': 'unknown',
     'name': 'Dormé',
     'skin_color': 'light',
     'species': ['https://swapi.dev/api/species/1/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/66/',
     'vehicles': []}
    {'birth_year': '102BBY',
     'created': '2014-12-20T16:52:14.726000Z',
     'edited': '2014-12-20T21:17:50.462000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'white',
     'height': '193',
     'homeworld': 'https://swapi.dev/api/planets/52/',
     'mass': '80',
     'name': 'Dooku',
     'skin_color': 'fair',
     'species': ['https://swapi.dev/api/species/1/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/67/',
     'vehicles': ['https://swapi.dev/api/vehicles/55/']}
    {'birth_year': '67BBY',
     'created': '2014-12-20T16:53:08.575000Z',
     'edited': '2014-12-20T21:17:50.463000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '191',
     'homeworld': 'https://swapi.dev/api/planets/2/',
     'mass': 'unknown',
     'name': 'Bail Prestor Organa',
     'skin_color': 'tan',
     'species': ['https://swapi.dev/api/species/1/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/68/',
     'vehicles': []}
    {'birth_year': '66BBY',
     'created': '2014-12-20T16:54:41.620000Z',
     'edited': '2014-12-20T21:17:50.465000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'black',
     'height': '183',
     'homeworld': 'https://swapi.dev/api/planets/53/',
     'mass': '79',
     'name': 'Jango Fett',
     'skin_color': 'tan',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/69/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T16:57:44.471000Z',
     'edited': '2014-12-20T21:17:50.468000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'blonde',
     'height': '168',
     'homeworld': 'https://swapi.dev/api/planets/54/',
     'mass': '55',
     'name': 'Zam Wesell',
     'skin_color': 'fair, green, yellow',
     'species': ['https://swapi.dev/api/species/30/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/70/',
     'vehicles': ['https://swapi.dev/api/vehicles/45/']}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:28:27.248000Z',
     'edited': '2014-12-20T21:17:50.470000Z',
     'eye_color': 'yellow',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '198',
     'homeworld': 'https://swapi.dev/api/planets/55/',
     'mass': '102',
     'name': 'Dexter Jettster',
     'skin_color': 'brown',
     'species': ['https://swapi.dev/api/species/31/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/71/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:30:50.416000Z',
     'edited': '2014-12-20T21:17:50.473000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '229',
     'homeworld': 'https://swapi.dev/api/planets/10/',
     'mass': '88',
     'name': 'Lama Su',
     'skin_color': 'grey',
     'species': ['https://swapi.dev/api/species/32/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/72/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:31:21.195000Z',
     'edited': '2014-12-20T21:17:50.474000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'none',
     'height': '213',
     'homeworld': 'https://swapi.dev/api/planets/10/',
     'mass': 'unknown',
     'name': 'Taun We',
     'skin_color': 'grey',
     'species': ['https://swapi.dev/api/species/32/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/73/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:32:51.996000Z',
     'edited': '2014-12-20T21:17:50.476000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'female',
     'hair_color': 'white',
     'height': '167',
     'homeworld': 'https://swapi.dev/api/planets/9/',
     'mass': 'unknown',
     'name': 'Jocasta Nu',
     'skin_color': 'fair',
     'species': ['https://swapi.dev/api/species/1/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/74/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:43:36.409000Z',
     'edited': '2014-12-20T21:17:50.478000Z',
     'eye_color': 'red, blue',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'none',
     'height': '96',
     'homeworld': 'https://swapi.dev/api/planets/28/',
     'mass': 'unknown',
     'name': 'R4-P17',
     'skin_color': 'silver, red',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/75/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:53:52.607000Z',
     'edited': '2014-12-20T21:17:50.481000Z',
     'eye_color': 'unknown',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '193',
     'homeworld': 'https://swapi.dev/api/planets/56/',
     'mass': '48',
     'name': 'Wat Tambor',
     'skin_color': 'green, grey',
     'species': ['https://swapi.dev/api/species/33/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/76/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T17:58:17.049000Z',
     'edited': '2014-12-20T21:17:50.484000Z',
     'eye_color': 'gold',
     'films': ['https://swapi.dev/api/films/5/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '191',
     'homeworld': 'https://swapi.dev/api/planets/57/',
     'mass': 'unknown',
     'name': 'San Hill',
     'skin_color': 'grey',
     'species': ['https://swapi.dev/api/species/34/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/77/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T18:44:01.103000Z',
     'edited': '2014-12-20T21:17:50.486000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'none',
     'height': '178',
     'homeworld': 'https://swapi.dev/api/planets/58/',
     'mass': '57',
     'name': 'Shaak Ti',
     'skin_color': 'red, blue, white',
     'species': ['https://swapi.dev/api/species/35/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/78/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T19:43:53.348000Z',
     'edited': '2014-12-20T21:17:50.488000Z',
     'eye_color': 'green, yellow',
     'films': ['https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '216',
     'homeworld': 'https://swapi.dev/api/planets/59/',
     'mass': '159',
     'name': 'Grievous',
     'skin_color': 'brown, white',
     'species': ['https://swapi.dev/api/species/36/'],
     'starships': ['https://swapi.dev/api/starships/74/'],
     'url': 'https://swapi.dev/api/people/79/',
     'vehicles': ['https://swapi.dev/api/vehicles/60/']}
    {'birth_year': 'unknown',
     'created': '2014-12-20T19:46:34.209000Z',
     'edited': '2014-12-20T21:17:50.491000Z',
     'eye_color': 'blue',
     'films': ['https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '234',
     'homeworld': 'https://swapi.dev/api/planets/14/',
     'mass': '136',
     'name': 'Tarfful',
     'skin_color': 'brown',
     'species': ['https://swapi.dev/api/species/3/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/80/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T19:49:35.583000Z',
     'edited': '2014-12-20T21:17:50.493000Z',
     'eye_color': 'brown',
     'films': ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'brown',
     'height': '188',
     'homeworld': 'https://swapi.dev/api/planets/2/',
     'mass': '79',
     'name': 'Raymus Antilles',
     'skin_color': 'light',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/81/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T20:18:37.619000Z',
     'edited': '2014-12-20T21:17:50.496000Z',
     'eye_color': 'white',
     'films': ['https://swapi.dev/api/films/5/', 'https://swapi.dev/api/films/6/'],
     'gender': 'female',
     'hair_color': 'none',
     'height': '178',
     'homeworld': 'https://swapi.dev/api/planets/60/',
     'mass': '48',
     'name': 'Sly Moore',
     'skin_color': 'pale',
     'species': [],
     'starships': [],
     'url': 'https://swapi.dev/api/people/82/',
     'vehicles': []}
    {'birth_year': 'unknown',
     'created': '2014-12-20T20:35:04.260000Z',
     'edited': '2014-12-20T21:17:50.498000Z',
     'eye_color': 'black',
     'films': ['https://swapi.dev/api/films/6/'],
     'gender': 'male',
     'hair_color': 'none',
     'height': '206',
     'homeworld': 'https://swapi.dev/api/planets/12/',
     'mass': '80',
     'name': 'Tion Medon',
     'skin_color': 'grey',
     'species': ['https://swapi.dev/api/species/37/'],
     'starships': [],
     'url': 'https://swapi.dev/api/people/83/',
     'vehicles': []}
    Найдено героев: 82.
    


```python

```
