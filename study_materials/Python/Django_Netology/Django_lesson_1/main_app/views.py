from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from main_app.models import Product


def product_details(request, product_id):

    """ Возвращает одну запись из таблицы БД по указанному id """

    product = get_object_or_404(Product, id=product_id)

    template_name = 'product.html'

    return render(request, template_name, {'item': product})


def products_list(request):

    """ Функция возвращает из таблицы БД 'main_app_product' все записи. """

    product = Product.objects.all()

    template_name = 'list.html'

    # 'products' - это ключ, указанный в файле шаблона list.html в качестве итерируемого объекта в цикле for
    return render(request, template_name, {'products': product})


def index_page(request):

    """ Функция отправит текст на указанную в модуеле urls.py страницу проекта. """

    message = "Hello World!"

    return HttpResponse(message)
