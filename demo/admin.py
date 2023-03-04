from django.contrib import admin
from .models import Person, Car, Product, Order, OrderPosition


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInline]