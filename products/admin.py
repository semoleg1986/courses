from django.contrib import admin
from .models import Product, Lesson

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'start_date', 'cost', 'min_group_size', 'max_group_size']
    list_filter = ['owner', 'start_date']
    search_fields = ['name']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'video_url']
    list_filter = ['product']
    search_fields = ['title']