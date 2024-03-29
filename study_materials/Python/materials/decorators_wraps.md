*Последние изменения внесены: `04.04.2023`*

# Декораторы и декоратор `wraps`.

**Декораторы** - это "обертки" вокруг функций, которые позволяют изменить ее поведение или функционал не вмешиваясь в исходный код функции.

### "Замыкание" (closures).
* Ключевой момент в работе функции декоратора лежит понятие `"замыкание"`.
* `"Замыкание"` возникает когда вложенная функция ссылается на значение из локальной области видимости объемлющей функции.
* Критерии, которые должны быть выполнены для создания замыкания в Python, изложены в следующих пунктах:
    * У нас должна быть вложенная функция (функция внутри функции).
    * Вложенная функция должна ссылаться на значение, определенное в объемлющей функции.
    * Объемлющая функция должна возвращать вложенную функцию.
* Ссылка на переменную объемлющей функции действительна, даже когда объемлющая функция закончила работу, и переменная вышла из области видимости или сама функция удаляется из текущего пространства имен.
* `"Замыкания"` позволяют избежать использования глобальных (global) значений и обеспечивают некоторую форму сокрытия данных. Для этого также может использоваться объектно-ориентированный подход.
* Если в классе необходимо реализовать небольшое количество методов (в большинстве случаев один метод), замыкания могут обеспечить альтернативное и более элегантное решение. Но когда количество атрибутов и методов становится больше, лучше реализовать класс.


Расмотрим базовую конструкцию функции `декоратора` и принцип ее работы:


```python
#Decorator - функция декоратор: 
def decorator(func):
    
    #Вложенная функция ("функция-обертка") inner(пер. "внутренний"):
    #Общепринятая практика называть функцию-обертку wrapper(пер. "обертка").
    def inner(): 
        
        print('Начало работы декоратора.')
        
        #Вызов функции, к которой применен декоратор
        func()
        
        print('Окончание работы декоратора.')
        
    #return возвращает имя вложенной функции inner вызывая "замыкание" работы функции на себя.
    return inner

@decorator  #декорируем функцию hello
def hello ():
    print('Hello World!')

if __name__ == "__main__":
    hello()
```

    Начало работы декоратора.
    Hello World!
    Окончание работы декоратора.
    

Порядок выполнения кода:
* Строка 21. Точка входа в программу.
* Строка 22. Вызываем работу функции `hello`.
* Строка 17. Вызывает работу функции-декоратора `decotaror`.
* Строка 2. Строка определния функции `decorator`
* Строка 15. В результате работы функция `decorator` возвращает имя функции `inner`
* Строка 5. Поскольку функция `hello` не содержит обязательных аргументов, то в функции `decorator` и `inner` передается в качестве аргумента ссылка в памяти на функцию `hello` и вызывается ее работа.
* Строка 18. Выполняется код внутри функции `func` и мы получаем результат. 

**Важный момент!**
Нужно понимать, что теперь при вызове функции `hello` в памяти сохранится ссылка на функцию-обертку `inner`:


```python
print(hello)
print(hello.__name__)
```

    <function decorator.<locals>.inner at 0x00000271DDEE5120>
    inner
    

**Альтернативная запись декорирования функции:**


```python
def hello ():
    print('Hello World!')

if __name__ == "__main__":
    
    #Строка кода ниже является аналогом записи @decorator перед функцией: 
    result = decorator(hello)
    
    result()
```

    Начало работы декоратора.
    Hello World!
    Окончание работы декоратора.
    

**Принцип использования нескольких `декораторов`**


```python
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

@header
@table
def hello(name):
    return print('\tHello', name)

if __name__ == '__main__':
    hello('Alex')
```

    <h1>
    <table>
    	Hello Alex
    </table>
    </h1>
    

**Еще один пример использования нескольких декораторов:**


```python
def summ(func):
    def inner(*args, **kwargs):
        
        a, b = func(*args, **kwargs)
        print(f'Функция inner через функцию декоратор summ приняла значения агрументов а = {a} и b = {b}.')
        
        x = a + b
        print(f'Результат сложения а и b равен {x} и сохранен в переменной x для передачи в следующую функцию декоратор square.')
        return x
    return inner

def square(func):
    def inner(*args, **kwargs):
        d = func(*args, **kwargs)
        w = d * d
        print(f'Результат работы функции suqre равне: {w}')
    return inner

@square
@summ
def elem(x, y):
    return x, y

if __name__ == '__main__':
    elem(5, 10)
```

    Функция inner через функцию декоратор summ приняла значения агрументов а = 5 и b = 10.
    Результат сложения а и b равен 15 и сохранен в переменной x для передачи в следующую функцию декоратор square.
    Результат работы функции suqre равне: 225
    

### Декоратор `wraps`

* Декоратор `wraps` позволяет сохранить имя функции и ее документации, после применения к ней других декораторов.

**Рассмотрим пример:**

Создадим декоратор и функцию, но для начала проверим ее работу и атрибуты без применения декораторы:


```python
def decorator(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper

def hello(name):
    """
    Функция привествует пользователя по имени!)
    """
    print('Hello', name, end='!\n')

if __name__ == '__main__':
    hello('Alex')
    
    print('Имя функции:', hello.__name__, end='\n')
    print('Документация функции:', hello.__doc__)
    
```

    Hello Alex!
    Имя функции: hello
    Документация функции: 
        Функция привествует пользователя по имени!)
        
    

* Функция возвращает результат, сохраняя при этом свое имя и документацию.
* Для более удобного и читаемого вывода документации лучше использовать функцию `help(имя_функции)`


```python
help(hello)
```

    Help on function hello in module __main__:
    
    hello(name)
        Функция привествует пользователя по имени!)
    
    

Задекорируем функцию `hello` И сравним результаты вызовов: 


```python
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@decorator
def hello(name):
    """
    Функция привествует пользователя по имени!)
    """
    print('Hello', name, end='!\n')

if __name__ == '__main__':

    hello('Alex')
    
    print('Имя функции:', hello.__name__, end='\n')
    print('Документация функции:', hello.__doc__)
    
```

    Hello Alex!
    Имя функции: wrapper
    Документация функции: None
    

* В результате мы получаем тот же рузультат работы функции, но мы потеряли оригинальное имя и документацию функции `hello`

Cохранить исходное имя и документацию функции `hello`, которую мы передаем в функцию-декоратор `decorator`, а затем  внутрь функции-обертки `wrapper` можно двумя способами:

**Способ 1.** 

Изменить напрямую атрибуты объекта (функции) `wrapper` присвоим им значения атрибутов объекта (функции) `hello`:


```python
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    
    #Вне тела функции wrapper() меняем значения ее атрибутов:
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    
    return wrapper

@decorator
def hello(name):
    """
    Функция привествует пользователя по имени!)
    """
    print('Hello', name, end='!\n')

if __name__ == '__main__':

    hello('Alex')
    
    print('Имя функции:', hello.__name__, end='\n')
    print('Документация функции:', hello.__doc__)
```

    Hello Alex!
    Имя функции: hello
    Документация функции: 
        Функция привествует пользователя по имени!)
        
    

**Способ 2.**

Более удобный, воспользуемся декоратором `wraps`


```python
from functools import wraps

def decorator(func):
    
    #Используем декоратор и передает в качетве аргумента функцию, в данном примере это будет `hello`
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        
    return wrapper

@decorator
def hello(name):
    """
    Функция привествует пользователя по имени!)
    """
    print('Hello', name, end='!\n')

if __name__ == '__main__':

    hello('Alex')
    
    print('Имя функции:', hello.__name__, end='\n')
    print('Документация функции:', hello.__doc__)
```

    Hello Alex!
    Имя функции: hello
    Документация функции: 
        Функция привествует пользователя по имени!)
        

