from django.db import models
from django.urls import reverse
from django.db.models import F
import os
from tinymce.models import HTMLField

#Контент главной страницы
class MainPageContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = HTMLField()
    #Получение содержимого по api запросу к бд
    def __str__(self):
        return self.content
        
    class Meta:
        verbose_name ='контент'
        verbose_name_plural ='Контент страницы "Компания"'

#Контент страницы "Партнеры"
class PartnersPageContent(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=200)
    image = models.ImageField();

    class Meta:
        verbose_name ='контент '
        verbose_name_plural ='Контент страницы "Партнеры"'

#Контент страницы "Реквизиты"
class RequsitesPageContent(models.Model):
    id = models.AutoField(primary_key=True)
    first_column = models.CharField(max_length=200)
    second_column = models.CharField(max_length=200)

    class Meta:
        verbose_name ='контент'
        verbose_name_plural ='Контент страницы "Реквизиты"'

    #Получение содержимого по api запросу к бд
    def __str__(self):
        return self.first_column + '|' + self.second_column

#Контент страницы "Контакты"
class ContactsPageContent(models.Model):
    id = models.AutoField(primary_key=True)
    content = HTMLField()

    class Meta:
        verbose_name ='контент'
        verbose_name_plural ='Контент страницы  "Контакты"'

    #Получение содержимого по api запросу к бд
    def __str__(self):
        return self.content


#Категории продукции
class Category(models.Model):
    name = models.CharField(max_length=30, unique = True)
    slug = models.SlugField()

    class Meta:
        verbose_name ='категорию'
        verbose_name_plural ='1.Категории продукции'
    
    #Получение содержимого по api запросу к бд
    def __str__(self):
        return self.name

     #Получение url адресса по api запросу к бд
    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_slug':self.slug})

#Марки
class Brand(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name ='марку товара'
        verbose_name_plural ='2.Марки товаров'

    #Получение содержимого по api запросу к бд
    def __str__(self):
        return self.name


#Продукция

#получение пути для закгрузки изображения
def image_folder(instance,filename):
    return '{0}/{1}'.format(instance.slug,filename)

class Product(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=300)
    picture = models.ImageField(upload_to=image_folder)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    available = models.BooleanField(default = True)
    slug = models.SlugField()

    class Meta:
        verbose_name ='продукцию'
        verbose_name_plural ='3.Продукция'

 #Получение содержимого по api запросу к бд
    def __str__(self):
        return self.title

 #Получение url адресса по api запросу к бд
    def get_absolute_url(self):
        return reverse('product', kwargs = {'product_slug':self.slug})
