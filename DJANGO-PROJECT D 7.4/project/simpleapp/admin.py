from django.contrib import admin
from .models import Product, Category, News


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(News)
