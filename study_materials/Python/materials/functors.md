*Последние изменения внесены: `04.04.2023`*

[<<< Предыдущее меню.](/study_materials/Python/Python_study_materials.md)

# Функтор. (Функциональный объект).

> **Функтор** - это конструкция, которая позволяет использовать объект класса как функцию.
    

Рассмотрим пример:


```python
class Functors:
    
    def __init__(self, degree):
        self.degree = degree
    
    def __call__(self, number):
        return number ** self.degree

if __name__ == '__main__':
    
    square = Functors(2)
    result_1 = square(2)
    
    cube = Functors(3)
    result_2 = cube(5)
    
    print(result_1)
    print(result_2)
    
    
```

    4
    125
    

* В данном примере мы создаем два объекта класса `Functors`
* `square` используем для возведения передаваемого в него числа (аргумента) в квадрат.
* `cube` используем для возведения передаваемого в него числа (аргумента) в куб.
* Мы создали два объекта класса способные принимать аргументы и вызываться как функции, за эту возможность в нашем классе отвечает метод `__call__`.

[<<< Предыдущее меню.](/study_materials/Python/Python_study_materials.md)


```python

```
