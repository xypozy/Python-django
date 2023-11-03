from django.contrib import admin
from .models import Article
from .models import Product
from .models import Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    pass
