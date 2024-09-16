from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
    list_filter = ('price', 'created_at')
    search_fields = ('title', 'description')
