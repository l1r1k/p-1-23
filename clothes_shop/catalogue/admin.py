from django.contrib import admin
from .models import Category, Collection, Clothe
from django.utils.html import format_html

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    ordering = ['name']
    search_fields = ['name']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'year', 'season']
    ordering = ['year']
    search_fields = ['name']

@admin.register(Clothe)
class ClotheAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'photo_preview',
        'name', 
        'description', 
        'price', 
        'color', 
        'size', 
        'category', 
        'collections', 
        'created_at', 
        'updated_at',
        'is_exists'
    ]
    ordering = ['name']
    search_fields = ['name']

    def collections(self, obj):
        qs = Collection.objects.all().filter(clothe__pk=obj.pk)
        return ', '.join([collection.name for collection in qs])
    collections.short_description = 'Коллекции'

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src={} style="max-height: 150px; max-width:150px;" />',
                obj.photo.url
            )
        return format_html(
                '<img src={} style="max-height: 150px; max-width:150px;" />',
                'img/no-photo.jpg'
            )
    photo_preview.short_description = 'Фото'