from django.contrib import admin

#импортируем модели приложения
from maincontent.models import *

@admin.register(MainPageContent)
class MainPageContentAdmin(admin.ModelAdmin):
    list_display =('id','content',)

@admin.register(PartnersPageContent)
class PartnersPageContentAdmin(admin.ModelAdmin):
    list_display = ('id','link','image',)

@admin.register(RequsitesPageContent)
class RequsitesPageContentAdmin(admin.ModelAdmin):
    list_display = ('id','first_column', 'second_column',)

@admin.register(ContactsPageContent)
class ContactsPageContentAdmin(admin.ModelAdmin):
    list_display =('id','content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name','slug')
    search_fields = ('name','slug',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title','text','picture',)
    list_display = ('title','text','picture','brand','category','cost')
    list_filter= ('available',)
