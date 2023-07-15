from django.contrib import admin

# Register your models here.

from main_app.models import Product

admin.site.register(Product)